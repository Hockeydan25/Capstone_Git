try: 
    with open('data.txt') as data_file:  #context manager
        contents = data_file.read()
        print(contents)
        # how is file closed here, now that the close method was removed?
except FileNotFoundError:
    print('Sorry we just couldn\'t find your file, file not found.')      