from numpy import dot, diag, cos, sin
from matplotlib.pyplot import axes, draw
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from numpy import dot, diag, radians

class Rotator:
    def __init__(self, ax):
        self.ax = ax
        self.rotate_button = self._create_rotate_button()

    def _create_rotate_button(self):
        ax_button = plt.axes([0.1, 0.01, 0.1, 0.05])
        button = Button(ax_button, 'Rotate')
        button.on_clicked(lambda event: self._rotate_figure())
        return button

    def _rotate_figure(self):
        angle_deg = 80
        angle_rad = radians(angle_deg)
        rotation_matrix = dot(Axes3D.get_proj(self.ax), diag([1, 1, 1, 1]))  # No rotation initially
        rotation_matrix = dot(rotation_matrix, [[1, 0, 0, 0], [0, cos(angle_rad), -sin(angle_rad), 0], [0, sin(angle_rad), cos(angle_rad), 0], [0, 0, 0, 1]])
        self.ax.get_proj = lambda: rotation_matrix
        plt.draw()


