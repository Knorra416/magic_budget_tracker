from __future__ import print_function
from ortools.graph import pywrapgraph

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


def main():
    cost = create_data_array()
    rows = len(cost)
    cols = len(cost[0])

    assignment = pywrapgraph.LinearSumAssignment()
    for worker in range(rows):
        for task in range(cols):
            if cost[worker][task]:
                assignment.AddArcWithCost(worker, task, cost[worker][task])
    solve_status = assignment.Solve()
    if solve_status == assignment.OPTIMAL:
        print("Total cost = ", assignment.OptimalCost())
        print()
        for i in range(0, assignment.NumNodes()):
            print(
                "Friend %s assigned to task %s.  Cost = %d"
                % (friends[i], commanders[assignment.RightMate(i)], assignment.AssignmentCost(i))
            )
    elif solve_status == assignment.INFEASIBLE:
        print("No assignment is possible.")
    elif solve_status == assignment.POSSIBLE_OVERFLOW:
        print("Some input costs are too large and may cause an integer overflow.")


def create_data_array():
    cost = [[1, 5, 10, 15], [], [15, 5, 1, 10], [1, 10, 5, 15]]
    return cost


if __name__ == "__main__":
    main()
