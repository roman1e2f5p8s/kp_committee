import numpy as np
import matplotlib.pyplot as plt

from src.parsers import costs_parser
import src.data_gen as dg


def main():
    args = costs_parser().parse_args()

    zipf_coeffs = np.arange(start=args.zipfc_min, stop=args.zipfc_max + args.zipfc_step,
            step=args.zipfc_step)

    costs = {}

    for i, z in enumerate(zipf_coeffs):
        cost = dg.get_costs(n_nodes=args.n_nodes, zipf_coeffs=z)#[:args.n_seats]
        costs['s={:.1f}'.format(z)] = cost

    if args.latex:
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
        plt.rc('text', usetex=True)
    
    title = 'Cost as a function of rank and Zipf coefficient'
    if args.latex:
        title = r'{\bf %s}' % title
    plt.title(label=title, fontweight='bold')

    for k, v in costs.items():
        plt.plot(np.arange(1, args.n_nodes + 1), v, label=k)
    plt.xlabel('Rank')
    plt.ylabel('Cost')
    plt.xscale('log')
    plt.yscale('log')
    # plt.ylim([0, 0.05])
    plt.legend()

    if not args.hide_plots:
        plt.show()
    

if __name__ == '__main__':
    main()
