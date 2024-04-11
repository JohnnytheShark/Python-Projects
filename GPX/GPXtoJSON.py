# %%
import gpxpy
import json

class GPXtoJSONConverter:
    '''Class based component used as a tool to convert GPX files into JSON for frontends'''
    def __init__(self, gpx_file):
        self.gpx_file = gpx_file
        self.gpx_data = gpxpy.parse(open(gpx_file,'r'))
        self.data = {
            'waypoints':[],
            'tracks':[],
            'routes':[]
        }

    def extract_data(self):
            for waypoint in self.gpx_data.waypoints:
                self.data['waypoints'].append({
                    'name': waypoint.name,
                    'latitude': waypoint.latitude,
                    'longitude': waypoint.longitude,
                    'elevation': waypoint.elevation,
                    'time': waypoint.time.isoformat() if waypoint.time else None
                })

            for track in self.gpx_data.tracks:
                track_data = {
                    'name': track.name,
                    'segments': []
                }
                for segment in track.segments:
                    segment_data = []
                    for point in segment.points:
                        point_data = {
                            'latitude': point.latitude,
                            'longitude': point.longitude,
                            'elevation': point.elevation,
                            'time': point.time.isoformat() if point.time else None,
                            'heart_rate': None # Initialize heart rate to None
                        }
                        # Extract heart rate from extensions
                        for extension in point.extensions:
                            if extension.tag == '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}TrackPointExtension':
                                for child in extension:
                                    if child.tag == '{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr':
                                        point_data['heart_rate'] = child.text
                        segment_data.append(point_data)
                    track_data['segments'].append(segment_data)
                self.data['tracks'].append(track_data)

            for route in self.gpx_data.routes:
                route_data = {
                    'name': route.name,
                    'points': []
                }
                for point in route.points:
                    route_data['points'].append({
                        'latitude': point.latitude,
                        'longitude': point.longitude,
                        'elevation': point.elevation,
                        'time': point.time.isoformat() if point.time else None
                    })
                self.data['routes'].append(route_data)

    def convert_to_json(self, output_file):
        with open(output_file, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)


# %%
converter = GPXtoJSONConverter("./MarthonRun.gpx")
converter.extract_data()
converter.convert_to_json("MarthonRun.json")


