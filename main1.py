# problem 1
# Input:a5b7c1
# Output:abc571

user_input = "a5b7c1"

string_value = ""
integer_value = ""

for i in user_input:
    if i.isnumeric():
        integer_value += i
    else:
        string_value += i

# print(string_value)
# print(integer_value)

combine = string_value + integer_value

print(combine)