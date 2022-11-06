# - Number to words . Create a python function that takes an integer number and
# print the number in words
from num2words import num2words


def num_words():
    '''Create a python function that takes an integer number and
print the number in words'''
    num = int(input("enter number : "))
    return f"{num2words(num,lang='ar')}\n{num2words(num,lang='en')}"

    # inpute number and return words in arabic langushe
words = num_words()
print(words)

# enter number : 13875
# ثلاثة عشر ألفاً  و ثمانمائةخمسة و سبعون
# thirteen thousand, eight hundred and seventy-five

# enter number : 1987
# one thousand, nine hundred and eighty-seven


# enter number : 2020
# two thousand and twenty


# Help on function num_words in module __main__:

# num_words()
#     Create a python function that takes an integer number and
# #     print the number in words
# واحد مليار  و ثمانية و ثمانون مليوناً  و سبعمائةسبعة و ثمانون ألفاً  و مئتان و خمسة و أربعون
# one billion, eighty-eight million, seven hundred and eighty-seven thousand, two hundred and forty-five