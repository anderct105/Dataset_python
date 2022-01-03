import pandas as pd
import numpy as np
from datetime import date

from dataset.plotting import roc_plot


def roc(d):
    """Computes the roc curve from a given d DataFrame. The first column of the database must be a list or number,
    commonly, a list of probabilities. The second column must be the class of the data. As a result, TPRs and FPRs
    will be calculated."""
    d = d.sort_values(d.columns[0])
    tprs = []
    fprs = []
    thresholds = sorted(list(set([x for x in d.iloc[:, 0]])))
    for t in thresholds:
        res = np.array(list(map(lambda x: x >= t, d.iloc[:, 0]))).astype(int)
        c = np.array(d.iloc[:, 1]).astype(int)
        tp = sum(res * c)
        tn = sum(not_v(res) * not_v(c))
        fp = sum(res * not_v(c))
        fn = sum(not_v(res) * c)
        tprs.append(tp / (tp + fn))
        fprs.append(fp / (fp + tn))
    roc_plot(tprs, fprs)


def not_v(v):
    """Computes the not of a binary vector, replacing 1's by 0's and viceversa"""
    a = np.array(v)
    res = 1 - a
    return res


def read_csv(path):
    """Reads a .csv file from a given path and returns a DataFrame containing all the data"""
    df = pd.read_csv(path, sep=",")
    return df


def create_log(path):
    """Creates a log file in the specified path"""
    with open(path, 'w') as f:
        f.close()


def write_log(path, message):
    """Adds a message into the log file in path"""
    with open(path, 'a') as f:
        today = date.today()
        f.write("\n" + str(today) + " - " + message)
        f.close()