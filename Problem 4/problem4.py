import re
from collections import defaultdict 
s = input()
x = re.findall("(?=(\d\d-\d\d-\d\d\d\d))", s)
ans = ""
def val():
    return 0
dates = defaultdict(val)
maxVal = 0
for date in x:
    d, m, y = [int(x) for x in date.split('-')]
    if(2013 <= y <= 2015 and 1 <= d <= 31 and 1 <= m <= 12):
        if m in [1, 3, 5, 7, 8, 10, 12] and 1 <= d <= 31:
            dates[date] += 1
        elif m == 2 and 1 <= d <= 28:
            dates[date] += 1
        elif m in [4, 6, 9, 11] and 1 <= d <= 30:
            dates[date] += 1
        if date in dates and dates[date] > maxVal:
            maxVal = dates[date]
            ans = date 
    else:
        pass
 
# print(x)
# print(dates)
print(ans)