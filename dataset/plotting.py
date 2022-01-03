import math

import seaborn as sns
from scipy.stats import entropy

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def roc_plot(tprs, fprs):
    """Plots the roc curve, given the TPRs and FPRs computed with the roc function"""
    plt.close()
    plt.plot(fprs, tprs)
    plt.ylabel("TPR")
    plt.xlabel("FPR")
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.show()

