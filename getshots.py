from scipy.interpolate import interp1d
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np
import csv

x = []


def shot_loc(id):

    with open('shotdist/{}.csv'.format(id)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(int(float(row['dist'])))

    ecdf = ECDF(x)
    inv_cdf = interp1d(ecdf.y, ecdf.x, bounds_error=False, assume_sorted=True)
    r = np.random.uniform(0, 1, 1000)
    ys = inv_cdf(r)
    ys = ys[~np.isnan(ys)]
    return ys