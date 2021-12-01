import numpy as np
import pandas as pd

from src.parsers import main_parser
import src.data_gen as dg
import src.graph_utils as gu
import src.opt_utils as opt


def main():
    args = main_parser().parse_args()

    np.random.seed(seed=args.seed)

    N_SEATS = args.n_seats
    ALPHA = 1.0 / 3 if args.mode == 'stop' else 2.0 / 3
    NODE_SIZE = 2000

    # COSTS = np.random.uniform(low=0, high=1, size=N_SEATS)
    # WEIGHTS = np.random.randint(low=1, high=args.max_weight + 1, size=N_SEATS)
    COSTS = dg.get_costs(n_nodes=args.n_nodes, zipf_coeffs=args.zipfc)[:N_SEATS]
    WEIGHTS = dg.get_voting_power(n_nodes=args.n_nodes)[:N_SEATS]
    
    if not args.novis:
        H, W, nodes_pos = gu.layout(n_seats=N_SEATS, node_size=NODE_SIZE)
        gu.plot(
                n_seats=N_SEATS,
                mode=args.mode,
                costs=COSTS,
                weights=WEIGHTS,
                nodes_pos=nodes_pos,
                node_size=NODE_SIZE,
                fig_w=W,
                fig_h=H,
                solved=False,
                latex=args.latex,
                show=not args.hide_plots,
                )
    
    model = opt.get_model(n_seats=N_SEATS, alpha=ALPHA, costs=COSTS, weights=WEIGHTS, mode=args.mode)

    instance, min_voting_power, adversary_voting_power, adversary_cost, selected_seats, colors =\
            opt.solve(model=model, solver_name=args.solver, verbose=args.verbose)

    if not args.novis:
        gu.plot(
                n_seats=N_SEATS,
                mode=args.mode,
                costs=COSTS,
                weights=WEIGHTS,
                nodes_pos=nodes_pos,
                node_size=NODE_SIZE,
                fig_w=W,
                fig_h=H,
                solved=True,
                min_voting_power=min_voting_power,
                adversary_voting_power=adversary_voting_power,
                adversary_cost=adversary_cost,
                colors=colors,
                latex=args.latex,
                show=not args.hide_plots,
                )
    
    if args.verbose:
        df = pd.DataFrame()
        df['seat'] = pd.Series(range(1, N_SEATS + 1))
        df['cost'] = pd.Series(COSTS)
        df['weight'] = pd.Series(WEIGHTS)
        df['selected'] = pd.Series(instance.x.get_values().values()).astype(bool)
        print(df)
        print()

        print('To {} the committee with the total voting power of {},'.format(args.mode, WEIGHTS.sum()))
        print('an adversary needs to obtain at least voting power of {:.2f}.'.format(min_voting_power))
        print('The minimum cost of doing this is {:.6f}.'.format(adversary_cost))
        print('Seats to be selected:', selected_seats)
        print('Obtained voting power: {}'.format(adversary_voting_power))


if __name__ == '__main__':
    main()
