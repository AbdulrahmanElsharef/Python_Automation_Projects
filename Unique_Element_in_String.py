def unique():
    '''create a python
function that takes a string and prints how many time each unique word exists in
the sentence'''
    string = input("enter word :")
    lis = list(string)
    del_lis = []
    unique_lis = []
    for x in lis:
        if x in del_lis:
            pass
        else:
            del_lis.append(x)
            unique_lis.append(lis.count(x))
            lis.remove(x)
    return f"unique_chr is {unique_lis} num of unique_chr is {len(unique_lis)} words"


stringuniq = unique()
print(stringuniq)
print(50*"*")

# enter word :AashutoshChauhan
# unique_chr is [1, 2, 2, 1, 4, 3, 1] num of unique_chr is 7 words
# **************************************************


def countDis():
    string = input("enter word :")
    # Stores all distinct characters
    s = set(string)
    # Return the size of the set
    return f" num of unique_chr is {len(s)}"


stringuniq = countDis()
print(stringuniq)
