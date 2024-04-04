from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from numpy import dot, diag, radians

class Translator:
    def __init__(self, ax):
        self.ax = ax
        self.translate_button = self._create_translate_button()
        self.translation_vector = [0, 0, 0]  # Inicialmente sin traslación

    def _create_translate_button(self):
        ax_button = plt.axes([0.1, 0.01, 0.1, 0.05])
        button = Button(ax_button, 'Translate')
        button.on_clicked(lambda event: self._translate_figure())
        return button

    def _translate_figure(self):
        translation_amount = 0.1  # Cantidad de traslación en cada eje
        self.translation_vector[0] += translation_amount
        self.translation_vector[1] += translation_amount
        self.translation_vector[2] += translation_amount

        translation_matrix = dot(Axes3D.get_proj(self.ax), diag([1, 1, 1, 1]))  # No translation initially
        translation_matrix[0:3, 3] = self.translation_vector

        self.ax.get_proj = lambda: translation_matrix
        plt.draw()
