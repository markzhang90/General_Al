__author__ = 'mark'
#Reverse words in a given string
"""
1) Reverse the individual words, we get the below string.
     "i ekil siht margorp yrev hcum"
2) Reverse the whole string from start to end and you get the desired output.
     "much very program this like i"
"""

s = "i like this program very much"


def reverse_all(s):
    my_list = []
    converted_string = ""
    for i in range(len(s)):
        print s[i]
        if s[i] != " ":
            my_list.append(s[i])
        else:
            while any(my_list):
                converted_string += my_list.pop()
            converted_string += " "

    while any(my_list):
        converted_string += my_list.pop()
    print converted_string


def reverse_single(s):
    my_list = []
    converted_string = ""
    last_p = 0
    for i in range(len(s)):
        if s[i] == " ":
            my_list.append(s[last_p:i])
            print s[last_p:i]
            last_p = i+1
        print s[last_p:i]
    converted_string += s[last_p:] + " "
    while any(my_list):
        converted_string += my_list.pop() + " "
    print converted_string

reverse_single(s)
