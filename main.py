import numpy as np
import pandas as pd
import pyomo.environ as pe

np.random.seed(2021)

N_SEATS = 1000
ALPHA = 1.0 / 3
COSTS = np.random.uniform(low=0, high=1, size=N_SEATS)
WEIGHTS = np.random.randint(low=1, high=20, size=N_SEATS)


def c1_rule(model):
    return sum([model.w[i] * model.x[i] for i in model.i]) >= \
            model.alpha * sum([model.w[i] for i in model.i])


def obj_rule(model):
    return sum([model.c[i] * model.x[i] for i in model.i])


model = pe.AbstractModel()
model.N = pe.Param(initialize=N_SEATS)
model.alpha = pe.Param(initialize=ALPHA)

model.i = pe.RangeSet(model.N)
model.c = pe.Param(model.i, initialize=dict(zip(range(1, N_SEATS + 1), COSTS)))
model.w = pe.Param(model.i, initialize=dict(zip(range(1, N_SEATS + 1), WEIGHTS)))
model.x = pe.Var(model.i, domain=pe.Binary)


model.c1 = pe.Constraint(rule=c1_rule)
model.obj = pe.Objective(rule=obj_rule, sense=pe.minimize)

solver = pe.SolverFactory('glpk')
# solver.options['max_iter'] = 10000
instance = model.create_instance()
results = solver.solve(instance)

if results.solver.status == pe.SolverStatus.ok and \
        results.solver.termination_condition == pe.TerminationCondition.optimal:
    print('\nSolution is optimal and feasible')
elif results.solver.termination_condition == pe.TerminationCondition.infeasible:
    print('\nThe model is infeasible')
else:
    print('\nSomething else is wrong: solver status:', results.solver.status)

instance.display()
print(results)
instance.x.pprint()
instance.obj.pprint()
print()

df = pd.DataFrame()
df['seat'] = pd.Series(range(1, N_SEATS + 1))
df['cost'] = pd.Series(COSTS)
df['weight'] = pd.Series(WEIGHTS)
df['x'] = pd.Series(instance.x.get_values().values())
print(df)

print()
print('OF =', pe.value(instance.obj))
