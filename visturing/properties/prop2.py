import os

import scipy.io as sio
import matplotlib.pyplot as plt

def load_ground_truth(root_path: str = "../../ground_truth_decalogo", # Path to the root containing all the ground truth files
                      ): # Tuple of tuples (x, y), (x_c, red-green), (x_c, yellow-blue)
    data = sio.loadmat(os.path.join(root_path, "weber.mat"))
    data = data["weber"]

    x = data[0]
    y = data[1]

    data = sio.loadmat(os.path.join(root_path, "resp_RG.mat"))
    data = data["resp_RG"]
    x_c, rg, _ = data

    data = sio.loadmat(os.path.join(root_path, "resp_YB.mat"))
    data = data["resp_YB"]
    _, yb = data
    return x, y, x_c, rg, x_c, yb

def plot_ground_truth(x,y,
                      x_c, rg,
                      x_cc, yb,
                      ): # Returns both the fig and axes objects
    fig, axes = plt.subplots(1,3, figsize=(18,5))
    axes[0].plot(x, y, "b")
    axes[1].plot(x_c, rg, "gray")
    axes[2].plot(x_c, yb, "gray")
    for ax, name in zip(axes, ["Achromatic", "Red-Green", "Yellow-Blue"]): ax.set_title(name)
    axes[0].set_xlabel(r"Luminance (cd/m$^2$)")
    axes[1].set_xlabel("Linear RG")
    axes[2].set_xlabel("Linear YB")
    for ax, name in zip(axes, ["Brightness", "Nonlinear RG", "Nonlinear YB"]): ax.set_ylabel(name)
    axes[1].set_xlim([-22,22])
    axes[1].set_ylim([-8,8])
    axes[2].set_xlim([-22,22])
    axes[2].set_ylim([-8,8])
    return fig, axes