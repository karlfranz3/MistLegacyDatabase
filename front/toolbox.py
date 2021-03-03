import math


def area(poly):
    """
    calculate the area of polygon
    Keyword arguments:
    poly -- polygon geojson object
    return polygon area
    """
    poly_area = 0
    # TODO: polygon holes at coordinates[1]
    points = poly['coordinates'][0]
    j = len(points) - 1
    count = len(points)

    for i in range(0, count):
        p1_x = points[i][1]
        p1_y = points[i][0]
        p2_x = points[j][1]
        p2_y = points[j][0]

        poly_area += p1_x * p2_y
        poly_area -= p1_y * p2_x
        j = i

    poly_area /= 2
    return poly_area


def centroid(poly):
    """
    get the centroid of polygon
    adapted from http://paulbourke.net/geometry/polyarea/javascript.txt
    Keyword arguments:
    poly -- polygon geojson object
    return polygon centroid
    """
    f_total = 0
    x_total = 0
    y_total = 0
    # TODO: polygon holes at coordinates[1]
    points = poly['coordinates'][0]
    j = len(points) - 1
    count = len(points)

    for i in range(0, count):
        p1_x = points[i][1]
        p1_y = points[i][0]
        p2_x = points[j][1]
        p2_y = points[j][0]

        f_total = p1_x * p2_y - p2_x * p1_y
        x_total += (p1_x + p2_x) * f_total
        y_total += (p1_y + p2_y) * f_total
        j = i

    six_area = area(poly) * 6
    return {'type': 'Point', 'coordinates': [y_total / six_area, x_total / six_area]}
