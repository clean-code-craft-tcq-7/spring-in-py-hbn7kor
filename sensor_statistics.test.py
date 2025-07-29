import math
import unittest
from sensor_statistics import calculateStats


class StatsTest(unittest.TestCase):
    def test_report_min_max_avg(self):
        computedStats = calculateStats([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_report_is_nan_for_empty_input(self):
        computedStats = calculateStats([])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))

    def test_report_for_nan_in_input(self):
        computedStats = calculateStats([1.5, 8.9, 3.2, 4.5, math.nan, math.nan])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_report_for_all_nan_values(self):
        computedStats = calculateStats([math.nan, math.nan])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))

    def test_report_for_invalid_values(self):
        computedStats = calculateStats([1e100, -0.45, 55.33, 1.5, 8.9, 3.2, 4.5, math.nan])
        self.assertTrue(math.isnan(computedStats["avg"]))
        self.assertTrue(math.isnan(computedStats["max"]))
        self.assertTrue(math.isnan(computedStats["min"]))


if __name__ == "__main__":
    unittest.main()
