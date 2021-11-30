import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def layout(n_seats, node_size):
    # position of nodes, height and width of the figure
    n_rows = int(np.floor(np.sqrt(n_seats)))
    n_cols = int(np.floor(n_seats/n_rows))

    remain = n_seats - n_rows * n_cols
    n_cols = n_cols + 1 if remain else n_cols

    H = (3 * n_rows + 1) * node_size / 2
    W = (3 * n_cols + 1) * node_size / 2

    pos = []

    for row in range(n_rows):
        y = (1 + 3 * row / 2) * node_size
        for col in range(n_cols):
            x = (1 + 3 * col / 2) * node_size
            pos += [[x, y]]
            if row == n_rows - 1 and len(pos) == n_seats:
                break
    pos = dict(zip(range(1, n_seats + 1), pos))
    
    return H, W, pos


def plot(n_seats, mode, costs, weights, nodes_pos, node_size, fig_w, fig_h,
        solved=False, min_voting_power=None,
        adversary_voting_power=None, adversary_cost=None, colors=None, latex=False, show=True):
    if latex:
        plt.rcParams['font.size'] = 11
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
        plt.rc('text', usetex=True)

    G = nx.Graph()
    labels = {}

    for seat in range(1, n_seats + 1):
        if latex:
            seat_ = r'{\bf %d}' % seat
            c = r'$C=%.2f$' % costs[seat-1]
            v = r'$V=%d$' % weights[seat-1]
        else:
            seat_ = seat
            c = 'C={:.2f}'.format(costs[seat-1])
            v = 'V={}'.format(weights[seat-1])
        label = '{}\n{}\n{}'.format(seat_, c, v)
        labels[seat] = label
        G.add_node(seat)

    _, ax = plt.subplots()

    title = 'Committee with {} seats'.format(n_seats)
    if solved:
        title = title + ', mode: {}'.format(mode)
        assert min_voting_power is not None
        assert adversary_voting_power is not None
        assert adversary_cost is not None
        assert colors is not None
    if latex:
        title = r'{\bf %s}' % title
    plt.title(label=title, fontweight='bold', fontsize=14 if latex else 11)

    plt.xlim([0, fig_w])
    plt.ylim([0, fig_h])

    if latex:
        c_label = r'$C$---cost'
        v_label = r'$V$---voting power'
        if solved:
            minV_label = r'$V_{min}=%.2f$' %  min_voting_power
            advV_label = r'$V_{adv}=%d$' % adversary_voting_power
            advC_label = r'$C_{adv}=%.2f$' %  adversary_cost
    else:
        c_label = 'C - cost'
        v_label = 'V - voting power'
        if solved:
            minV_label = 'minV={:.2f}'.format(min_voting_power)
            advV_label = 'advV={}'.format(adversary_voting_power)
            advC_label = 'advC={:.2f}'.format(adversary_cost)

    if solved:
        plt.plot(-np.inf, -np.inf, linestyle='', marker='o', color='green', label='Selected by adversary')
    plt.plot(-1, -1, linestyle='', color='white', label=c_label)
    plt.plot(-1, -1, linestyle='', color='white', label=v_label)
    if solved:
        plt.plot(-1, -1, linestyle='', color='white', label=minV_label)
        plt.plot(-1, -1, linestyle='', color='white', label=advV_label)
        plt.plot(-1, -1, linestyle='', color='white', label=advC_label)

    nx.draw(
            G=G,
            pos=nodes_pos,
            ax=ax,
            with_labels=True,
            labels=labels,
            node_size=node_size,
            node_color='orange' if colors is None else colors,
            font_size=11 if latex else 10,
            )
    if solved:
        plt.legend()
    else:
        plt.legend(handlelength=0)

    if show:
        plt.show()
