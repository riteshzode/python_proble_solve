# problem 2
# Input:a4b3c2
# Output:aaaabbbcc

# this code is only work for no 0 to 9 not more than that
user_input = "a1b3c2"

# we are using list
string_value = []
integer_value = []

for i in user_input:
    try:
        # try to change the type to integer
        type(int(i))
        integer_value.append(i)

    except ValueError:
        # if it is string then it will give error
        type(str(i))
        string_value.append(i)

# print(string_value)
# print(integer_value)

# making empty dictionary
dict = {}

for i in range(len(string_value)):
    dict[string_value[i]] = int(integer_value[i])

# print(dict)

# storing all the value in temporary list

temp = [i*j for i, j in dict.items()]

# use join function to join entire list

print("".join(temp))