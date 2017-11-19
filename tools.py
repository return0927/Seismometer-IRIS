import requests
from datetime import datetime, timedelta


class _IRIS:
    def __init__(self):
        self.imageAPI = "http://service.iris.edu/irisws/timeseries/1/query" \
                   "?output=plot" \
                   "&ref=direct" \
                   "&width=600" \
                   "&height=200" \
                   "&net=%s" \
                   "&sta=%s" \
                   "&loc=--" \
                   "&start=%s" \
                   "&dur=300" \
                   "&cha=%s"

        self.textAPI = "http://service.iris.edu/irisws/timeseries/1/query" \
                   "?output=ascii" \
                   "&ref=direct" \
                   "&width=600" \
                   "&height=200" \
                   "&net=%s" \
                   "&sta=%s" \
                   "&loc=--" \
                   "&start=%s" \
                   "&dur=300" \
                   "&cha=%s"

        self.seismometer = {
            "Network": "KG",
            "Station": "TJN"
        }


    def updateSeismometer(self, network, station):
        self.seismometer['Network'] = network
        self.seismometer['Station'] = station

    def getTime(self):
        return (datetime.utcnow()-timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%S")

    def getImage(self, debug=False):
        try:
            url = self.imageAPI % (
                self.seismometer['Network'],
                self.seismometer['Station'],
                self.getTime(),
                "BHZ"
            )
            if debug: print(url)

            resp = requests.get(url)
            return [False, resp.content]
        except Exception as ex:
            return [True, ex]

    def getData(self, debug=False):
        try:
            url = self.imageAPI % (
                self.seismometer['Network'],
                self.seismometer['Station'],
                self.getTime(),
                "BHZ"
            )
            if debug: print(url)

            resp = requests.get(url)
            return [False, resp.content]
        except Exception as ex:
            return [True, ex]