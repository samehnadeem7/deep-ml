import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    mean = np.mean(data)
    median = np.median(data)

    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)]

    variance = np.var(data)
    standard_deviation = np.std(data)

    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)

    iqr = q3 - q1

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }