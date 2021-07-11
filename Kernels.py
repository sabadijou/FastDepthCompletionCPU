import numpy as np

class kernel():

    FULL_KERNEL_3 = np.ones((3, 3), np.uint8)
    FULL_KERNEL_5 = np.ones((5, 5), np.uint8)
    FULL_KERNEL_7 = np.ones((7, 7), np.uint8)
    FULL_KERNEL_9 = np.ones((9, 9), np.uint8)
    FULL_KERNEL_31 = np.ones((31, 31), np.uint8)

    def cross_kernel_3(self):
        self.CROSS_KERNEL_3 = np.asarray(
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0],
            ], dtype=np.uint8)
        return self.CROSS_KERNEL_3


    def cross_kernel_5(self):
        self.CROSS_KERNEL_5 = np.asarray(
            [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ], dtype=np.uint8)
        return self.CROSS_KERNEL_5

    def diamond_kernel_5(self):
        self.DIAMOND_KERNEL_5 = np.array(
            [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
            ], dtype=np.uint8)
        return self.DIAMOND_KERNEL_5

    def cross_kernel_7(self):
        self.CROSS_KERNEL_7 = np.asarray(
            [
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
            ], dtype=np.uint8)
        return self.CROSS_KERNEL_7

    def diamond_kernel_7(self):
        self.DIAMOND_KERNEL_7 = np.asarray(
            [
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
            ], dtype=np.uint8)
        return self.DIAMOND_KERNEL_7



