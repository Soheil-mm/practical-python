# bounce.py
#
# Exercise 1.5
height = 100.0
bounce_back = 0

while bounce_back < 10:
    bounce_back = bounce_back + 1
    height = height * 0.6
    print(bounce_back, round(height , 4))