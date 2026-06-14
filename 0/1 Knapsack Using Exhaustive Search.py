from itertools import combinations

def total_value(selected_items, values):

    value = 0

    for item in selected_items:
        value += values[item]

    return value


def is_feasible(selected_items, weights, capacity):

    total_weight = 0

    for item in selected_items:
        total_weight += weights[item]

    return total_weight <= capacity


def knapsack(weights, values, capacity):

    n = len(weights)

    best_value = 0
    best_items = []

    for r in range(n + 1):

        for subset in combinations(range(n), r):

            if is_feasible(subset, weights, capacity):

                value = total_value(subset, values)

                if value > best_value:
                    best_value = value
                    best_items = subset

    return best_items, best_value


# Test Case 1
weights = [2,3,1]
values = [4,5,3]
capacity = 4

items, value = knapsack(weights, values, capacity)

print("Selected Items:", items)
print("Maximum Value:", value)


# Test Case 2
weights = [1,2,3,4]
values = [2,4,6,3]
capacity = 6

items, value = knapsack(weights, values, capacity)

print("Selected Items:", items)
print("Maximum Value:", value)