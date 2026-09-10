import numpy as np

from stochplot import Ensemble, EnsembleVisualizer, Moments


# creates an ensemble of a numerical simulation of a wiener process
def wiener(time_len, num_steps, num_processes, seed=1):
    time_increment = time_len / num_steps
    np.random.seed(seed)
    increments = np.sqrt(time_increment) * np.random.randn(num_processes, num_steps-1)
    return Ensemble(time_len, increments=increments)


ensemble = wiener(1, 100, 500)
moments = Moments(mean=np.zeros(ensemble.num_steps), std=np.sqrt(ensemble.time))

# plot the wiener process
visualizer = EnsembleVisualizer(ensemble, 'wiener process', y_label='value', y_range=[-2.2, 2.2])
visualizer.plot_single_example()
visualizer.plot_ensemble_distribution(method='kde')
visualizer.plot_ensemble_distribution(method='hist norm')  # normalizes by the standard deviation for similar max value
visualizer.plot_ensemble_curve_dist(method='kde')
visualizer.plot_ensemble_curve_dist(method='hist norm')    # normalizes by the standard deviation for similar max height

# plot the wiener process with analytical moments and empirical moments
visualizer = EnsembleVisualizer(ensemble, 'wiener process w. moments', y_label='value', y_range=[-2.2, 2.2], analytical_moments=moments)
visualizer.plot_swarm()
visualizer.plot_ensemble_distribution(method='hist')
visualizer.plot_ensemble_distribution(method='kde norm')   # normalizes by the standard deviation for similar max value
visualizer.plot_ensemble_curve_dist(method='kde')
visualizer.plot_ensemble_curve_dist(method='hist norm')    # normalizes by the standard deviation for similar max height
