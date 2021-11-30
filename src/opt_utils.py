import pyomo.environ as pe


def get_model(n_seats, alpha, costs, weights):
    model = pe.AbstractModel()

    model.N = pe.Param(initialize=n_seats)
    model.alpha = pe.Param(initialize=alpha)
    
    model.i = pe.RangeSet(model.N)
    model.c = pe.Param(model.i, initialize=dict(zip(range(1, n_seats + 1), costs)))
    model.w = pe.Param(model.i, initialize=dict(zip(range(1, n_seats + 1), weights)))

    model.x = pe.Var(model.i, domain=pe.Binary)

    def c1_rule(model):
        return sum([model.w[i] * model.x[i] for i in model.i]) >= \
                model.alpha * sum([model.w[i] for i in model.i])
    model.c1 = pe.Constraint(rule=c1_rule)
    
    
    def obj_rule(model):
        return sum([model.c[i] * model.x[i] for i in model.i])
    model.obj = pe.Objective(rule=obj_rule, sense=pe.minimize)

    return model


def solve(model, solver_name):
    solver = pe.SolverFactory(solver_name)
    instance = model.create_instance()
    results = solver.solve(instance)
    
    if results.solver.status == pe.SolverStatus.ok and \
            results.solver.termination_condition == pe.TerminationCondition.optimal:
        print('Solution is optimal and feasible')
    elif results.solver.termination_condition == pe.TerminationCondition.infeasible:
        print('The model is infeasible')
        exit()
    else:
        print('Something else is wrong: solver status:', results.solver.status)
        exit()
    
    min_voting_power = 0
    adversary_voting_power = 0
    adversary_cost = 0
    selected_seats = []
    colors = []

    for s, x, w, c in zip(instance.i, instance.x.get_values().values(),
            instance.w.values(), instance.c.values()):
        if x:
            colors += ['green']
            adversary_voting_power += w
            adversary_cost += c
            selected_seats += [s]
        else:
            colors += ['orange']
        min_voting_power += w
    min_voting_power *= instance.alpha

    return instance, min_voting_power, adversary_voting_power, adversary_cost, selected_seats, colors
