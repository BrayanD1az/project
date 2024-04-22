from matplotlib.pyplot import axes, draw
from matplotlib.widgets import Button

class ScaleDownButton:
    def __init__(self, ax, scale_factor=1.1):
        self.ax = ax
        self.scale_factor = scale_factor
        self.button = self._create_button('Escalar -', self._scale_down)

    def _create_button(self, label, callback):
        ax_button = axes([0.1, 0.1, 0.1, 0.05])
        button = Button(ax_button, label)
        button.on_clicked(callback)
        return button

    def _scale_down(self, event):
        print("Reduciendo escala")
        self._scale_figure(self.scale_factor)

    def _scale_figure(self, factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        new_xlim = (xlim[0] - (factor - 1) * (xlim[1] - xlim[0]) / 2, xlim[1] + (factor - 1) * (xlim[1] - xlim[0]) / 2)
        new_ylim = (ylim[0] - (factor - 1) * (ylim[1] - ylim[0]) / 2, ylim[1] + (factor - 1) * (ylim[1] - ylim[0]) / 2)
        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        draw()


class ScaleUpButton:
    def __init__(self, ax, scale_factor=1.1):
        self.ax = ax
        self.scale_factor = scale_factor
        self.button = self._create_button('Escalar +', self._scale_up)

    def _create_button(self, label, callback):
        ax_button = axes([0.1, 0.2, 0.1, 0.05])  # Cambiar la posición en y para separar los botones
        button = Button(ax_button, label)
        button.on_clicked(callback)
        return button

    def _scale_up(self, event):
        print("Aumentando escala")
        self._scale_figure(1 / self.scale_factor)

    def _scale_figure(self, factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        new_xlim = (xlim[0] - (factor - 1) * (xlim[1] - xlim[0]) / 2, xlim[1] + (factor - 1) * (xlim[1] - xlim[0]) / 2)
        new_ylim = (ylim[0] - (factor - 1) * (ylim[1] - ylim[0]) / 2, ylim[1] + (factor - 1) * (ylim[1] - ylim[0]) / 2)
        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        draw()
