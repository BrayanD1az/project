from matplotlib.pyplot import axes, draw
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
from numpy import dot, diag, cos, sin, radians

class Rotator:
    def __init__(self, ax):
        self.ax = ax
        self.angle_deg = 0  # Inicializamos el ángulo en 0
        self.rotate_button = self._create_rotate_button()

    def _create_rotate_button(self):
        ax_button = axes([0.8, 0.9, 0.1, 0.05])
        button = Button(ax_button, 'Rotar')
        button.on_clicked(lambda event: self._rotate_figure())
        return button

    def _rotate_figure(self):
        print("Rotando figura")
        self.angle_deg += 80  # Incrementamos el ángulo en 80 grados cada vez que se toca el botón
        angle_rad = radians(self.angle_deg)
        rotation_matrix = dot(Axes3D.get_proj(self.ax), diag([1, 1, 1, 1]))  # No rotation initially
        rotation_matrix = dot(rotation_matrix, [[1, 0, 0, 0], [0, cos(angle_rad), -sin(angle_rad), 0], [0, sin(angle_rad), cos(angle_rad), 0], [0, 0, 0, 1]])
        self.ax.get_proj = lambda: rotation_matrix
        draw()
