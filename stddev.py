import numpy as np

dataset = [
    [37, 50, 50, 49, 47, 45, 43, 44, 43],
    [36, 32, 26, 26, 25, 23, 22, 21, 39, 48, 39, 39, 38, 38, 50, 40, 35, 36, 37, 39, 45],
    [60, 70, 74, 77, 56, 61, 67, 67, 67, 67, 60, 68, 66, 72, 72, 75]
]

if __name__ == "__main__":
    for i in range(len(dataset)):
        nparr = np.array(dataset[i])
        mean = np.mean(nparr)
        stddev = np.std(nparr)
        print("mean: ", mean)
        print("stddev: ", stddev)
        print("\n")
