![License](https://img.shields.io/badge/license-MIT-blue)

# stochplot

Visualizations for ensembles of stochastic processes: 
- singe paths
- mean and standard deviations over time
- distribution over time by a heatmap encoding the density as intensity
- distribution over time by showing estimations of the curves of probability density functions 


## Installation
Install from a local checkout (recommended for development inside a virtualenv):
```
python -m pip install -e .
```

Install the latest published source directly from GitHub (for usage only):
```
pip install git+https://github.com/m-kaletta/stochplot.git
```

Editable/development install directly from GitHub (no clone required):
```
pip install -e git+https://github.com/m-kaletta/stochplot.git
```


## Usage

### Examples
Creating a Wiener-process ensemble and render some visualizations of it

```python
import numpy as np
from stochplot import Ensemble, EnsembleVisualizer


def wiener(time_len, num_steps, num_processes, seed=1):
    time_increment = time_len / num_steps
    np.random.seed(seed)
    increments = np.sqrt(time_increment) * np.random.randn(num_processes, num_steps-1)
    return Ensemble(time_len, increments=increments)

# create an ensemble of a numerical simulation of a wiener process
ensemble = wiener(1, 100, 500)
# create a visualizer object that produces plots as svg-files
visualizer = EnsembleVisualizer(ensemble, 'wiener process', y_label='value', y_range=[-2.2, 2.2])
visualizer.plot_swarm()
visualizer.plot_ensemble_distribution(method="kde")
visualizer.plot_ensemble_curve_dist(method="kde")
```

Further examples can be found at
- examples/visualize_wiener_process.py — more exhaustive Wiener process visualizations
- examples/visualize_geometric_brownian.py — geometric Brownian motion example

### Public API
- `Ensemble` in `ensemble.py`, encapsulate a collection of paths of a stochastic process to resemble that stochastic process numerically. 
- `Moments` in `visualizer.py` is a container for the standard deviation and mean value of a stochastic process as it evolves over time. 
- `EnsembleVisualizer` in `visualizer.py` provides an object that creates different plots from an `Ensemble`. 

See the docstrings for more details and the examples for concrete usage patterns.

## License 
This project is licensed under the MIT License. 
See the [LICENSE](LICENSE) file for details.

