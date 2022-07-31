val = int(input())
def find_last(val):
    data = []
    res = []
    for i in range(1, val+1):
        data.append(i)
       
    for i in range(1, val+1):
        count = 0 
        for j in range(0, val):
            count += (i-1)*j
            if (j+count) < len(data) and len(data) > 0:
                res.append(data.pop(j+count))
    return res[-1]
print(find_last(val))