from matplotlib.pyplot import axes, draw
from matplotlib.widgets import Button

class Translator:
    def __init__(self, ax):
        self.ax = ax
        self.translate_button = self._create_translate_button()
        self.translation_amount = 0.1  # Cantidad de traslación en cada eje

    def _create_translate_button(self):
        ax_button = axes([0.1, 0.9, 0.1, 0.05])
        button = Button(ax_button, 'Trasladar')
        button.on_clicked(lambda event: self._translate_figure())
        return button

    def _translate_figure(self):
        print("Trasladando figura")
        xlim = self.ax.get_xlim3d()
        ylim = self.ax.get_ylim3d()
        zlim = self.ax.get_zlim3d()

        new_xlim = (xlim[0] + self.translation_amount, xlim[1] + self.translation_amount)
        new_ylim = (ylim[0] + self.translation_amount, ylim[1] + self.translation_amount)
        new_zlim = (zlim[0] + self.translation_amount, zlim[1] + self.translation_amount)

        self.ax.set_xlim3d(new_xlim)  # Traslación en eje x
        self.ax.set_ylim3d(new_ylim)  # Traslación en eje y
        self.ax.set_zlim3d(new_zlim)  # Traslación en eje z

        draw()
