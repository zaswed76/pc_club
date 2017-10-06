

a = [1, 1, 2, 2, 3, 3]

def rs(lst):
    res = []
    for i in lst:
        if not i in res:
            res.append(i)
        else:
            res.append("")
    return res

print(rs(a))


