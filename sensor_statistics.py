import math
import statistics

from typing import List


def calculateStats(numbers: List[float]):
    numbers = list(filter(lambda x: isinstance(x, float) and not math.isnan(x), numbers))
    if numbers and all(0.0 <= x <= 50.0 for x in numbers):
        return {"avg": statistics.mean(numbers), "min": min(numbers), "max": max(numbers)}
    return {"avg": math.nan, "min": math.nan, "max": math.nan}
