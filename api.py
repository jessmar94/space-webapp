import requests, json
from datetime import datetime

class API:
    @staticmethod
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def datetime(obj):
        pass_times = obj.json()['response']

        risetimes = []

        for d in pass_times:
            time = d['risetime']
            risetimes.append(time)

        times = []

        for rt in risetimes:
            time = datetime.fromtimestamp(rt)
            times.append(time)
            print(time)
        return times
        # return risetimes
