import math


# https://www.youtube.com/watch?v=2uxXPzm-7FY
def tf_idf(docs, target, subject):
    n_docs = len(docs)
    tf = {}
    idf = {}
    term_dc = {}

    # Step 1: Build term frequency
    for ix, doc in docs.items():
        current = tf[ix] = {}
        for line in doc:
            terms = line.split(" ")
            for term in terms:
                if term not in current:
                    current[term] = 0
                current[term] += 1
        for key in current.keys():
            if key not in term_dc:
                term_dc[key] = 0
            term_dc[key] += 1

    # Step 2: Build inverse document frequency
    for term, doc_count in term_dc.items():
        idf[term] = math.log(n_docs / doc_count)

    # Step 3: Return weight of subject for target doc
    return tf[target].get(subject, 0) * idf.get(subject, 0.0)


def main():
    docs = {
        "Hello": [
            "Lorem ipsum",
            "ipsum is cool",
            "cool is nothing blah",
            "blah blah blah blah blah blah",
        ],
        "World": ["Lorem lorem", "lorem lorem lorem is", "nothing"],
        "Taxi": ["Lorem", "is"],
        "Bus": ["is is is"],
        "Arg": ["has is"],
    }
    print(tf_idf(docs, "Hello", "blah"))
    print(tf_idf(docs, "Taxi", "Lorem"))
    print(tf_idf(docs, "Arg", "has"))
    print(tf_idf(docs, "Bus", "is"))
    print(tf_idf(docs, "World", "blah"))
    print(tf_idf(docs, "Arg", "foobar"))


if __name__ == "__main__":
    main()
