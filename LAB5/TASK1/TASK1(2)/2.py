from ortools.sat.python import cp_model

products = [
    {"id": 1, "frequency": 15, "volume": 2},
    {"id": 2, "frequency": 8,  "volume": 1},
    {"id": 3, "frequency": 20, "volume": 3}
]

slots = [
    {"id": 1, "distance": 1, "capacity": 3},
    {"id": 2, "distance": 2, "capacity": 2},
    {"id": 3, "distance": 3, "capacity": 2}
]

model = cp_model.CpModel()
assignment = {}

for i in range(len(products)):
    for j in range(len(slots)):
        assignment[(i, j)] = model.new_bool_var(f"p{products[i]['id']}_s{slots[j]['id']}")

for i in range(len(products)):
    model.add(sum(assignment[(i, j)] for j in range(len(slots))) == 1)

for j in range(len(slots)):
    model.add(
        sum(assignment[(i, j)] * products[i]["volume"] for i in range(len(products)))
        <= slots[j]["capacity"]
    )

model.Minimize(
    sum(
        assignment[(i, j)] * products[i]["frequency"] * slots[j]["distance"]
        for i in range(len(products))
        for j in range(len(slots))
    )
)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    for i in range(len(products)):
        for j in range(len(slots)):
            if solver.value(assignment[(i, j)]) == 1:
                print(f"Product {products[i]['id']} assigned to Slot {slots[j]['id']}")
    print(f"Minimum Total Walking Distance: {solver.objective_value}")
else:
    print("No solution found.")
