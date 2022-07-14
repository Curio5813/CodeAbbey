"""
===============
Body Mass Index
===============

Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only
abstract things.

The simple measure of body constitution was proposed at the middle of XIX century. It depends only on the
height and weight of a person - and is called Body Mass Index or BMI. It is defined as:

BMI = weight / height^2
Where weight is taken in kilograms and height in meters.

Four general grades are proposed:

Underweight     -           BMI < 18.5
Normal weight   -   18.5 <= BMI < 25.0
Overweight      -   25.0 <= BMI < 30.0
Obesity         -   30.0 <= BMI
For example, if I have weight of 80 kg and height of 1.73 m I can calculate:

BMI = 80 / (1.73)^2 = 26.7
i.e. somewhat overweight.

We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades
for several people.

Input data contain number of people in the first line.
Other lines will contain two values each - weight in kilograms and height in metres.
Answer should contain words under, normal, over, obese for each corresponding test-case, separated with
spaces. For example:

input data:
3
80 1.73
55 1.58
49 1.91

answer:
over normal under
"""

print('')
v1 = [45, 1.40,
      72, 1.66,
      93, 2.78,
      63, 1.87,
      107, 2.31,
      75, 2.61,
      104, 2.83,
      67, 1.83,
      108, 2.88,
      58, 1.97,
      75, 2.61,
      60, 1.88,
      105, 2.96,
      48, 1.92,
      112, 2.43,
      80, 1.47,
      104, 1.72,
      83, 1.90,
      116, 1.87,
      99, 1.76,
      54, 1.90,
      105, 1.68,
      60, 2.00,
      66, 2.25,
      59, 1.54,
      63, 1.47,
      87, 1.87,
      114, 2.33,
      87, 2.81]
v2 = []
for i in range(0, len(v1), 2):
    bmi = v1[i] / v1[i + 1] ** 2
    if bmi < 18.5:
        situation = 'under'
        v2.append(situation)
    if 18.5 <= bmi < 25:
        situation = 'normal'
        v2.append(situation)
    if 25.5 <= bmi < 30:
        situation = 'over'
        v2.append(situation)
    if 30 <= bmi:
        situation = 'obese'
        v2.append(situation)
for k in range(0, len(v2)):
    print(v2[k], end=' ')
print('')
print('')
