import numpy as np
from matplotlib.pyplot import figure, show
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scalation import ScaleUpButton, ScaleDownButton
from rotation import Rotator
from translation import Translator

class Main:
    def __init__(self):
        self.fig, self.ax = self.create_figure()
        self.ax.axis('off')
        self.scale_up_button = ScaleUpButton(self.ax)
        self.scale_down_button = ScaleDownButton(self.ax)
        self.rotator = Rotator(self.ax)
        self.translator = Translator(self.ax)

    def create_figure(self):
        fig = figure()
        ax = fig.add_subplot(111, projection='3d')
        return fig, ax

    def rotation_matrix_3d(self, angle):
        # Convertir el ángulo de grados a radianes
        angle_rad = np.radians(angle)

        # Matriz de rotación en el eje z
        rotation_z = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                           [np.sin(angle_rad), np.cos(angle_rad), 0],
                           [0, 0, 1]])

        return rotation_z

    def draw_prism(self, position):
        # Definir vértices del prisma rectangular
        vertices = np.array(
            [[-0.7, -0.75, -0.5], [.1 - 0.7, -0.75, -0.5], [.1 - 0.7, .25 - 0.75, -0.5], [-0.7, .25 - 0.75, -0.5],
             [-0.7, -0.75, .5], [.1 - 0.7, -0.75, .5], [.1 - 0.7, .25 - 0.75, .5], [-0.7, .25 - 0.75, .5]])

        # Rotar los vértices del prisma 45 grados
        rotation_angle = 45
        rotation_matrix = self.rotation_matrix_3d(rotation_angle)
        vertices_rotated = np.dot(vertices, rotation_matrix.T)

        # Rotar los vértices del prisma 90 grados adicionales
        rotation_angle_2 = 90
        rotation_matrix_2 = self.rotation_matrix_3d(rotation_angle_2)
        vertices_rotated_2 = np.dot(vertices_rotated, rotation_matrix_2.T)

        # Restar 0.5 unidades en las dimensiones X e Y
        vertices_scaled = vertices_rotated_2 - [0.80, 0.1, 0]

        # Ajustar la posición del prisma en Z
        vertices_scaled[:, 2] += position

        # Definir las caras del prisma
        caras = [[0, 1, 2, 3],
                 [4, 5, 6, 7],
                 [0, 1, 5, 4],
                 [2, 3, 7, 6],
                 [1, 2, 6, 5],
                 [0, 3, 7, 4]]

        # Graficar las caras del prisma
        prisma = Poly3DCollection([vertices_scaled[face] for face in caras], alpha=1, linewidths=1, edgecolors='black')
        prisma.set_facecolor('white')
        self.ax.add_collection3d(prisma)

        # Graficar las aristas del prisma
        for k in range(4):
            self.ax.plot3D(*zip(vertices_scaled[caras[k][0]], vertices_scaled[caras[k][1]]), color="black")
            self.ax.plot3D(*zip(vertices_scaled[caras[k][1]], vertices_scaled[caras[k][2]]), color="black")
            self.ax.plot3D(*zip(vertices_scaled[caras[k][2]], vertices_scaled[caras[k][3]]), color="black")
            self.ax.plot3D(*zip(vertices_scaled[caras[k][3]], vertices_scaled[caras[k][0]]), color="black")

    def draw_cylinder_with_spheres(self, position, rotation_angle):
        # Parámetros del cilindro
        r_cilindro = .2  # Radio del cilindro
        h_cilindro = 1  # Altura del cilindro
        resolution = 100  # Resolución

        # Generar los datos para el cilindro
        theta = np.linspace(0, 2*np.pi, resolution)
        z = np.linspace(-h_cilindro/2, h_cilindro/2, resolution)
        theta, z = np.meshgrid(theta, z)
        x = r_cilindro * np.cos(theta)
        y = r_cilindro * np.sin(theta)

        # Aplicar rotación al cilindro
        rotated_x = x * np.cos(np.radians(rotation_angle)) - y * np.sin(np.radians(rotation_angle))
        rotated_y = x * np.sin(np.radians(rotation_angle)) + y * np.cos(np.radians(rotation_angle))

        # Ajustar la posición del cilindro
        rotated_x += position[0]
        rotated_y += position[1]
        z += position[2]

        # Coordenadas de las esferas
        r_esferas = 0.3  # Radio de las esferas
        z_esfera_above = h_cilindro/2 + 0.1  # Posición z de la esfera superior
        z_esfera_below = -h_cilindro/2 - 0.1  # Posición z de la esfera inferior

        # Generar los datos para las esferas
        phi = np.linspace(0, np.pi, resolution//2)
        theta_esferas = np.linspace(0, 2*np.pi, resolution)
        phi, theta_esferas = np.meshgrid(phi, theta_esferas)
        x_esferas = r_esferas * np.sin(phi) * np.cos(theta_esferas) + position[0]
        y_esferas = r_esferas * np.sin(phi) * np.sin(theta_esferas) + position[1]
        z_esferas_above = r_esferas * np.cos(phi) + z_esfera_above + position[2]
        z_esferas_below = -r_esferas * np.cos(phi) + z_esfera_below + position[2]

        # Dibujar el cilindro
        self.ax.plot_surface(rotated_x, rotated_y, z, color='white')

        # Dibujar las esferas
        self.ax.plot_surface(x_esferas, y_esferas, z_esferas_above, color='white')
        self.ax.plot_surface(x_esferas, y_esferas, z_esferas_below, color='white')

    def draw_skull(self):
        # Generar datos de ejemplo para el cráneo
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, np.pi, 100)
        theta, phi = np.meshgrid(theta, phi)
        r = .45  # Radio del cráneo

        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)

        # Graficar el cráneo
        self.ax.plot_surface(x, y, z, color='white')

    def draw_eyes(self):
        # Agregar los ojos
        eye_radius = 0.1  # Radio de las esferas de los ojos
        eye_center_x = .35  # Posición x del centro del ojo
        eye_center_y = -.35  # Posición y del centro del ojo
        eye_center_z = -0.15  # Posición z del centro del ojo

        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 15)
        u, v = np.meshgrid(u, v)
        x_eye = eye_center_x + eye_radius * np.cos(u) * np.sin(v)
        y_eye = eye_center_y + eye_radius * np.sin(u) * np.sin(v)
        z_eye = eye_center_z + eye_radius * np.cos(v)

        # Graficar los ojos
        self.ax.plot_surface(x_eye + .1, y_eye + .1, z_eye + .15, color='black')

        # Agregar el segundo ojo
        eye_center_x2 = -0.5  # Posición x del centro del segundo ojo
        x_eye2 = eye_center_x2 + eye_radius * np.cos(u) * np.sin(v)
        self.ax.plot_surface(x_eye2 + .58, y_eye - 0.2, z_eye + .15, color='black')

    def draw_conical_hat(self):
        # Datos del sombrero cónico
        r_hat = np.linspace(0, 1, 70)
        theta_hat, r_hat = np.meshgrid(np.linspace(0, 2 * np.pi, 50), r_hat)
        x_hat = .50 * np.sqrt(1 - r_hat ** 2) * np.sin(theta_hat)
        y_hat = .50 * np.sqrt(1 - r_hat ** 2) * np.cos(theta_hat)
        z_hat = .7 * r_hat

        # Plot conical hat
        self.ax.plot_surface(x_hat, y_hat, z_hat + .25, color='yellow')

        # Circular base data
        hat_radius = .5
        theta_circle = np.linspace(0, 2 * np.pi, 50)
        x_circle = hat_radius * np.sin(theta_circle)
        y_circle = hat_radius * np.cos(theta_circle)
        z_circle = np.zeros_like(theta_circle)

        # Plot circular base
        self.ax.plot(x_circle, y_circle, z_circle + .25, color='red', linewidth=2 * 5)

    def draw_conical_hat_custom(self):
        # Datos del sombrero cónico
        r_custom = np.linspace(0, 1, 70)
        theta_custom, r_custom = np.meshgrid(np.linspace(0, 2 * np.pi, 50), r_custom)
        x_custom = r_custom * np.cos(theta_custom)
        y_custom = r_custom * np.sin(theta_custom)
        z_custom = -0.1 * r_custom  # Ajustar la coordenada Z para que el sombrero esté debajo del sombrero amarillo

        # Dibujar la superficie del sombrero cónico
        self.ax.plot_surface(x_custom, y_custom, z_custom + .3, color='yellow')  # Cambiar el color a azul para distinguirlo

    def draw(self):
        self.draw_skull()
        self.draw_eyes()
        self.draw_conical_hat()
        self.draw_conical_hat_custom()
        self.draw_prism(0)
        self.draw_prism(-0.1)
        self.draw_cylinder_with_spheres(position=[0, 0, 0], rotation_angle=0)
        
        # Puntos para la primera línea de la 'X'
        x1 = np.array([-0.7, 0.7])
        y1 = np.array([-0.7, 0.7])
        z1 = np.array([1, -1])

        # Puntos para la segunda línea de la 'X'
        x2 = np.array([-0.7, 0.7])
        y2 = np.array([-0.7, 0.7])
        z2 = np.array([-1, 1])

        # Dibujar las líneas para formar la 'X' con líneas más gruesas
        self.ax.plot(x1, y1, z1, color='gray', linewidth=20)
        self.ax.plot(x2, y2, z2, color='gray', linewidth=20)

        # Agregar esferas en cada punto de la primera línea de la 'X'
        self.ax.scatter(x1 - 0.1, y1, z1, color='grey', s=1600)
        # Agregar esferas en cada punto de la segunda línea de la 'X'
        self.ax.scatter(x2 - 0.1, y2, z2, color='grey', s=1600)
        
        self.ax.set_aspect('equal')
        self.ax.set_box_aspect([1, 1, 1])  # Igualar las proporciones de los ejes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        show()

if __name__ == "__main__":
    main = Main()
    main.draw()
