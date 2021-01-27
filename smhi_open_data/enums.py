from enum import Enum


# See https://opendata.smhi.se/apidocs/metobs/parameter.html
class Parameter(Enum):
    TemperaturePast1h = 1               # Lufttemperatur                        Momentanvärde, 1 gång/tim
    TemperaturePast24h = 2              # Lufttemperatur                        Medelvärde 1 dygn, 1 gång/dygn, kl 00
    WindDirection = 3                   # Vindriktning                          Medelvärde 10 min, 1 gång/tim
    WindSpeed = 4                       # Vindhastighet	                        Medelvärde 10 min, 1 gång/tim
    PrecipPast24hAt06 = 5               # Nederbördsmängd                       Summa 1 dygn, 1 gång/dygn, kl 06
    Humidity = 6                        # Relativ Luftfuktighet	                Momentanvärde, 1 gång/tim
    PrecipPast1h = 7                    # Nederbördsmängd                       Summa 1 timme, 1 gång/tim
    SnowDepthPast24h = 8                # Snödjup                               Momentanvärde, 1 gång/dygn, kl 06
    Pressure = 9                        # Lufttryck reducerat havsytans nivå    Vid havsytans nivå, momentanvärde, 1 gång/tim
    SunLast1h = 10                      # Solskenstid                           Summa 1 timme, 1 gång/tim
    RadiaGlob = 11                      # Global Irradians (svenska stationer)  Medelvärde 1 timme, 1 gång/tim
    Visibility = 12                     # Sikt                                  Momentanvärde, 1 gång/tim
    CurrentWeather = 13                 # Rådande väder                         Momentanvärde, 1 gång/tim resp 8 gånger/dygn
    PrecipPast15m = 14                  # Nederbördsmängd                       Summa 15 min, 4 gånger/tim
    PrecipMaxPast15m = 15               # Nederbördsintensitet                  Max under 15 min, 4 gånger/tim
    CloudCover = 16                     # Total molnmängd                       Momentanvärde, 1 gång/tim
    PrecipPast12h = 17                  # Nederbörd                             2 gånger/dygn, kl 06 och 18
    PrecipPast24hAt18 = 18              # Nederbörd                             1 gång/dygn, kl 18
    TemperatureMinPast24h = 19          # Lufttemperatur                        Min, 1 gång per dygn
    TemperatureMaxPast24h = 20          # Lufttemperatur                        Max, 1 gång per dygn
    WindSpeedTown = 21                  # Byvind                                Max, 1 gång/tim
    TemperatureMeanPastMonth = 22       # Lufttemperatur                        Medel, 1 gång per månad
    PrecipPastMonth = 23                # Nederbördsmängd                       Summa, 1 gång per månad
    LongwaveIrradians = 24              # Långvågs-Irradians                    Långvågsstrålning, medel 1 timme, varje timme
    WindSpeedMaxMeanPast3h = 25         # Max av MedelVindhastighet             Maximum av medelvärde 10 min, under 3 timmar, ...
    TemperatureMinPast12h = 26          # Lufttemperatur                        Min, 2 gånger per dygn, kl 06 och 18
    TemperatureMaxPast12h = 27	        # Lufttemperatur                        Max, 2 gånger per dygn, kl 06 och 18
    CloudLayerLowest = 28               # Molnbas                               Lägsta molnlager, momentanvärde, 1 gång/tim
    CloudAmountLowest = 29              # Molnmängd                             Lägsta molnlager, momentanvärde, 1 gång/tim
    CloudLayerOther = 30                # Molnbas                               Andra molnlager, momentanvärde, 1 gång/tim
    CloudAmountOther = 31               # Molnmängd                             Andra molnlager, momentanvärde, 1 gång/tim
    CloudLayer3rd = 32                  # Molnbas                               Tredje molnlager, momentanvärde, 1 gång/tim
    CloudAmount3rd = 33                 # Molnmängd                             Tredje molnlager, momentanvärde, 1 gång/tim
    CloudLayer4th = 34                  # Molnbas                               Fjärde molnlager, momentanvärde, 1 gång/tim
    CloudAmount4th = 35                 # Molnmängd                             Fjärde molnlager, momentanvärde, 1 gång/tim
    CloudStorageLowest = 36             # Molnbas                               Lägsta molnbas, momentanvärde, 1 gång/tim
    CloudStorageLowestMin = 37          # Molnbas                               Lägsta molnbas, min under 15 min, 1 gång/tim
    PrecipIntensityMaxMeanPast15m = 38  # Nederbördsintensitet                  Max av medel under 15 min, 4 gånger/tim
    TemperatureDew = 39                 # Daggpunktstemperatur                  Momentanvärde, 1 gång/tim
    GroundCondition = 40                # Markens tillstånd                     Momentanvärde, 1 gång/dygn, kl 06
