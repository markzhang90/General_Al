__author__ = 'mark'
# String Break

s = "leeetleetcode"
dict = ["leet", "code"]


def word_break(s, dic):
    result_set = [False for i in range(len(s)+1)]
    result_set[0] = True

    for i in range(len(s)):
        for j in range(i+1):
            print "%d---%s" % (i, s[j:(i+1)])
            if result_set[j] and (s[j:(i+1)] in dic):
                result_set[i+1] = True
                break
    print result_set
    return result_set[-1]



print word_break(s, dict)