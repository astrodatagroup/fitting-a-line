# Fitting a line to data

A collection of recipes for how to fit a line to data with different methods and
software tools.

## Recipes:

| Summary | Method / approach | Software | Link |
|---------|-------------------|----------|------|
| Direct linear algebra | least squares, maximum likelihood | Python, numpy | [link](https://github.com/astrodatagroup/fitting-a-line/blob/main/recipes/least-squares.ipynb) |
| Least squares optimization | least squares, maximum likelihood, optimization | Python, numpy, scipy | TBD |
| Underestimated uncertainties | maximum likelihood, optimization | Python, numpy, scipy | TBD |
| Unknown uncertainties per object | TBD | TBD | TBD |
| Outliers | TBD | TBD | TBD |
| Two populations | TBD | TBD | TBD |
| Uncertainty in x and y | TBD | TBD | TBD |
| Non-Gaussian / asymmetric uncertainty | TBD | TBD | TBD |
| Upper/lower limits | TBD | TBD | TBD |
| Missing data | TBD | TBD | TBD |
| How to tell if a line is a bad model | TBD | TBD | TBD |
| Orthogonal fits (2d) | TBD | TBD | TBD |
| Variational inference | TBD | TBD | TBD |
| Simulation based inference / likelihood-free inference | TBD | TBD | TBD |

Feel free to contribute ideas for new recipes to this list, or to contribute recipes for
any of the ideas listed in this table!


## Set up to contribute

Install the dependencies:

```bash
uv venv
uv sync
pre-commit install
```
