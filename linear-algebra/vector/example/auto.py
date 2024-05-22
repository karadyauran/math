import numpy as np
from math import sqrt

car_a_cords = np.array([3, 4, 5])
car_b_cords = np.array([1, 2, 3])
car_c_cords = np.array([7, 8, 9])

car_a_direction = np.array([1, 1, 0])
car_b_direction = np.array([2, 2, 0])
car_c_direction = np.array([1, 0, 1])

normalized_car_a_direction = sqrt(
	car_a_direction[0] ** 2 + 
	car_a_direction[1] ** 2 + 
	car_a_direction[2] ** 2
)

normalized_car_b_direction = sqrt(
	car_b_direction[0] ** 2 + 
	car_b_direction[1] ** 2 + 
	car_b_direction[2] ** 2
)

normalized_car_c_direction = sqrt(
	car_c_direction[0] ** 2 + 
	car_c_direction[1] ** 2 + 
	car_c_direction[2] ** 2
)

normalized_car_a_direction = car_a_direction / normalized_car_a_direction
normalized_car_b_direction = car_b_direction / normalized_car_b_direction
normalized_car_c_direction = car_c_direction / normalized_car_c_direction


dot_product_AB = np.dot(normalized_car_a_direction, normalized_car_b_direction)
dot_product_AC = np.dot(normalized_car_a_direction, normalized_car_c_direction)
dot_product_BC = np.dot(normalized_car_b_direction, normalized_car_c_direction)

print(dot_product_AB)
print(dot_product_AC)
print(dot_product_BC)


