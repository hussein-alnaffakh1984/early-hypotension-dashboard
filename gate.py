import pandas as pd

def apply_gate(X: pd.DataFrame) -> pd.DataFrame:
    """
    Gate removes stable regions (low risk)
    """
    gated = X.copy()
    gated = gated[gated["MAP"] < 75]  # simple physiological gate
    return gated
