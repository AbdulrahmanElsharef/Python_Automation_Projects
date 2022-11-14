# Create 2 functions , the first one takes text as input,
# replaces each letter with another letter, and outputs the “encoded” message. , the
# second one decode the message to the original text
def encoded():
    lis_str = list(input("enter your code :"))
    lis_str.reverse()
    global encoded_str
    encoded_str = "".join(lis_str)
    print(f"encoded message is {encoded_str}".title())
    print(50*"*")
    return encoded_str


encoded()
# enter your code :Python code generator - itemis AG
# Encoded Message Is Ga Simeti - Rotareneg Edoc Nohtyp
# **************************************************
# ________________________________________________________
# enter your code :Create a code generator
# Encoded Message Is Rotareneg Edoc A Etaerc
# **************************************************


def decode():
    lis_str = list(encoded_str)
    lis_str.reverse()
    decode_str = "".join(lis_str)
    print(f"decode message is {decode_str}".title())
    print(50*"*")
    return decode_str


decode()
# Decode Message Is Python Code Generator - Itemis Ag
# **************************************************
# ________________________________________________________
# Decode Message Is Create A Code Generator
# **************************************************

# enter your code :pythondevlober1585
# Encoded Message Is 5851Rebolvednohtyp
# **************************************************
# Decode Message Is Pythondevlober1585
# **************************************************
