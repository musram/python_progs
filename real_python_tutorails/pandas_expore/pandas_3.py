#https://realpython.com/pandas-settingwithcopywarning/#example-of-a-settingwithcopywarning


import pandas as pd
import numpy as np


if __name__ == "__main__":
    data = {"x": 2**np.arange(5),
        "y": 3**np.arange(5),
        "z": np.array([45, 98, 24, 11, 64])}

    index = ["a", "b", "c", "d", "e"]

    df = pd.DataFrame(data=data, index=index)

    print(df)

    #mask is an instance of a Pandas Series with Boolean data and the indices from df:


    mask = df["z"] < 50
    print(mask)

    print(df[mask])

    
    df[mask]["z"] = 0 #look at the webpage to understand this

