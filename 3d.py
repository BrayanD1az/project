import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scalation import Scaler

class Main:
    def __init__(self):
        self.fig, self.ax = self._create_figure()
        self.scaler = Scaler(self.ax)

    def _create_figure(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Dibujar elementos en la escena
        self._draw_scene(ax)

        # Configurar la apariencia de la figura
        self._configure_axes(ax)

        return fig, ax

    def _draw_scene(self, ax):
        # Dibujar cilindros con esferas
        self._draw_cylinder_with_spheres(ax, (0, 0, 0), 0)
        self._draw_cylinder_with_spheres(ax, (-0.9, 0.6, 0), 0)
        self._draw_cylinder_with_spheres(ax, (-0.3, 1, 0), 0)

        # Dibujar cráneo y ojos
        self._draw_skull(ax)
        self._draw_eyes(ax)

        # Dibujar sombreros
        self._draw_conical_hat(ax)
        self._draw_conical_hat_custom(ax)

        # Dibujar prismas
        self._draw_prism(ax, 0)
        self._draw_prism(ax, -0.1)

    def _configure_axes(self, ax):
        ax.set_aspect('equal')
        ax.set_box_aspect([1, 1, 1])  # Igualar las proporciones de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    def rotation_matrix_3d(self, angle):
        angle_rad = np.radians(angle)
        rotation_z = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                            [np.sin(angle_rad), np.cos(angle_rad), 0],
                            [0, 0, 1]])
        return rotation_z

    def _draw_cylinder_with_spheres(self, ax, position, rotation_angle):
        r_cilindro = .2
        h_cilindro = 1
        resolution = 100

        theta = np.linspace(0, 2*np.pi, resolution)
        z = np.linspace(-h_cilindro/2, h_cilindro/2, resolution)
        theta, z = np.meshgrid(theta, z)
        x = r_cilindro * np.cos(theta)
        y = r_cilindro * np.sin(theta)

        rotated_x = x * np.cos(np.radians(rotation_angle)) - y * np.sin(np.radians(rotation_angle))
        rotated_y = x * np.sin(np.radians(rotation_angle)) + y * np.cos(np.radians(rotation_angle))

        rotated_x += position[0]
        rotated_y += position[1]
        z += position[2]

        r_esferas = 0.3
        z_esfera_above = h_cilindro/2 + 0.1
        z_esfera_below = -h_cilindro/2 - 0.1

        phi = np.linspace(0, np.pi, resolution//2)
        theta_esferas = np.linspace(0, 2*np.pi, resolution)
        phi, theta_esferas = np.meshgrid(phi, theta_esferas)
        x_esferas = r_esferas * np.sin(phi) * np.cos(theta_esferas) + position[0]
        y_esferas = r_esferas * np.sin(phi) * np.sin(theta_esferas) + position[1]
        z_esferas_above = r_esferas * np.cos(phi) + z_esfera_above + position[2]
        z_esferas_below = -r_esferas * np.cos(phi) + z_esfera_below + position[2]

        ax.plot_surface(rotated_x, rotated_y, z, color='white')
        ax.plot_surface(x_esferas, y_esferas, z_esferas_above, color='white')
        ax.plot_surface(x_esferas, y_esferas, z_esferas_below, color='white')

    def _draw_prism(self, ax, position):
        vertices = np.array([[-0.7, -0.75, -0.5], [.1-0.7, -0.75, -0.5], [.1-0.7, .25-0.75, -0.5], [-0.7, .25-0.75, -0.5],
                            [-0.7, -0.75, .5], [.1-0.7, -0.75, .5], [.1-0.7, .25-0.75, .5], [-0.7, .25-0.75, .5]])

        rotation_angle = 45
        rotation_matrix = self.rotation_matrix_3d(rotation_angle)
        vertices_rotated = np.dot(vertices, rotation_matrix.T)

        rotation_angle_2 = 90
        rotation_matrix_2 = self.rotation_matrix_3d(rotation_angle_2)
        vertices_rotated_2 = np.dot(vertices_rotated, rotation_matrix_2.T)

        vertices_scaled = vertices_rotated_2 - [0.80, 0.1, 0]
        vertices_scaled[:, 2] += position

        caras = [[0, 1, 2, 3],
                [4, 5, 6, 7],
                [0, 1, 5, 4],
                [2, 3, 7, 6],
                [1, 2, 6, 5],
                [0, 3, 7, 4]]

        prisma = Poly3DCollection([vertices_scaled[face] for face in caras], alpha=1, linewidths=1, edgecolors='black')
        prisma.set_facecolor('white')
        ax.add_collection3d(prisma)

        for k in range(4):
            ax.plot3D(*zip(vertices_scaled[caras[k][0]], vertices_scaled[caras[k][1]]), color="black")
            ax.plot3D(*zip(vertices_scaled[caras[k][1]], vertices_scaled[caras[k][2]]), color="black")
            ax.plot3D(*zip(vertices_scaled[caras[k][2]], vertices_scaled[caras[k][3]]), color="black")
            ax.plot3D(*zip(vertices_scaled[caras[k][3]], vertices_scaled[caras[k][0]]), color="black")

    def _draw_skull(self, ax):
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, np.pi, 100)
        theta, phi = np.meshgrid(theta, phi)
        r = .45

        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)

        ax.plot_surface(x, y, z, color='white')

    def _draw_eyes(self, ax):
        eye_radius = 0.1
        eye_center_x = .35
        eye_center_y = -.35
        eye_center_z = -0.15

        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 15)
        u, v = np.meshgrid(u, v)
        x_eye = eye_center_x + eye_radius * np.cos(u) * np.sin(v)
        y_eye = eye_center_y + eye_radius * np.sin(u) * np.sin(v)
        z_eye = eye_center_z + eye_radius * np.cos(v)

        ax.plot_surface(x_eye+.1, y_eye+.1, z_eye+.15, color='black')

        eye_center_x2 = -0.5
        x_eye2 = eye_center_x2 + eye_radius * np.cos(u) * np.sin(v)
        ax.plot_surface(x_eye2+.58, y_eye-0.2, z_eye+.15, color='black')

    def _draw_conical_hat(self, ax):
        r_hat = np.linspace(0, 1, 70)
        theta_hat, r_hat = np.meshgrid(np.linspace(0, 2*np.pi, 50), r_hat)
        x_hat = .50 * np.sqrt(1 - r_hat**2) * np.sin(theta_hat)
        y_hat = .50 * np.sqrt(1 - r_hat**2) * np.cos(theta_hat)
        z_hat = .7 * r_hat

        ax.plot_surface(x_hat, y_hat, z_hat+.25, color='yellow')

        hat_radius = .5
        theta_circle = np.linspace(0, 2*np.pi, 50)
        x_circle = hat_radius * np.sin(theta_circle)
        y_circle = hat_radius * np.cos(theta_circle)
        z_circle = np.zeros_like(theta_circle)

        ax.plot(x_circle, y_circle, z_circle+.25, color='red', linewidth=2*5)

    def _draw_conical_hat_custom(self, ax):
        r_custom = np.linspace(0, 1, 70)
        theta_custom, r_custom = np.meshgrid(np.linspace(0, 2*np.pi, 50), r_custom)
        x_custom = r_custom * np.cos(theta_custom)
        y_custom = r_custom * np.sin(theta_custom)
        z_custom = -0.1 * r_custom

        ax.plot_surface(x_custom, y_custom, z_custom+.3, color='yellow')

    def show_figure(self):
        plt.show()

if __name__ == "__main__":
    main = Main()
    main.show_figure()
