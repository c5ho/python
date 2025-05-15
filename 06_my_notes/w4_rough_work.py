# print("Hello World!")
# a = "Hello World"
# b = "Hi"
# c = "hi"

# print(a[1])

# #for x in a:
#  # print(x)

# for x in range(len(a)):
#   print(x, a[x])

# print(len('hello'))

# #del a[5]
# print(a)
# print(len(a))
# newA = a.replace(a[5], "")
# a = newA
# # print(newA)
# # print(len(newA))
# print(a)
# print(len(a))

# if a[0] == c[0]:
#   print("TRUE")
# else:
#   print("FALSE") 

# Proceed if length of word1 = length of word2.
# Iterate through every letter in word1.
# For each letter in word1, iterate through each letter in word2.
# If there's a match, remove that letter form word2.
# Proceed to the next letter in word1 and repeat.
# If there's no match, exit (both) loops, result is false.
# If iterate to last letter of word1 and there is a match in word2
# then result is true.

word1 = "12345"
word2 = "abcde"
word3 = "Cars"

for x in range(len(word1)):
  # print(word1[x])
  # for y in range(len(word2)):
  print(word1[x], word2[y])
  index = word1.find(word2[x]) 
      print("this is ", word2)
print(word1)
print(word2)