from scipy.optimize import linear_sum_assignment

commanders = {
    0: "Kadena, Sinking Sorceror",
    1: "Ghired, Conclave Exile",
    2: "Anje Falkenrath",
    3: "Sevinne, the Chronoclasm",
}

friends = {
    0: "Alex",
    1: "Adam",
    2: "George",
    3: "Mike"
}

costs = {
    "1st": 1,
    "2nd": 5,
    "3rd": 10,
    "4th": 15
}

Alex = [
    "Kadena, Sinking Sorceror",
    "Ghired, Conclave Exile",
    "Anje Falkenrath",
    "Sevinne, the Chronoclasm",
]
Adam = [
    "Anje Falkenrath",
    "Kadena, Sinking Sorceror",
    "Ghired, Conclave Exile",
    "Sevinne, the Chronoclasm"
]
George = [
    "Anje Falkenrath",
    "Ghired, Conclave Exile",
    "Sevinne, the Chronoclasm",
    "Kadena, Sinking Sorceror",
]
Mike = [
    "Kadena, Sinking Sorceror",
    "Anje Falkenrath",
    "Ghired, Conclave Exile",
    "Sevinne, the Chronoclasm"
]

all_costs = [[1, 5, 10, 15], [5, 10, 1, 15], [15, 5, 1, 10], [1, 10, 5, 15]]

row_ind, col_ind = linear_sum_assignment(all_costs)

print(f"The optimal column index is: {col_ind}")

optimal_commanders_order = []
for i in col_ind:
    optimal_commanders_order.append(commanders[i])

print(
    f"The optimal commander choices for {friends} order is: {optimal_commanders_order}"
)
