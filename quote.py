"""
Dan Smestad ITEC 2905-80 Capstone 2/1/2021.
Python code example for reading a file. 

Generate quotes for lawns service.
small lawn = $10
medium lawn = $15
lager lawn = $20

add $5 for same-dat service.

"""

def lawn_quote(size, same_day):
    if size == 'small':
        price = 10
    elif size == 'medium':
        price = 15  
    elif size == 'large':
        price = 20
    else:
        return # can't calculate, return None  

    if same_day:
        price += 5

    return price        