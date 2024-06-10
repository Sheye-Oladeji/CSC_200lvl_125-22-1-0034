# PW


def paint_calc(height, width, cover):
    number_of_cans = round(height * width / cover)
    print(f"You'll need {number_of_cans} cans of paint.")



# VID
import math



def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
