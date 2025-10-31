import os

import scipy.io as sio
import matplotlib.pyplot as plt

def load_ground_truth(root_path: str = "../../ground_truth_decalogo", # Path to the root containing all the ground truth files
                      ): # Tuple (x, y, red-green, yellow-blue)
    data = sio.loadmat(os.path.join(root_path, "responses_CSF_achrom.mat"))
    data = data["CSF_achrom"]
    x, y = data
    data = sio.loadmat(os.path.join(root_path, "responses_CSF_RG.mat"))
    data = data["CSF_RG"]
    _, rg = data
    data = sio.loadmat(os.path.join(root_path, "responses_CSF_YB.mat"))
    data = data["CSF_YB"]
    _, yb = data
    return x, y, rg, yb

def plot_ground_truth(x,
                      y,
                      rg,
                      yb,
                      ): # Returns both the fig and axes objects
    fig, axes = plt.subplots()
    axes.plot(x, y, "k", label="Achromatic")
    axes.plot(x, rg, "r", label="Red-Green")
    axes.plot(x, yb, "b", label="Yellow-Blue")
    axes.set_xscale("log")
    axes.set_yscale("log")
    axes.set_xlim([1,32])
    axes.set_ylim(bottom=0.3)
    axes.legend()
    axes.set_xlabel("Frequency (cpd)")
    axes.set_ylabel("Sensitivity")
    return fig, axes