import requests, json
from datetime import datetime

class Formatter:
    @staticmethod
    def datetime(pass_times):
        risetimes = []

        for d in pass_times:
            time = d['risetime']
            risetimes.append(time)

        times = []

        for rt in risetimes:
            time = datetime.fromtimestamp(rt)
            times.append(time.strftime("%a %d %b %Y, %H:%M"))
            # print(times)
        return times
