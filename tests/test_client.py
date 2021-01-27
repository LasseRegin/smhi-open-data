import unittest
import warnings

from smhi_open_data import SMHIOpenDataClient, Parameter, microseconds2date


warnings.simplefilter('ignore', ResourceWarning)


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = SMHIOpenDataClient()

    def test_stations(self):
        stations = self.client.get_stations()
        self.assertIsInstance(stations, list, 'Did not return a list of stations')
        self.assertGreater(len(stations), 0, 'Could not find any stations')

    def test_observations(self):
        observations = self.client.get_latest_observations(parameter=Parameter.TemperaturePast1h)
        self.assertIsInstance(observations, list, 'Did not return a list of observations')
        self.assertGreater(len(observations), 0, 'Could not find any observations')

    def test_list_parameters(self):
        parameters = self.client.list_parameters()
        self.assertTrue(
            all(
                isinstance(Parameter(parameter['value']), Parameter)
                for parameter in parameters
            ),
            'Returned a wrong parameter')

    def test_get_parameter(self):
        parameter = self.client.get_parameter(parameter_id=1)
        self.assertIsInstance(parameter, Parameter, 'Returned value was not a Parameter object.')
        self.assertEqual(parameter, Parameter.TemperaturePast1h, 'Wrong parameter returned.')


if __name__ == '__main__':
    unittest.main()
