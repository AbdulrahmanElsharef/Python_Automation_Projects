# - Number to words . Create a python function that takes an integer number and
# print the number in words
from num2words import num2words


def num_words():
    '''Create a python function that takes an integer number and
print the number in words'''
    num = int(input("enter number : "))
    return num2words(num,lang='ar')
    # inpute number and return words in arabic langushe


words = num_words()
print(words)
help(num_words)


# enter number : 175
# مائةخمسة و سبعون

# enter number : 1987
# one thousand, nine hundred and eighty-seven


# enter number : 2020
# two thousand and twenty


# Help on function num_words in module __main__:

# num_words()
#     Create a python function that takes an integer number and
#     print the number in words
