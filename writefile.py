numbers = ['one', 'two', 'three']

# with open('numbers.txt', 'w') as number_file:
#     number_file.writelines(numbers)  #creates numbers.txt and writes number list to writefile.

#wites with a loop, previously writefile numbers.txt would be overwritten.
# with open('numbers.txt', 'w') as number_file:  # 'w' = write mode.
#     for n in numbers:
#         number_file.write(n + '\n')  #creates writefile and writes number list to writefile.

#adding try exception error handling
#same code with append mode. I remove the extra space I had after quote for three to see append.
try:
    with open('numbers.txt', 'a') as number_file:  # 'a' = appends.
        for n in numbers:
            number_file.write(n + '\n') 
except OSError:
    print('Error writing to file.')  
    # writing error approperate as the code is writing to a text file. Choose appropreate error handling.           
    # avoid letting program crash, watch error message don't give away the key to the house.