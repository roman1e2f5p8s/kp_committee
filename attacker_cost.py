import numpy as np
import matplotlib.pyplot as plt

from src.parsers import attacker_cost_parser
import src.data_gen as dg
import src.opt_utils as opt


def main():
    args = attacker_cost_parser().parse_args()

    ALPHA = 1.0 / 3 if args.mode == 'stop' else 2.0 / 3
    WEIGHTS = dg.get_voting_power(n_nodes=args.n_nodes)[:args.n_seats]

    zipf_coeffs = np.arange(start=args.zipfc_min, stop=args.zipfc_max + args.zipfc_step,
            step=args.zipfc_step)

    attacker_costs = np.empty_like(zipf_coeffs)

    for i, z in enumerate(zipf_coeffs):
        if args.verbose:
            print('Solving problem for zipfc={:.2f}'.format(z))
        costs = dg.get_costs(n_nodes=args.n_nodes, zipf_coeffs=z)[:args.n_seats]
        
        model = opt.get_model(n_seats=args.n_seats, alpha=ALPHA, costs=costs, weights=WEIGHTS,
                mode=args.mode)

        _, _, _, attacker_cost, _, _ = opt.solve(model=model, solver_name=args.solver,
                verbose=args.verbose)

        attacker_costs[i] = attacker_cost

    if args.latex:
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
        plt.rc('text', usetex=True)
    
    title = 'Minimum attacker cost to {} the committee as a function of Zipf coefficient'.\
            format(args.mode)
    if args.latex:
        title = r'{\bf %s}' % title
    plt.title(label=title, fontweight='bold')

    plt.plot(zipf_coeffs, attacker_costs)
    plt.xlabel('Zipf coefficient')
    plt.ylabel('Attacker cost')

    if not args.hide_plots:
        plt.show()
    

if __name__ == '__main__':
    main()
