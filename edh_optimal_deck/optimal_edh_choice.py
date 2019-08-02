from scipy.optimize import linear_sum_assignment

commanders = {
    "Kadena, Sinking Sorceror": 1,
    "Ghired, Conclave Exile": 2,
    "Angie Falkenrath": 3,
    "Sevinne, the Chronoclasm": 4
}

Alex = ["Kadena, Sinking Sorceror", "Ghired, Conclave Exile", "Angie Falkenrath", "Sevinne, the Chronoclasm"]
Adam = []
George = []
Mike = []

all_rankings = [[1, 2, 3, 4], [], [], []]

row_ind, col_ind = linear_sum_assignment(all_rankings)

print(f"The optimal column index is: {col_ind}")
print(f"The optimal row index is: {row_ind}")
