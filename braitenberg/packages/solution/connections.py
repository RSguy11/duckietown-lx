from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    
    # these are random values

    res[:, 120:319] = 1
    res[:, 320:550] = -1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
   
    res[:, 321:550] = 1
    res[:,150:320] = -1
 
    return res
