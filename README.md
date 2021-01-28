
# SMHI Open Data API

Simple Python interface to the Swedish Meteorological and Hydrological Institute's (SMHI) [Open Data API](https://opendata.smhi.se/apidocs/metobs/index.html).

Weather data from Sweden are publicly available through SMHI's Open Data API. Fetch raw weather observations from all available weather stations in Sweden. Parameters available include _temperature_, _windspeed_, _humidity_, _pressure_, _precipitation__, and many more.

## Requirements

* Python 3.6+

## Installation

```bash
$ pip install smhi-open-data
```

## Example

```python
from smhi_open_data import SMHIOpenDataClient, Parameter


# Get 10 stations
client = SMHIOpenDataClient()

# Get all stations
stations = client.get_stations()

# Get available parameters
parameters = client.list_parameters()

# Get available parameters at station
parameters_station = client.get_station_parameters(station_id=173010)

# Get temperature observations from available stations from past hour
observations = client.get_latest_observations(
    parameter=Parameter.TemperaturePast1h)
```

## Tests

Run tests
```bash
$ python -m unittest discover tests
```
