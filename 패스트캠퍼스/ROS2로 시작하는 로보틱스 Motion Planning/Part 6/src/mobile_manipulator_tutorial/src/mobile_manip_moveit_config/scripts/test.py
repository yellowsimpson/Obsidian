import numpy as np
from tf_transformations import quaternion_from_euler, quaternion_multiply, quaternion_conjugate, quaternion_matrix

def compute_robot_to_object(T_wo_trans, T_wo_quat, T_wr_trans, T_wr_quat):
    """
    Compute T_ro (robot -> object) given T_wo (world -> object) and T_wr (world -> robot).
    
    Args:
        T_wo_trans: Translation vector (x, y, z) from world to object
        T_wo_quat: Quaternion (x, y, z, w) from world to object (90° Z rotation)
        T_wr_trans: Translation vector (x, y, z) from world to robot (from simulation)
        T_wr_quat: Quaternion (x, y, z, w) from world to robot (from simulation)
    
    Returns:
        T_ro_trans: Translation vector (x, y, z) from robot to object
        T_ro_quat: Quaternion (x, y, z, w) from robot to object
    """
    # Convert inputs to numpy arrays
    t_wo = np.array(T_wo_trans)  # World -> Object translation
    q_wo = np.array(T_wo_quat)   # World -> Object quaternion
    t_wr = np.array(T_wr_trans)  # World -> Robot translation
    q_wr = np.array(T_wr_quat)   # World -> Robot quaternion

    # Step 1: Compute T_wr inverse
    # Inverse quaternion (conjugate)
    q_wr_inv = quaternion_conjugate(q_wr)  # [qx, qy, qz, qw] -> [-qx, -qy, -qz, qw]
    
    # Inverse translation: Rotate -t_wr by q_wr_inv
    rot_wr = quaternion_matrix(q_wr)[:3, :3]  # Rotation matrix from q_wr
    t_wr_inv = -np.dot(rot_wr.T, t_wr)  # Inverse translation in world frame (rot^T * -t)

    # Step 2: Compute T_ro = T_wr^{-1} * T_wo
    # Orientation: q_ro = q_wr_inv * q_wo
    q_ro = quaternion_multiply(q_wr_inv, q_wo)

    # Translation: t_ro = t_wr_inv + R(q_wr_inv) * t_wo
    rot_wr_inv = quaternion_matrix(q_wr_inv)[:3, :3]  # Rotation matrix from q_wr_inv
    t_ro = t_wr_inv + np.dot(rot_wr_inv, t_wo)

    return list(t_ro), list(q_ro)

# Example usage
# T_wo: World -> Object (90° rotation around Z-axis, assume some translation)
T_wo_trans = [1.0, 2.0, 0.0]  # Example translation
T_wo_quat = quaternion_from_euler(0, 0, np.pi/2)  # 90° around Z = [0, 0, 0.707, 0.707]

# T_wr: World -> Robot (from simulation, example values)
T_wr_trans = [0.5, 1.0, 0.0]  # Example translation
T_wr_quat = [0.0, 0.0, 0.0, 1.0]  # No rotation (identity quaternion)

# Compute T_ro
T_ro_trans, T_ro_quat = compute_robot_to_object(T_wo_trans, T_wo_quat, T_wr_trans, T_wr_quat)

print(f"T_ro translation: {T_ro_trans}")
print(f"T_ro quaternion: {T_ro_quat}")