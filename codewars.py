# def digitize(n):
#     digit=[int(x) for x in str(n)]
#     digit.reverse()
#     return digit
# print(digitize(35231))


# def sum_array(arr):
#     lis=list(arr)
#     mx=max(lis)
#     mn=min(lis)
#     lis.remove(mx); lis.remove(mn)
#     if sum(lis) <=0:
#         return 0
#     else:
#         return sum(lis)

# x=sum_array({ 1 })
# print(x)


# def greet(name, owner):
#     if name==owner:
#         return "Hello boss"
#     else :
#         return "Hello guest"
# greet("abdo","abdo")


# def string_to_array(s):
#     return s.split(" ")
# print(string_to_array("Robin Singh"))


# def likes(names):
#     if len(names) <= 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


# def xo(s):
#     lis = list(s)
#     count_x=lis.count("x") + lis.count("X")
#     print(count_x)
#     count_o=lis.count("o")+lis.count("O")
#     print(count_o)
#     if count_x == count_o:
#         return True
#     else:
#         return False


# def binary_array_to_number(arr):
#     lis = list(arr)
#     y = "".join([str(x) for x in lis])
#     print(y)
#     return int(y, 2)
# print(binary_array_to_number([0, 0, 0, 1]))


# def abbrev_name(name):
#     names=name.split(" ")
#     return f"{names[0][0]}.{names[1][0]}".upper()

# print(abbrev_name("patrick feeney"))


# def spin_words(sentence):
#     lis=sentence.split(" ")
#     new=[]
#     for x in lis :
#         if len(x)<5:
#             new.append(x)
#         else:
#             new.append(str(x[::-1]))
#     return " ".join(new)

# print(spin_words("This is another test"))
# # spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# # spinWords( "This is a test") => returns "This is a test"
# # spinWords( "This is another test"


# def valid_parentheses(string):
#     if string.count("(")==string.count(")"):
#         return True
#     else:
#         return False

# print(valid_parentheses("'hi())('"))

# # "()"              =>  true
# # ")(()))"          =>  false
# # "("               =>  false
# # "(())((()())())"


# def count_bits(n):
#     bin_n = bin(n)[2:]
#     return str(bin_n).count("1")

# print(count_bits(13))


# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0]+numbers[1]

# print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

def find_missing_letter(chars):
    alph_4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    st =[]
    count=len(chars)
    for x in alph_4:
        if x  in chars and count >0:
            pass
        else:
            st.append(x)
        count-=1
    return st


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
