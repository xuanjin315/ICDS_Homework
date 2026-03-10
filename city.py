import numpy as np

def city_mean(temps):
    output=[]
    for i in range(len(temps)):
        mean=[np.mean(temps[i])]
    output.append(mean)
    return output

def day_mean(temps):
    # TODO: mean per column (axis=0)
    return np.mean(temps,axis=0)
            
            
            

def apply_offset(temps, offset):
    # TODO: use broadcasting to add offset to each row
    a=temps
    b=offset.reshape(-1,1)
    output=a+b
    return output

def deviation_matrix(temps):
    # TODO: subtract each city’s mean from its row
    a=temps
    processed=city_mean(temps)
    output=a-processed
    return output
    

def city_correlation(D):
    # TODO: matrix multiplication D @ D.T / N
    N=7
    output=D@D.T/N
    return output


# ---------- Self-test ----------
if __name__ == "__main__":
    temps = np.array([
        [22, 24, 25, 28, 26, 27, 29],
        [19, 20, 21, 22, 23, 24, 25],
        [30, 32, 33, 31, 29, 30, 28],
        [25, 27, 26, 28, 27, 26, 25]
    ], dtype=float)

    offset = np.array([0.5, -0.2, 0.0, 0.3])

    print("City mean:", city_mean(temps))
    print("Day mean:", day_mean(temps))
    adjusted = apply_offset(temps, offset)
    print("After offset:\n", np.round(adjusted, 1))
    D = deviation_matrix(adjusted)
    print("Deviation matrix:\n", np.round(D, 2))
    C = city_correlation(D)
    print("City correlation:\n", np.round(C, 3))