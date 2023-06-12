import pandas as pd
import os.path


def load(path: str) -> pd.DataFrame:
    assert isinstance(path, str), "path isn t a string"
    assert ".csv" in path, "format not handle"
    if os.path.exists(path) is False:
        print("path not found")
        return None
    csv = pd.read_csv(path)
    print("Loading dataset of dimensions", csv.shape)

    return csv


load.__doc__ = "load a csv and return a dataframe"
