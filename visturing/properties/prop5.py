import os

import scipy.io as sio
import matplotlib.pyplot as plt

def load_ground_truth(root_path: str = "../../ground_truth_decalogo", # Path to the root containing all the ground truth files
                      ): # Tuple (x, y1, y2, y3)
    data = sio.loadmat(os.path.join(root_path, "Campbell_Blakemore.mat"))
    data = data["Campbell_Blakemore"]
    x, y1, y2, y3 = data
    return x, y1, y2, y3

def plot_ground_truth(x,
                      y1,
                      y2,
                      y3,
                      ): # Returns both the fig and axes objects
    fig, axes = plt.subplots()
    axes.plot(x, y1, "k", linestyle="-", label="3 cpd")
    axes.plot(x, y2, "k", linestyle=":", label="6 cpd")
    axes.plot(x, y3, "k", linestyle="-.", label="12 cpd")
    axes.set_xlabel("Frequency (cpd)")
    axes.set_xscale("log")
    axes.set_xlim([1,32])
    axes.legend()
    return fig, axes