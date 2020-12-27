def get_itinerary(start, flights):
    itinerary = []
    exists = _get_itinerary_work(start, flights, itinerary, set())
    return itinerary[::-1] if exists is True else None


def _get_itinerary_work(start, flights, itinerary, visited):
    if 0 < len(flights) == len(visited):
        return True
    for src, dst in flights:
        if (src, dst) not in visited and src == start:
            visited.add((src, dst))
            exists = _get_itinerary_work(dst, flights, itinerary, visited)
            visited.remove((src, dst))
            if exists:
                itinerary.append((src, dst))
                return True
    return False
