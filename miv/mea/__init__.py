import numpy as np

from miv.mea.grid import *

mea_map = {
    "64_upper_half_intanRHD_stim": np.array(
        [
            [-1, 2, 4, 6, 23, 20, 18],
            [10, 9, 3, 5, 24, 19, -1],
            [12, 11, 1, 7, 22, -1, -1],
            [15, 14, 13, 8, 21, -1, -1],
            [-1, 25, 26, -1, -1, -1, -1],
            [27, 28, 31, -1, -1, -1, -1],
            [29, 30, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1],
        ],
        dtype=np.int_,
    )
    - 1,
    "64_intanRHD": np.array(
        [
            [-1, 10, 12, 14, 31, 28, 26, -1],
            [18, 17, 11, 13, 32, 27, 38, 37],
            [20, 19, 9, 15, 30, 39, 36, 35],
            [23, 22, 21, 16, 29, 34, 33, 56],
            [-1, 1, 2, 61, 44, 53, 54, 55],
            [3, 4, 7, 62, 43, 48, 51, 52],
            [5, 6, 59, 64, 41, 46, 49, 50],
            [-1, 58, 60, 63, 42, 45, 47, -1],
        ],
        dtype=np.int_,
    )
    - 1,
    "128_first_32": np.array(
        [
            [10, 23, 9, 24],
            [12, 21, 11, 22],
            [14, 19, 13, 20],
            [16, 17, 15, 18],
            [8, 25, 7, 26],
            [6, 27, 5, 28],
            [4, 29, 3, 30],
            [2, 31, 1, 32],
        ],
        dtype=np.int_,
    )
    - 1,
}
