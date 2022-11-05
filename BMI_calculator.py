# BMI calculator : create a python function that takes the user height , weight and
# print the user BMI and if the user underweight , overweight or healthy


from pywebio.input import *
from pywebio.output import *


def bmi():
    '''This is just a very simple script if you ignore PyWebIO, but after using the input and output functions provided by PyWebIO, you can interact with the code in the browser:'''
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break


if __name__ == '__main__':
    bmi()
    '''Your BMI: 26.3. Category: Overweight'''

# Please enter height in meters(m)171
# Please enter Mass/Weight in Kilograms(Kg)76
# Your BMI is {0.002599090318388564} and the person is : {'severely underweight'}
