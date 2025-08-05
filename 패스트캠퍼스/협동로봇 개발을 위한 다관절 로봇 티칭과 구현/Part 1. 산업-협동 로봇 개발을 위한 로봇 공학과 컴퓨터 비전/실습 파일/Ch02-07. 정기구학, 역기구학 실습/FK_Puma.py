import numpy as np

# DH parameters (a, b, alpha, theta) based on the provided table
DH_params = [
    [0, 0, -90, 0],      # Link 1
    [0.432, 0.149, 0, 30],  # Link 2
    [0.02, 0, 90, 10],    # Link 3
    [0, 0.432, -90, 45],  # Link 4
    [0, 0, 90, 90.0002],  # Link 5
    [0, 0.056, 0, 60.0001] # Link 6
]

# Function to create DH transformation matrix
def dh_matrix(a, b, alpha, theta):
    alpha = np.radians(alpha)
    theta = np.radians(theta)
    
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), b],
        [0, 0, 0, 1]
    ])

# Calculate the total transformation matrix by multiplying each link's transformation matrix
T_total = np.eye(4)

for params in DH_params:
    a, b, alpha, theta = params
    T_total = np.dot(T_total, dh_matrix(a, b, alpha, theta))

# Extract the position (translation) from the transformation matrix
position = T_total[:3, 3]

# Extract the rotation matrix from the final transformation matrix (T_total)
R = T_total[:3, :3]

# Function to calculate Euler angles from rotation matrix (ZYX convention)
def rotation_matrix_to_euler_angles(R):
    # Ensure the matrix is a valid rotation matrix
    sy = np.sqrt(R[0, 0]**2 + R[1, 0]**2)

    singular = sy < 1e-6

    if not singular:
        x = np.arctan2(R[2, 1], R[2, 2])
        y = np.arctan2(-R[2, 0], sy)
        z = np.arctan2(R[1, 0], R[0, 0])
    else:
        x = np.arctan2(-R[1, 2], R[1, 1])
        y = np.arctan2(-R[2, 0], sy)
        z = 0

    # Convert to degrees
    return np.degrees(x), np.degrees(y), np.degrees(z)

# Calculate the Euler angles (roll, pitch, yaw)
roll, pitch, yaw = rotation_matrix_to_euler_angles(R)

# Output the results
print("Position (TCP):")
print(f"X: {position[0]:.4f} m, Y: {position[1]:.4f} m, Z: {position[2]:.4f} m")

print("\nOrientation (Euler Angles):")
print(f"Roll: {roll:.4f}°, Pitch: {pitch:.4f}°, Yaw: {yaw:.4f}°")
