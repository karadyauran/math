import numpy as np
import matplotlib.pyplot as plt

# Координаты дронов
drone_a_coords = np.array([2, 3, 5])
drone_b_coords = np.array([5, 6, 7])
drone_c_coords = np.array([8, 9, 10])

# Векторы скоростей дронов
drone_a_speed = np.array([3, 3, 1])
drone_b_speed = np.array([6, 6, 2])
drone_c_speed = np.array([1, -1, 0])

# Нормализация векторов скоростей
normalized_drone_a_speed = drone_a_speed / np.linalg.norm(drone_a_speed)
normalized_drone_b_speed = drone_b_speed / np.linalg.norm(drone_b_speed)
normalized_drone_c_speed = drone_c_speed / np.linalg.norm(drone_c_speed)

print(normalized_drone_a_speed)

# Создание 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отображение начальных позиций дронов
ax.scatter(drone_a_coords[0], drone_a_coords[1],
           drone_a_coords[2], color='r', label='Drone A')
ax.scatter(drone_b_coords[0], drone_b_coords[1],
           drone_b_coords[2], color='g', label='Drone B')
ax.scatter(drone_c_coords[0], drone_c_coords[1],
           drone_c_coords[2], color='b', label='Drone C')

# Визуализация направлений движения
ax.quiver(drone_a_coords[0], drone_a_coords[1], drone_a_coords[2],
          normalized_drone_a_speed[0], normalized_drone_a_speed[1], normalized_drone_a_speed[2],
          color='r', length=1.0, normalize=True)
ax.quiver(drone_b_coords[0], drone_b_coords[1], drone_b_coords[2],
          normalized_drone_b_speed[0], normalized_drone_b_speed[1], normalized_drone_b_speed[2],
          color='g', length=1.0, normalize=True)
ax.quiver(drone_c_coords[0], drone_c_coords[1], drone_c_coords[2],
          normalized_drone_c_speed[0], normalized_drone_c_speed[1], normalized_drone_c_speed[2],
          color='b', length=1.0, normalize=True)

# Настройка графика
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('Initial Positions and Movement Directions of Drones')

plt.show()
