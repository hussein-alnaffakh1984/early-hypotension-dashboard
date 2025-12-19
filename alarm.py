def generate_alarm(prob: float, threshold: float) -> str:
    """
    Alarm levels:
    A = severe
    B = moderate
    C = mild
    """
    if prob >= threshold + 0.2:
        return "A"   # Rapid / severe drop
    elif prob >= threshold:
        return "B"   # Gradual hypotension
    elif prob >= threshold - 0.05:
        return "C"   # Intermittent
    else:
        return ""
