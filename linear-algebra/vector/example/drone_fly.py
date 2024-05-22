import numpy as np
import matplotlib.pyplot as plt

first_point = np.array([1, 2, 3])
second_point = np.array([-2, 0, 4])
third_point = np.array([3, -1, -2])
fourth_point = np.array([0, 1, 5])


def calculate_last_position(*points):
    last_position = [0, 0, 0]

    for point in points:
        last_position[0] = last_position[0] + point[0]
        last_position[1] = last_position[1] + point[1]
        last_position[2] = last_position[2] + point[2]

    return last_position


def d_visualize(*points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    current_point = [0, 0, 0]
    ax.scatter(current_point[0], current_point[1], current_point[2], color='black', label='Start')

    for point in points:
        next_point = [current_point[0] + point[0], current_point[1] + point[1], current_point[2] + point[2]]

        ax.quiver(current_point[0], current_point[1], current_point[2],
                  point[0], point[1], point[2],
                  length=1.0, normalize=False)

        current_point = next_point

        ax.scatter(current_point[0], current_point[1], current_point[2], color='blue')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Drone Movement Trajectory')

    plt.legend()
    plt.show()


print(calculate_last_position(
    first_point,
    second_point,
    third_point,
    fourth_point
))

d_visualize(
    first_point,
    second_point,
    third_point,
    fourth_point
)
