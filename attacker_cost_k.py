# Calculates attacker cost as a function of Zipf coefficient and k in k-scheme

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.parsers import attacker_cost_k_parser
import src.data_gen as dg
import src.opt_utils as opt


def main():
    args = attacker_cost_k_parser().parse_args()

    ALPHA = 1.0 / 3 if args.mode == 'stop' else 2.0 / 3
    ZIPF_COEFFS = np.arange(start=args.zipfc_min, stop=args.zipfc_max + args.zipfc_step,
            step=args.zipfc_step)
    attacker_costs_k = {}

    for k in range(1, args.k_max + 1):
        weights = dg.get_voting_power(n_seats=args.n_seats, k=k)
        attacker_costs = np.empty_like(ZIPF_COEFFS)

        for i, s in enumerate(ZIPF_COEFFS):
            if args.verbose:
                print('Solving problem for k={:d}, zipfc={:.2f}'.format(k, s))
            costs = dg.get_costs(n_nodes=args.n_nodes, zipf_coeffs=s)[:args.n_seats]
            
            model = opt.get_model(n_seats=args.n_seats, alpha=ALPHA, costs=costs, weights=weights,
                    mode=args.mode)

            _, _, _, attacker_cost, _, _ = opt.solve(model=model, solver_name=args.solver,
                    verbose=args.verbose)

            attacker_costs[i] = attacker_cost
        attacker_costs_k['k={:d}'.format(k)] = attacker_costs
    
    if args.csv:
        data = {'s': ZIPF_COEFFS}
        for k, v in attacker_costs_k.items():
            data['cost for ' + k] = v
        df = pd.DataFrame(data)

        fname = '{}_cost_k.csv'.format(args.mode)
        if os.path.isfile(fname):
            print('File {} exists: o - overwrite, n - enter new file name, c - cancel saving data'.\
                    format(fname))

            i = input('Enter your choice: ')
            if i == 'o':
                df.to_csv(fname, index=False)
                print('Data saved in {}'.format(fname))
            elif i == 'n':
                fname = input('Type new file name: ')
                while not fname or fname == 'costs.csv':
                    fname = input('Type new file name: ')

                df.to_csv(fname, index=False)
                print('Data saved in {}'.format(fname))
            else:
                print('Data has not been be saved')
        else:
            df.to_csv(fname, index=False)
            print('Data saved in {}'.format(fname))

    if args.latex:
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
        plt.rc('text', usetex=True)
    
    if args.latex:
        title = r'{\bf Minimum attacker cost to %s the committee as a function of $s$ and $k$}' % \
                args.mode
    else:
        title = 'Minimum attacker cost to {} the committee as a function of s and k'.\
                format(args.mode)
    plt.title(label=title, fontweight='bold')

    for k, v in attacker_costs_k.items():
        label = r'$%s$' % k if args.latex else k
        plt.plot(ZIPF_COEFFS, v, label=label)
    plt.xlabel('Zipf coefficient s')
    plt.ylabel('Attacker cost')
    plt.legend()

    if not args.hide_plots:
        plt.show()
        # d = np.empty(shape=(len(attacker_costs_k['k=1']), len(attacker_costs_k)))
        # for i, v in enumerate(attacker_costs_k.values()):
            # d[:, i] = v
        # _, _ = heatmap(data=d, row_labels=ZIPF_COEFFS, col_labels=np.arange(1, args.k_max + 1))
        # plt.show()
    

if __name__ == '__main__':
    main()
