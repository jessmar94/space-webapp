class Coordinates:
    @staticmethod
    def lat_long(city):
        params = {
            "lat": 0,
            "lon": 0
        }
        if city == "New York":
            params.update({
                "lat": 40.71,
                "lon": -74
            })
        if city == "London":
            params.update({
                "lat": 51.50853,
                "lon": -0.12574
            })
        if city == "Cape Town":
            params.update({
                "lat": -33.9188610,
                "lon": 18.42330
            })
        if city == "Tokyo":
            params.update({
                "lat": 35.652832,
                "lon": 139.839478
            })
        return params
