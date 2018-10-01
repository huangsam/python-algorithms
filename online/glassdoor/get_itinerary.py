def get_itinerary(start, flights):
    itinerary = []
    exists = get_itinerary_work(start, flights, itinerary, set())
    return itinerary[::-1] if exists is True else None


def get_itinerary_work(start, flights, itinerary, visited):
    if len(flights) == len(visited):
        itinerary.append(start)
        return True
    exists = False
    for src, dst in flights:
        if (src, dst) not in visited and src == start:
            visited.add((src, dst))
            exists |= get_itinerary_work(dst, flights, itinerary, visited)
            visited.remove((src, dst))
    if exists:
        itinerary.append(start)
    return exists
