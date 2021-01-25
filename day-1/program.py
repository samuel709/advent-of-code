import sys, time
num_list = []

start_time = time.time()

def text_to_array(filename):
    file = open(filename, "r")
    
    for x in file:
        num_list.append(int(x))

   
    file.close()
    
## Solution to part 1
# def add_nums(num_list):
    # for first_index, first_num in enumerate(num_list):
        # for second_index, second_num in enumerate(num_list[first_index+1::]):
            # if (first_num + second_num == 2020):
                # print("We did it!")
                # print(first_num * second_num)
                # return 
                
def add_nums(num_list):
    for first_index, first_num in enumerate(num_list):
        for second_index, second_num in enumerate(num_list[first_index+1::]):
            for third_index, third_num in enumerate(num_list[second_index+1::]):
                if (first_num + second_num + third_num == 2020):
                    print("We did it!")
                    print(first_num * second_num * third_num)
                    return
                
                
        
text_to_array("data.txt")
add_nums(num_list)

print("My program took {}".format(time.time() - start_time))
   
