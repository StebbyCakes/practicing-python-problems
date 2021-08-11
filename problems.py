# 1st
# Make a loop that starts by adding by adding one for every time that loop ocurrs, after it reaches a number divisible by 10 make it add an extra digit.
# Ex 1+1+1+1 ... = 10, now it goes 2+2+2+2+2.... so on and so forth
# n = 1
# sum = 0
# newsum = 0
# for i in range(n, 100):
#     if (sum % 10 != 0):
#         sum = sum + n
#         print(sum)
#     else:
#         newsum = n + 1
#         print(newsum)


# 2nd
# Make a loop that concats text to a variable everytime it loops, you need to input how many times you want it to loop.
# Ex Enter amount of times its gonna loop: 3, word: test  result = testtesttest

# loopCounter = int(input('enter a number: '))
# word = input('enter a word: ')
# output = ''
#
# for i in range(loopCounter):
#     output = word * loopCounter
#     print(output)


# 3rd
# Do a program that takes an input of any word and using a WHILE loop make it loop until the word inputed has been reduced to a single character.
# Ex: Word = CSGO  loop results = CSGO = CSG = CS = Final Result = C.
word2 = input('Enter a word: ')
while (len(word2) > 1):
    word2 = word2[:-1]
    print(word2)






# 4th
# Create a list that has an item with a property named color. Each item in the list needs to have the property color filled with something that isn't null.
# You can fill the list in whichever way you see fit.
# Once the list is full with as many colors as possible you need to asign a number to each color, assign a number to each color in the list and print the name of
# the colors with their respective number.
# Ex: List = red, blue, red, green   Outuput should be 1,2,1,3.
