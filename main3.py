# check weather it is integer or alphabet

s = 'a4b3c2'
alphabet = []
numaric = []
for i in s:
    if i.isalpha():
        alphabet.append(i)
    elif i.isnumeric():
        numaric.append(int(i))

print(alphabet, numaric)

# using in built python sorted function to sort a list

l1 = [2, 5, 10, 9, 3, 1]
# l1.sort(reverse=True)
# print(l1)
print(sorted(l1))
print(sorted(l1, reverse=True))
