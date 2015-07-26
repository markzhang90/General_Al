__author__ = 'mark'


def subsets(S):
        res = []
        S.sort(reverse=True)
        subsets_rec(S, 0, res)
        return res


def subsets_rec(arr, i, res):
    print arr
    if i == len(arr):
        res.append([])
    else:
        subsets_rec(arr, i+1, res)
        temp = []
        for item in res:
            # if ([arr[i]] + item) not in res: # subsets 2

            temp.append([arr[i]] + item)
        res.extend(temp)
#         res.extend([item + [arr[i]] for item in res])


def subsets_dfs(S):
    S.sort()
    res = []
    def dfs(depth, start, valuelist):
        # if valuelist not in res: # subsets 2
        res.append(valuelist)
        if depth == len(S): return
        for i in range(start, len(S)):
            dfs(depth+1, i+1, valuelist+[S[i]])

    dfs(0, 0, [])
    return res

list = [1,2,3]
print subsets(list)
