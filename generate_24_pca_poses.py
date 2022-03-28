import numpy as np
import itertools




def generate_24_poses(pcd):
    """
    @param pcd: N*3 point cloud
    @return: a list of the 24 poses
    """
    ## get principle axes
    _, eig_vecs = np.linalg.eigh(pcd.T @ pcd)
    if np.linalg.det(eig_vecs) < 0:
        eig_vecs[:, 2] = -1.0 * eig_vecs[:, 2]
    e1, e2, e3 = eig_vecs[:, 0], eig_vecs[:, 1], eig_vecs[:, 2]

    ## get all 48 possible combos, among them, 
    ## 24 are with det 1 (rotations), and the other 24 are with det -1 (improper rotations)
    all_R = list(itertools.permutations([e1, e2, e3])) + list(itertools.permutations([-e1, -e2, -e3])) + \
             list(itertools.permutations([-e1, e2, e3])) + list(itertools.permutations([e1, -e2, e3])) + \
             list(itertools.permutations([e1, e2, -e3])) + list(itertools.permutations([-e1, -e2, e3])) + \
             list(itertools.permutations([-e1, e2, -e3])) + list(itertools.permutations([e1, -e2, -e3]))
    all_R = [np.array(x) for x in all_R]

    ## remove improper rotations, the left are the 24 ambiguities
    all_R = [x for x in all_R if np.linalg.det(x) > 0]

    res = [pcd @ R for R in all_R]
    return res




##---------------------------------------------------------------------------



if __name__ == '__main__':

   
    pcd = np.random.rand(1024, 3)
    res = generate_24_poses(pcd)

