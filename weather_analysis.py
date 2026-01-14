"""Weather analysis helpers.

This module implements basic statistics (median and standard deviation) for
temperature data received from an external API. The input may be one of:

- A list of numeric temperature values: [12.3, 13.4, 11.0]
- A list of records (dict-like) containing a temperature field, for example:
  [{'time': '2026-01-14T09:00Z', 'temp': 12.3}, ...]
- A list of (time, temperature) tuples: [('2026-01-14T09:00Z', 12.3), ...]

The implemented functions are intentionally small and pure so they are easy to
unit test and to reuse in other parts of the project.

Functions:
- median(values)
- mean(values)
- stddev(values, sample=True)
- extract_temperatures(records)
- analyze_temperatures(records)

Assumptions made:
- If the input is a sequence of dicts, the temperature key is looked up using
  common names: 'temp', 'temperature', or 'value'. If none of these keys
  exists an exception is raised.
- stddev defaults to sample standard deviation (ddof=1). Use sample=False for
  population standard deviation.
"""

import math


def median(temperatures):
    """Return the median of temperatures.

    Raises ValueError for empty input.
    """
    if not temperatures:
        raise ValueError("median() requires at least one value")

    sorted_vals = sorted(temperatures)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        return float(sorted_vals[mid])
    # even
    return (float(sorted_vals[mid - 1]) + float(sorted_vals[mid])) / 2.0


def mean(temperatures):
    """Return the arithmetic mean of temperatures.

    Raises ValueError for empty input.
    """
    if not temperatures:
        raise ValueError("mean() requires at least one value")
    return sum(temperatures) / len(temperatures)



def stddev(temperatures, sample=True):
    """Compute the standard deviation.

    By default this computes the sample standard deviation (ddof=1). Set
    sample=False to compute the population standard deviation (ddof=0).

    Raises ValueError for empty input or when sample=True and len(temperatures) < 2.
    """
    n = len(temperatures)
    if n == 0:
        raise ValueError("stddev() requires at least one value")
    if sample and n < 2:
        raise ValueError("sample standard deviation requires at least two values")

    mu = mean(temperatures)
    ddof = 1 if sample else 0
    var = sum((x - mu) ** 2 for x in temperatures) / (n - ddof)
    return math.sqrt(var)


def _is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def analyze_temperatures(times, temperatures):
    """Compute basic temperature statistics from separate times and temperatures.

    times and temperatures must be the same length. Only the temperatures are used
    to compute statistics. This function computes the sample standard deviation.
    """
    times_list = list(times)
    temps = list(temperatures)

    if len(times_list) != len(temps):
        raise ValueError("times and temperatures must have the same length")
    if not temps:
        raise ValueError("analyze_temperatures requires at least one temperature")
    if not all(_is_number(t) for t in temps):
        raise TypeError("temperatures must be numeric")

    total = sum(temps)
    stats = {
        "minimum": min(temps),
        "maximum": max(temps),
        "sum": total,
        "mean": mean(temps),
        "median": median(temps),
        "stddev": stddev(temps, sample=True),
    }
    return stats
