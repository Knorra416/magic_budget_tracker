from scipy.optimize import linear_sum_assignment

commanders = {
    0: "Kadena, Sinking Sorceror",
    1: "Ghired, Conclave Exile",
    2: "Angie Falkenrath",
    3: "Sevinne, the Chronoclasm"
}

Alex = ["Kadena, Sinking Sorceror", "Ghired, Conclave Exile", "Angie Falkenrath", "Sevinne, the Chronoclasm"]
Adam = []
George = []
Mike = []

friends = ["Alex", "Adam", "George", "Mike"]

all_rankings = [[0, 1, 2, 3], [], [], []]

row_ind, col_ind = linear_sum_assignment(all_rankings)

print(f"The optimal column index is: {col_ind}")

optimal_commanders_order = []
for i in col_ind:
    optimal_commanders_order.append(commanders[i])

print(f"The optimal commander choices in {friends} order is: {optimal_commanders_order}")
