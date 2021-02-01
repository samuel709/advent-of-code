"""
1-3 x: xijijppjwqx
Numbers indicate the number of times x must be present in the string
In this case, x must be present at least once and no more than three times

Input is always assumed to be structured identically to ^^^
"""


# def text_to_array(filename):

    # words_list = []
    # file = open(filename)
    
    # for x in file:
        # words_list.append(x.split())
     
    # print(words_list)
    
    # file.close()
    
file = open("short-text.txt")
is_valid = False

###Splits password into an array
###[upper and lower limits, character we are counting, string we are to check]
password = file.readline().split()

###Get the lower and upper limits from our password 
nums = password[0].split('-')
lower_limit = int(nums[0])
upper_limit = int(nums[1])

###Get the character we are counting in our string
char_to_check = password[1][0]

###Count the number of times a character appears in the string
###Return True if count is greater than lower limit and less than upper limit
letter_count = password[2].count(char_to_check)
if letter_count > lower_limit and letter_count < upper_limit:
    is_valid = True


for x in file:
    print(x)

    
# print(lower_limit, upper_limit)
# print(char_to_check)
# print(letter_count)
# print(is_valid)

file.close()

