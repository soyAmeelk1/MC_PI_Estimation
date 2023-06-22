import numpy as np

def MC_Simulation(total_points, radius):
    circle = 0
    for i in range(total_points):
        x = np.random.uniform(-radius, radius)
        y = np.random.uniform(-radius, radius)
        distance = np.sqrt(y**2 + x**2)
        if distance <= radius:
            circle += 1

    ratio_big_square = circle / total_points
    ratio = 4 * ratio_big_square
    return ratio

# Generate 10 parameters for testing
parameters = []
for _ in range(10):
    total_points = np.random.randint(100000, 1000000)  # Random number of points between 100,000 and 1,000,000
    radius = np.random.uniform(0.1, 1.0)  # Random radius between 0.1 and 1.0
    parameters.append((total_points, radius))

# Test the code with the generated parameters
for i, (total_points, radius) in enumerate(parameters):
    print(f"Test {i+1}:")
    print("Total Points:", total_points)
    print("Radius:", radius)
    result = MC_Simulation(total_points, radius)
    print("Estimated Pi:", result)
    print()
