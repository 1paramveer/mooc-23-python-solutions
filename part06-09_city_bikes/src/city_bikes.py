# Write your solution here
import math

def get_data(filename):

    file_list = []

    with open(filename) as file:
        for line in file:
            line = line.strip().split(';')
            file_list.append(line)

    file_list = file_list[1:]

    return file_list

def get_station_data(filename: str):
    dict_ = {}
    data = get_data(filename)
    
    for bike in data:
        dict_[bike[3]] = tuple(list(map(float , bike[0:2])))

    return dict_

def distance(stations: dict, station1: str, station2: str):

    for name,coords in stations.items():
        if name == station1:
            longitude1 = coords[0]
            latitude1 = coords[1]
        if name == station2:
            longitude2 = coords[0]
            latitude2 = coords[1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):

    max_distance = 0
    station1 = ''
    station2 = ''

    for i in stations:
        for j in stations:
            if distance(stations, i , j) > max_distance:
                station1 = i
                station2 = j
                max_distance = distance(stations, i , j)

    return (station1, station2, max_distance)

if __name__ == "__main__":

    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
