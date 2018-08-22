def comeOnDown(maxPrice, bids):
    bids.append(maxPrice)
    bids.sort()
    maxInterval = 0
    optimalBid = 0
    previousBid = 0
    for bid in bids:
        if bid > maxPrice:
            continue
        currentBid = bid
        if currentBid == maxPrice:
            interval = len(range(previousBid + 1, currentBid + 1))
        else:
            interval = len(range(previousBid + 1, currentBid))
        if interval > maxInterval:
            maxInterval = interval
            optimalBid = previousBid + 1
        previousBid = bid
    return optimalBid
