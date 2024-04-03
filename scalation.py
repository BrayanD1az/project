from numpy import dot, diag
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

class EscaladorFigura3D:
    def __init__(self, ax):
        self.ax = ax
        self.slider = self._create_scale_slider()

    def _create_scale_slider(self):
        ax_slider = plt.axes([0.1, 0.01, 0.8, 0.03])
        slider = Slider(ax_slider, 'Escala', 0.1, 2.0, valinit=1.0)
        slider.on_changed(lambda val: self._on_slider_change(val))
        return slider

    def _on_slider_change(self, val):
        escala = self.slider.val
        self.ax.get_proj = lambda: dot(Axes3D.get_proj(self.ax), diag([escala, escala, escala, 1]))
        plt.draw()