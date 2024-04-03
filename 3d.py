import numpy as np
import matplotlib.pyplot as plt
from scalation import Scaler

class Main:
    def __init__(self):
        self.fig, self.ax = self._create_figure()
        self.Scaler = Scaler(self.ax)

    def _create_figure(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        self._draw_conical_hat(ax)
        return fig, ax

    def _draw_conical_hat(self, ax):
        r_hat = np.linspace(0, 1, 100)
        theta_hat, r_hat = np.meshgrid(np.linspace(0, 2*np.pi, 50), r_hat)
        x_hat = .50 * np.sqrt(1 - r_hat**2) * np.sin(theta_hat)
        y_hat = .50 * np.sqrt(1 - r_hat**2) * np.cos(theta_hat)
        z_hat = .5 * r_hat

        ax.plot_surface(x_hat, y_hat, z_hat, color='yellow')

        hat_radius = .5
        theta_circle = np.linspace(0, 2*np.pi, 50)
        x_circle = hat_radius * np.sin(theta_circle)
        y_circle = hat_radius * np.cos(theta_circle)
        z_circle = np.zeros_like(theta_circle)

        ax.plot(x_circle, y_circle, z_circle, color='red', linewidth=2*4)

    def show_figure(self):
        plt.show()


if __name__ == "__main__":
    main = Main()
    main.show_figure()