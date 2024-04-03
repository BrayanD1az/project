import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_conical_hat(ax):
    # Conical hat data
    r_hat = np.linspace(0, 1, 100)
    theta_hat, r_hat = np.meshgrid(np.linspace(0, 2*np.pi, 50), r_hat)
    x_hat = .50 * np.sqrt(1 - r_hat**2) * np.sin(theta_hat)
    y_hat = .50 * np.sqrt(1 - r_hat**2) * np.cos(theta_hat)
    z_hat = .5 * r_hat

    # Plot conical hat
    ax.plot_surface(x_hat, y_hat, z_hat, color='yellow')

    # Circular base data
    hat_radius = .5
    theta_circle = np.linspace(0, 2*np.pi, 50)
    x_circle = hat_radius * np.sin(theta_circle)
    y_circle = hat_radius * np.cos(theta_circle)
    z_circle = np.zeros_like(theta_circle)

    # Plot circular base
    ax.plot(x_circle, y_circle, z_circle, color='red', linewidth=2*4)

def main():
    # Create figure and 3D axes object
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw conical hat and circular base
    draw_conical_hat(ax)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
