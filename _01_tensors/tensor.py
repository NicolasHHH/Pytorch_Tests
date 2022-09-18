import torch
import numpy as np

# declare from list
t1 = torch.Tensor([[1,2,3],[1,2,3]])

# declare from numpy array
array1 = np.arange(12).reshape(3,4)
t2 = torch.Tensor(array1)


def main():
    print(t1, t1.shape)
    print(t2, t2.shape)


if __name__ == '__main__':
    main()
