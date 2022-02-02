"""
Dan Smestad ITEC 2905-80 Capstone 2/2/2021.
Python testing example for testing your code. 
"""

def triangle_area(base, height):
    if base < 0 or height < 0:  #adding in if statement to create oppertunity good testing
        raise ValueError('Base and height must be above 0 or another positive')
        # this would be an example of TDD? 
    return base * height * 0.5

