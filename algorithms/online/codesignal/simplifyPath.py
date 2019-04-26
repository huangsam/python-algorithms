def simplifyPath(path):
    tokens = path.split("/")
    simple = []
    for token in tokens:
        if token == "." or len(token) == 0:
            continue
        elif token == "..":
            if len(simple) > 0:
                simple.pop()
            continue
        simple.append(token)
    return "/" + "/".join(simple)
