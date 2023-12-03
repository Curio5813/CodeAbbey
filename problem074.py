from csv import reader
from math import sin, cos, radians


def clock_hands():
    """
    The face of analog clock has two hands and is proportionally divided by 12 marks.
    The shorter hour hand makes the whole turn (360 degrees) in 12 hours, while the
    longer minute hand makes the whole circle each hour. See Clock Face on wiki for
    more details.

    Suppose, the Cartesian Coordinate System (i.e. ordinary rectangular coordinate grid)
    is placed upon the clock face so that the center of the face has coordinates 10, 10
    and Y axis is directed upwards while X axis is directed to the right (i.e. at 3:00
    minute hand is parallel to Y axis and hour hand is parallel to X axis).

    Assuming the length of the minute hand be 9 and the length of the hour hand be 6 you
    are to find coordinates of the hand ends for each given time - e.g. (16 10) and (10 19)
    for the time 3:00.

    Input data contain the number of test cases.
    Following line contains the testcases themselves in form 03:15, 21:44 etc.
    Answer should contain four real numbers for each test case - X and Y coordinates for hour
    hand, then X and Y coordinate for minute hand. All values should be simply separated with
    spaces.

    Real values should have accuracy of 1e-7 or better. Time is specified as a value from 0:00
    to 23:59.
    :return:
    """
    arq = open("problem074.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(*l1)
    hour, minutes, x_hour, y_hour, x_minutes, y_minutes, coord_hour = [], [], 0, 0, 0, 0, []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            hour.append(int(l1[i][0:2]))
            minutes.append(int(l1[i][3:]))
            break
    for i in range(len(hour)):
        if hour[i] == 12 or hour[i] == 0:
            angle_hour = 90
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9  # As the hand of minutes is equal the ray of the circle
            y_minutes = 10 + cos(rad_minues) * 9  # the coordinates is where the function sine and cosseno
            coord_hour.append(x_minutes)          # is inverse of the hand hours.
            coord_hour.append(y_minutes)
        elif hour[i] == 13 or hour[i] == 1:
            angle_hour = 60
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 14 or hour[i] == 2:
            angle_hour = 30
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 15 or hour[i] == 3:
            angle_hour = 0
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 16 or hour[i] == 4:
            angle_hour = 330
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 17 or hour[i] == 5:
            angle_hour = 300
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 18 or hour[i] == 6:
            angle_hour = 270
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 19 or hour[i] == 7:
            angle_hour = 240
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 20 or hour[i] == 8:
            angle_hour = 210
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 21 or hour[i] == 9:
            angle_hour = 180
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 22 or hour[i] == 10:
            angle_hour = 150
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
        elif hour[i] == 23 or hour[i] == 11:
            angle_hour = 120
            angle_minut = (minutes[i] / 60) * 6 * 5
            angle = angle_hour - angle_minut
            rad = radians(angle)
            x_hour = 10 + cos(rad) * 6
            y_hour = 10 + sin(rad) * 6
            coord_hour.append(x_hour)
            coord_hour.append(y_hour)
            angle_minutes = minutes[i] * 6
            rad_minues = radians(angle_minutes)
            x_minutes = 10 + sin(rad_minues) * 9
            y_minutes = 10 + cos(rad_minues) * 9
            coord_hour.append(x_minutes)
            coord_hour.append(y_minutes)
    print(*coord_hour)


clock_hands()
