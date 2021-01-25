import sys

num_list = []

def text_to_array(filename):
    file = open(filename, "r")
    
    for x in file:
        num_list.append(x)
   
    file.close()
        
text_to_array("data.txt")
    
print(num_list[0])
print(num_list[-1])    
