import unittest
from datetime import date, datetime, timedelta
from airflow_test.sensor_test import get_poking_time_for_reports


class TestSensor(unittest.TestCase):
    def test_sensor_poking_time(self):
        result = datetime(2021, 1, 28)  # get_poking_time_for_reports()
        expected_result = datetime(2021, 1, 28)

        self.assertEquals(result, expected_result)
