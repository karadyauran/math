import numpy as np

record_1 = np.array([3, 4])
record_2 = np.array([1, 2])
record_3 = np.array([5, 12])


def count(*records):
    total = 0
    for record in records:
        distance = np.linalg.norm(record)
        total += distance

    return total


print(count(record_1, record_2, record_3))
