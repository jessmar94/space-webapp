class Coordinates:
    @staticmethod
    def lat_long(city):
        params = {
            "lat": 0,
            "lon": 0,
        }
        if city == "New York":
            params.update({
                "lat": 40.71,
                "lon": -74,
            })
        return params 
