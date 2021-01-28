"""
1-3 x: xijijppjwqx
Numbers indicate the number of times x must be present in the string
In this case, x must be present at least once and no more than three times
"""


# def text_to_array(filename):

    # words_list = []
    # file = open(filename)
    
    # for x in file:
        # words_list.append(x.split())
     
    # print(words_list)
    
    # file.close()
file = open("short-text.txt")

my_list = []

my_word = file.readline().split()
num = my_word[0].split('-')
for x in num:
    my_list.append(int(x))
    
print(type(my_list[0]))    
print(num)
print(my_word)

file.close()

# nums = my_array[0].split('-')
# for x in nums:
    
# print(nums)   

# text_to_array("short-text.txt")
