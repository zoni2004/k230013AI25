model=cp_model.CpModel()
ub=50
x=model.new_int_var(0,ub,"x")
y=model.new_int_var(0,ub,"y")
z=model.new_int_var(0,ub,"z")
model.add(2 * x + 7 * y + 3 * z <= 50)
model.add(3 * x - 5 * y + 7 * z <= 45)
model.add(5 * x + 2 * y - 6 * z <= 37)

model.maximize(2 * x + 2 * y + 3 * z)
solver=cp_model.CpSolver()
status=solver.Solve(model)
if status==  cp_model.OPTIMAL or status==cp_model.FEASIBLE:
  print(solver.objective_value)
  print(f"x={solver.value(x)}")
  print(f"y={solver.Value(y)}")
  print(f"z={solver.Value(z)}")
else:
  print("None")
  print(f"  status   : {solver.status_name(status)}")
print(f"  conflicts: {solver.num_conflicts}")
print(f"  branches : {solver.num_branches}")
print(f"  wall time: {solver.wall_time} s")

class AllSolutions(cp_model.CpSolverSolutionCallback):
  def __init__(self,variables :list[cp_model.IntVar]):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0

  def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)}  ")
        print()

  @property
  def solution_count(self) -> int:
    return self.__solution_count
solver=cp_model.CpSolver()
solution_printer=AllSolutions([x,y,z])
solver.parameters
status=solver.solve(model,solution_printer)
