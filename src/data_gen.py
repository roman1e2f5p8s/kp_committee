import numpy as np


def get_costs(n_nodes, zipf_coeffs):
    zipf_coeffs = zipf_coeffs * np.ones(n_nodes) if np.isscalar(zipf_coeffs) else zipf_coeffs

    costs = np.array([1.0 / np.power(i+1, s) for i, s in enumerate(zipf_coeffs)])
    
    return costs / costs.sum()


def get_voting_power(n_nodes, k):
    vp = np.zeros(n_nodes, dtype=int)

    for kk in range(k, 0, -1):
        if kk == k:
            low_i = n_nodes * (kk - 1) / kk # inclusive
            low_i = int(np.ceil(low_i))
            # print('kk={}, low_i={}'.format(kk, low_i))
            idx = [i for i in range(low_i - 1, n_nodes)]
        elif kk == 1:
            up_i = n_nodes / 2 # exclusive
            up_i = int(np.floor(up_i))
            # print('kk={}, up_i={}'.format(kk, low_i))
            idx = [i for i in range(up_i)]
        else:
            low_i = n_nodes * (kk - 1) / kk # inclusive
            low_i = int(np.ceil(low_i))
            up_i = n_nodes * kk / (kk + 1) # exclusive
            up_i = int(np.floor(up_i))
            # print('kk={}, low_i={}, up_i={}'.format(kk, low_i, up_i))
            idx = [i for i in range(low_i - 1, up_i)]
        vp[idx] = kk
    
    assert (vp > 0).all()
    return vp
