"""
=====================
Smoothing the Weather
=====================

Little Merlin wants to become a meteorologist. He measures the temperature of the air each hour so that after
several days he has a long sequence of values.

However, his instruments are not ideal so the measurements are not exact - they randomly jump up and down by
several degrees from the real values.

Observing this, Merlin decided to make his data more smooth. To achieve this he only needs every value to be
substituted by the average of it and its two neighbors. For example, if he have the sequence of 5 values like
this:

3 5 6 4 5
Then the second (i.e. 5) should be substituted by (3 + 5 + 6) / 3 = 4.66666666667,
the third (i.e. 6) should be substituted by (5 + 6 + 4) / 3 = 5,
the fourth (i.e. 4) should be substituted by (6 + 4 + 5) / 3 = 5.
By agreement, the first and the last values will remain unchanged.

At the picture above the blue line shows unprocessed data while red represents the smoothing.

You are to write the program which helps Little Merlin in this whimsical algorithm of digital signal processing.

Input data will contain the length of the sequence in the first line.
The second line will contain the measurements itself.
Answer should contain the processed sequence. All values should be calculated to precision of 1e-7 or better.

Example:

input data:
7
32.6 31.2 35.2 37.4 44.9 42.1 44.1

answer:
32.6 33 34.6 39.1666666667 41.4666666667 43.7 44.1
"""
print('')


def smoothing_the_weather():
    aproximacao = []
    medidas = [31.6, 35.6, 39.3, 34.9, 41.7, 59.2, 55.4, 59.5, 46.6, 42.7, 46.1, 29.6, 25.5, 27.5, 20.0, 14.0,
               12.7, 10.0, 10.2, 19.6, 7.5, 12.8, 23.8, 36.5, 28.7, 20.2, 37.4, 39.0, 43.7, 49.6, 38.7, 58.5,
               46.0, 43.8, 25.0, 35.1, 29.0, 30.2, 19.7, 16.1, 6.4, 8.2, 12.1, 9.6, -1.9, 15.0, 20.0, 24.8, 30.3,
               30.2, 40.0, 47.1, 47.0, 47.4, 51.8, 49.7, 45.4, 56.6, 43.2, 35.2, 30.1, 29.8, 19.7, 22.2, 9.8,
               10.4, 9.0, 10.7, 10.0, 16.3, 13.9, 24.4, 37.1, 42.6, 40.3, 51.8, 44.1, 45.4, 49.9, 54.2, 46.8,
               49.5, 40.3, 36.2, 22.3, 24.6, 19.6, 15.5, 12.2, 5.1, 13.1, 20.9, 26.8, 10.9, 23.6, 21.4, 30.0,
               28.1, 41.1, 45.9, 49.7, 54.2, 41.4, 49.8, 48.9, 45.6, 40.0, 45.4, 38.3, 37.7, 22.6, 14.0, 16.8,
               10.6, 21.3, 20.2, 15.5, 14.8, 18.7, 18.5, 30.0, 25.6, 29.8, 44.1, 44.8, 55.6, 50.2, 51.2, 61.0,
               43.6, 40.0, 37.2, 25.9, 24.9, 19.9, 24.4, 11.8, 23.1, 15.4, 7.9, 22.9, 16.2, 20.0, 27.1, 18.3,
               35.1, 40.8, 48.5, 48.5, 62.2, 61.3, 44.4, 35.6, 30.0, 40.1, 33.7, 36.8, 21.9, 6.3, 21.9, 12.7,
               10.7, 10.2, 12.0, 4.1, 3.4, 20.3, 24.7, 45.0, 35.2, 40.1, 54.4, 41.0, 39.8, 51.0, 45.0, 47.3,
               44.0, 55.0, 31.9, 29.7, 36.1, 19.7, 15.8, 24.7, 21.3, 10.6, 15.8, 7.8, 16.7, 21.3, 25.9, 26.8,
               34.6, 39.9, 43.0, 47.1, 39.4, 50.8, 49.0, 47.4, 43.0, 39.1, 36.0, 29.7, 10.3, 25.6, 21.0, 12.6,
               16.3, -1.3, 12.9, 16.3, 15.8, 15.5, 27.3, 29.6, 39.9, 40.2, 44.1, 47.3, 48.8, 47.1, 50.9, 48.0,
               44.5, 26.7, 23.9, 31.0, 25.9, 19.9, 14.3, 27.2, 12.0, 21.7, 10.3, 14.1, 19.8, 16.8, 18.5]
    for k in range(0, len(medidas)):
        if 0 <= k < len(medidas) - 2:
            aproximar = round(((medidas[k] + medidas[k + 1] + medidas[k + 2])/3), 8)
            aproximacao.append(aproximar)
    aproximacao.insert(0, medidas[0])
    aproximacao.insert(239, medidas[239])
    return f'{[m for m in aproximacao]}'.replace('[', '').replace(']', '').replace(',', '')


print(smoothing_the_weather())
