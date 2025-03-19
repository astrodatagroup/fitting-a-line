import pathlib

import astropy.table as at
import numpy as np


def main(n_data):
    data_path = pathlib.Path(__file__).parent

    rng = np.random.default_rng(seed=42)

    x = rng.uniform(-1, 10, 1024)

    true_pars = rng.uniform(-10, 10, size=2)
    y = true_pars[0] + true_pars[1] * x
    y_err = np.exp(rng.uniform(np.log(0.1), np.log(10), size=n_data))
    y = rng.normal(y, y_err)

    tbl = at.Table({"x": x, "y": y, "y_err": y_err})
    tbl.meta["true_pars"] = list(true_pars)
    tbl.write(data_path / f"heteroskedastic-{n_data}.ecsv", overwrite=True)


if __name__ == "__main__":
    main(n_data=1024)
