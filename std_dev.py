import numpy as np
from copy import deepcopy
import pprint

buy_dict = {
    "sample1": [[36, 44], [52, 56], [49, 44]],
    "sample2": [[42, 46, 54], [62, 68, 65], [60, 56]],
    "sample3": [[42, 40, 41], [43, 52, 55], [59, 60, 55, 47]],
    "mean1": 0,
    "stddev1": 0,
    "mean2": 0,
    "stddev2": 0,
    "mean3": 0,
    "stddev3": 0
}

dataset = {
    "BUY": buy_dict
}

if __name__ == "__main__":
    # Calculate initial mean and std
    for key in dataset.keys():
        value = dataset[key]
        # Get mean and std for state1
        state1 = np.array([value["sample1"][0] + value["sample2"][0] + value["sample3"][0]])
        value["mean1"] = np.mean(state1)
        value["stddev1"] = np.std(state1)

        # Get mean and std for state2
        state2 = np.array([value["sample1"][1] + value["sample2"][1] + value["sample3"][1]])
        value["mean2"] = np.mean(state2)
        value["stddev2"] = np.std(state2)

        # Get mean and std for state3
        state3 = np.array([value["sample1"][2] + value["sample2"][2] + value["sample3"][2]])
        value["mean3"] = np.mean(state3)
        value["stddev3"] = np.std(state3)

    # Train model
    for key in dataset.keys():
        value = dataset[key]
        samples = ["sample1", "sample2", "sample3"]
        sample1_copy = deepcopy(value["sample1"])
        sample2_copy = deepcopy(value["sample2"])
        sample3_copy = deepcopy(value["sample3"])
        for sample in samples:
            # Check first boundary
            # Check to see if boundary can move left
            state1 = value[sample][0]
            state2 = value[sample][1]
            state3 = value[sample][2]
            if len(state1) > 1:
                val = state1[-1]
                val_state1 = np.abs(val - value["mean1"]) / value["stddev1"]
                val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                if val_state2 < val_state1:
                    while val_state2 < val_state1:
                        if len(state1) == 1:
                            break
                        state1.remove(val)
                        state2.insert(0, val)
                        val = state1[-1]
                        val_state1 = np.abs(val - value["mean1"]) / value["stddev1"]
                        val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
            # Check to see if boundary can move right
            elif len(state2) > 1:
                val = state2[0]
                val_state1 = np.abs(val - value["mean1"]) / value["stddev1"]
                val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                if val_state1 < val_state2:
                    while val_state1 < val_state2:
                        if len(state2) == 1:
                            break
                        state2.remove(val)
                        state1.append(val)
                        val_state1 = np.abs(val - value["mean1"]) / value["stddev1"]
                        val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]

            # Check second boundary
            if len(state2) > 1:
                val = state2[-1]
                val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                val_state3 = np.abs(val - value["mean3"]) / value["stddev3"]
                if val_state3 < val_state2:
                    if len(state2) == 1:
                        break
                    state2.remove(val)
                    state3.insert(0, val)
                    val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                    val_state3 = np.abs(val - value["mean3"]) / value["stddev3"]
            elif len(state3) > 1:
                val = state3[0]
                val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                val_state3 = np.abs(val - value["mean3"]) / value["stddev3"]
                if val_state2 < val_state3:
                    if len(state3) == 1:
                        break
                    state3.remove(val)
                    state2.append(val)
                    val_state2 = np.abs(val - value["mean2"]) / value["stddev2"]
                    val_state3 = np.abs(val - value["mean3"]) / value["stddev3"]

        # Check to see if algorithm has converged
        if sample1_copy == value["sample1"] and sample2_copy == value["sample2"] and sample3_copy == value["sample3"]:
            break

        for key in dataset.keys():
            value = dataset[key]
            # Get mean and std for state1
            state1 = np.array([value["sample1"][0] + value["sample2"][0] + value["sample3"][0]])
            value["mean1"] = np.mean(state1)
            value["stddev1"] = np.std(state1)

            # Get mean and std for state2
            state2 = np.array([value["sample1"][1] + value["sample2"][1] + value["sample3"][1]])
            value["mean2"] = np.mean(state2)
            value["stddev2"] = np.std(state2)

            # Get mean and std for state3
            state3 = np.array([value["sample1"][2] + value["sample2"][2] + value["sample3"][2]])
            value["mean3"] = np.mean(state3)
            value["stddev3"] = np.std(state3)
    pprint.pprint(dataset)
