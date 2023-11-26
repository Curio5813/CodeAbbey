from csv import reader


def star_medal():
    """
    Military decorations in the kingdom of Geometry are represented by stars
    with different number of rays. Each star is designed as consisting of
    intersecting line segments and precious gems are incrusted at each point
    where these lines cross each other. The more gems - the more valuable is
    the medal.

    Suppose the star has N rays (each ending with a point) and its line segments
    connect the points with the step of T. As an example you see above the typical
    pentagram - the star with 5 points connected with the step of 2.

    You are to tell the value of the star-medal - i.e. how many gems it has.

    Of course with the step of T = 1 stars became simple polygons and have no gems.

    Input data contains the number of medals for which you are to count gems.
    Next lines have a pair of values N T each.
    Answer should contain the amount of gems for each of medals.

    N and T will be always coprime since this allows to draw a line as a single
    figure - in contrast to Star of David for example which is build of two triangles.
    :return:
    """
    arq = open("problem108.csv")
    l1 = reader(arq, delimiter=" ")
    l1 = list(l1)
    answer = []
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            ray = int(l1[i][k])
            cross = int(l1[i][k + 1])
            medal = ray * (cross - 1)
            answer.append(medal)
            break
    print(*answer)


star_medal()
