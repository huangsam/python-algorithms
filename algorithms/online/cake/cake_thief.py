def max_duffel_bag_value(cake_tuples, capacity):
    """Get maximum value out of existing cakes.

    Worst-case: O(cake_tuples) * O(capacity)
    Average-case: O(cake_tuples) * O(capacity)

    Args:
        cake_tuples (tuple): Weight followed by value
        capacity (int): How much weight duffel bag can carry

    Returns:
        int: Maximum value that can be retrieved.
    """
    weights = [0]
    weight_value = {0: 0}
    max_value = 0
    while len(weights) > 0:
        current_weight = weights.pop()
        current_value = weight_value[current_weight]
        for cake_weight, cake_value in cake_tuples:
            if cake_weight == 0:
                continue
            new_weight = current_weight + cake_weight
            new_value = current_value + cake_value
            if new_weight > capacity:
                continue
            weights.append(new_weight)
            value = weight_value.get(new_weight)
            if value is None or value < new_value:
                weight_value[new_weight] = new_value
                if max_value < new_value:
                    max_value = new_value
    return max_value
