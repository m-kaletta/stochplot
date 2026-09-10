import numpy as np

from stochplot import Ensemble, EnsembleVisualizer


# creates an ensemble of a numerical simulation of a wiener process
def wiener(time_len, num_steps, num_processes, seed=1):
    time_increment = time_len / num_steps
    np.random.seed(seed)
    increments = np.sqrt(time_increment) * np.random.randn(num_processes, num_steps-1)
    return Ensemble(time_len, increments=increments)

# solves the SDE of geometric brownian motion using the euler-maruyama method
# uses the ensemble of a numerical simulation of a wiener process as basis
def solve_geometric_brownian(wiener_ensemble, mu, sigma):
    ito_process = np.zeros(wiener_ensemble.shape)
    ito_process[:, 0] = 0.1  # initial value
    for time_idx in range(1, wiener_ensemble.num_steps):
        prev_ito = ito_process[:, time_idx-1]
        drift = mu * prev_ito * wiener_ensemble.time_increment
        diffusion = sigma * prev_ito * wiener_ensemble.increments[:, time_idx-1]
        ito_process[:, time_idx] = prev_ito + drift + diffusion
    return Ensemble(wiener_ensemble.time_len, processes=ito_process)

wiener_ensemble = wiener(2, 100, 1000)
gbm_ensemble = solve_geometric_brownian(wiener_ensemble, mu=1.2, sigma=0.8)
visualizer = EnsembleVisualizer(gbm_ensemble, 'geometric brownian Motion', y_label='value', y_range=[-1.8, 4.0])
visualizer.plot_swarm()
# for the high dynamic range of the GBM only the normalized versions are visually tangible
visualizer.plot_ensemble_distribution('hist norm')
visualizer.plot_ensemble_curve_dist('kde norm')
visualizer.plot_ensemble_curve_dist('hist norm')
