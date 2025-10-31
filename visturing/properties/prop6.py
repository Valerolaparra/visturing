import os

import scipy.io as sio
import matplotlib.pyplot as plt

def load_ground_truth(root_path: str = "../../ground_truth_decalogo", # Path to the root containing all the ground truth files
                      ): # Tuple (x, y, y_rg, y_yb)
    data = sio.loadmat(os.path.join(root_path, "responses_no_mask_achrom_1p5_3_6_12_24.mat"))
    data = data["resp_no_mask_achrom"]
    x, y = data[0], data[1:]
    
    data = sio.loadmat(os.path.join(root_path, "responses_no_mask_RG_1p5_3_6_12_24.mat"))
    data = data["resp_no_mask_RG"]
    x, y_rg = data[0], data[1:]
    
    data = sio.loadmat(os.path.join(root_path, "responses_no_mask_YB_1p5_3_6_12_24.mat"))
    data = data["resp_no_mask_YB"]
    x, y_yb = data[0], data[1:]
    
    return x, y, y_rg, y_yb

def plot_ground_truth(x,
                      y,
                      y_rg,
                      y_yb,
                      figsize=(14,4),
                      ): # Returns both the fig and axes objects
    freqs = [1.5, 3, 6, 12, 24]
    colors = ["lightgray", "black", "blue", "gray", "red"]
    colors_rg = ["blue", "black", "gray", "lightgray", "red"]
    colors_yb = ["blue", "black", "gray", "lightgray", "red"]

    fig, axes = plt.subplots(1,3, figsize=figsize, sharex=True, sharey=True)
    for y_, f, c in zip(y, freqs, colors):
        axes[0].plot(x, y_, color=c, label=f"Freq {f}")
    for y_, f, c in zip(y_rg, freqs, colors_rg):
        axes[1].plot(x, y_, color=c, label=f"Freq {f}")
    for y_, f, c in zip(y_yb, freqs, colors_yb):
        axes[2].plot(x, y_, color=c, label=f"Freq {f}")
    axes[0].set_ylabel("Visibility")
    for ax in axes.ravel():
        ax.set_xlabel("Contrast")
        ax.legend()
    return fig, axes
    