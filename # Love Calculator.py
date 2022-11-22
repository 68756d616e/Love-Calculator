# Welcome to the Love Calculator
# The love calculator sees how many time the letters ture love appear in you, and your crsuh name. Depending on the amount, you
# will be given a result, whether you are good for each other or not.
# Below you will find two methods of the calculator, version 1 merge both names together and then provide a result, 
# while the other seperates the name.
# Example Version 1
# Example version 2

#Version 1

print("Welcome to the Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is the name of your crush? ")

bothnames = name1 + name2
bothnameslower = bothnames.lower()

a = bothnameslower.count('t')
b = bothnameslower.count('r')
c = bothnameslower.count('u')
d = bothnameslower.count('e')
e = bothnameslower.count('l')
f = bothnameslower.count('o')
g = bothnameslower.count('v')
h = bothnameslower.count('e')

true = a + b + c + d 
love = e + f + g + h

result = str(true) + str(love)
result_int = int(result)

if result_int < 10 or result_int > 90:
  print(f"Your score is {result_int}, you go together like coke and mentos.")
elif result_int > 40 and result_int < 50:
  print(f"Your score is {result_int}, you are alright together.")
else:
  print(f"Your score is {result_int}.")
  
# Version 2

# # Python Love Calculator

# print("Welcome to the Love Calculator")
# name1 = str.lower(input("What is your name? "))
# name2 = str.lower(input("What is the name of your crush? "))

# a = name1.count('t')
# b = name1.count('r')
# c = name1.count('u')
# d = name1.count('e')
# e = name1.count('l')
# f = name1.count('o')
# g = name1.count('v')
# h = name1.count('e')

# total1 = a + b + c + d + e + f + g + h

# i = name2.count('t')
# j = name2.count('r')
# k = name2.count('u')
# l = name2.count('e')
# m = name2.count('l')
# n = name2.count('o')
# o = name2.count('v')
# p = name2.count('e')

# total2 = i + j + k + l + m + n + o + p

# total3 = int('%d%d' % (total1, total2))

# if total3 < 10 or total3 > 90:
#   print(f"Your score is {total3}, you go together like coke and mentos.")
# elif total3 > 40 and total3 < 50:
#   print(f"Your score is {total3}, you are alright together.")
# else:
#   print(f"Your score is {total3}.")

