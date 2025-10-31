import os

import scipy.io as sio
import matplotlib.pyplot as plt

def load_ground_truth(root_path: str = "../../ground_truth_decalogo", # Path to the root containing all the ground truth files
                      ): # Tuple (x, achromatic, red-green, yellow-blue)
    data = sio.loadmat(os.path.join(root_path, "spectral_sensitivities.mat"))
    data = data["spectral_sensitivities"]

    x = data[0]
    a = data[1]
    rg = data[2]
    yb = data[3]

    return (x, a, rg, yb)


def plot_ground_truth(x,
                      a,
                      rg,
                      yb,
                      ): # Returns both the fig and axes objects
    fig, axes = plt.subplots(1,2, sharex=True, sharey=False, figsize=(10,4))
    axes[0].plot(x, a, "k", label="Achromatic")

    axes[0].set_xlim([380, 720])
    axes[0].set_ylim([0, 1.1])
    axes[0].legend()

    axes[1].plot(x, rg, "r", label="Red-Green")
    axes[1].plot(x, yb, "b", label="Yellow-Blue")
    axes[1].set_xlim([380, 720])
    axes[1].set_ylim([-0.7, 0.7])

    axes[1].legend()

    axes[0].set_xlabel(r"Wavelength ($\lambda$)")
    axes[0].set_ylabel("Visibility")
    axes[1].set_xlabel(r"Wavelength ($\lambda$)")

    return fig, axes