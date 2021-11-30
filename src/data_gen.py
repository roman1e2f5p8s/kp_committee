import numpy as np


def get_costs(n_nodes, zipf_coeffs):
    zipf_coeffs = zipf_coeffs * np.ones(n_nodes) if np.isscalar(zipf_coeffs) else zipf_coeffs

    costs = np.array([1.0 / np.power(i+1, s) for i, s in enumerate(zipf_coeffs)])
    
    return costs / costs.sum()


def get_voting_power(n_nodes):
    return np.ones(n_nodes)
