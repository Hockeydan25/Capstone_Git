"""
Dan Smestad ITEC 2905-80 Capstone 2/1/2021.
Python code example for reading a file. 

"""

try: 
    with open('data.txt') as data_file:  #context manager
        contents = data_file.read()
        print(contents)
        # how is file closed here, now that the close method was removed?
except FileNotFoundError:
    print('Sorry we just couldn\'t find your file, file not found.')      