"""
2-5 x: xijixppjwqx
All input from text.txt is assumed to be structured identically to the one above.

PART 1:
Numbers indicate the number of times x must be present in the string.
In this case, x must be present at least twice and no more than five times.

PART 2:
Numbers indicate two positions in the string, and our char must occupy ONLY one of those positions
for the password to be valid.
In this case, x must either be in the second or fifth position, but it can't be in both. 
Their fictional password system is not zero-indexed.
"""

###SOLUTION TO PART 1###
"""
file = open("text.txt")
good_password_count = 0

for x in file:
    
    ###Splits password into array ['1-3', 'a:', 'asdgasg']
    pw_info = x.split()
    
    limits = pw_info[0].split('-')
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])
    
    ###pw_char is the first character of the second element of our pw_info array
    pw_char = pw_info[1][0]
    
    pw_string = pw_info[2]
    letter_count = pw_string.count(pw_char)
    
    if letter_count >= lower_limit and letter_count <= upper_limit:
        good_password_count += 1

print(good_password_count)

file.close()
"""

###SOLUTION TO PART 2###
###Most of the logic here is copied from solution 1
"""
file = open("text.txt")
good_password_count = 0

for x in file:

    pw_info = x.split()
    
    positions = pw_info[0].split('-')
    first_pos = int(positions[0])
    second_pos = int(positions[1])
    
    pw_char = pw_info[1][0]
    pw_string = pw_info[2]
    
    ###Because their fictional password system is not zero-indexed we subtract one from each position
    if pw_string[first_pos - 1] == pw_char and pw_string[second_pos - 1] != pw_char:
        good_password_count += 1
    if pw_string[second_pos -1] == pw_char and pw_string[first_pos - 1] != pw_char:
        good_password_count += 1

print(good_password_count)
file.close()
"""