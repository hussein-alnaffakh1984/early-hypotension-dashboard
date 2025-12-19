import pandas as pd
import numpy as np

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic rolling features from vitals
    """
    X = pd.DataFrame()

    X["MAP"] = df["MAP"]
    X["MAP_mean_60"] = df["MAP"].rolling(60, min_periods=1).mean()
    X["MAP_std_60"] = df["MAP"].rolling(60, min_periods=1).std().fillna(0)

    X["HR"] = df["HR"]
    X["HR_mean_60"] = df["HR"].rolling(60, min_periods=1).mean()

    X["SpO2"] = df["SpO2"]
    X["SpO2_mean_60"] = df["SpO2"].rolling(60, min_periods=1).mean()

    return X.fillna(0)
