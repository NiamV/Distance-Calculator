from math import *

def distance(lat1, lon1, lat2, lon2):
    R = 6371
    return acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2)) * R

# lat1 = float(input("What is the latitude of Place 1? ")) * float(pi) / float(180)
# lon1 = float(input("What is the longitude of Place 1? ")) * float(pi) / float(180)

# lat2 = float(input("What is the latitude of Place 2? ")) * float(pi) / float(180)
# lon2 = float(input("What is the longitude of Place 2? ")) * float(pi) / float(180)

