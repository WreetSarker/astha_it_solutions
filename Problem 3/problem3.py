#taking test case number from user
test_cases = int(input())
for i in range(test_cases):
    #taking line input
    st = input()
    stArr = st.split(" ")
    data = []

    # Storing initials of each string and concatanating them to a string and forming an array
    for j in range(len(stArr[0])):
        res = ''
        for k in range(len(stArr)):
            res += stArr[k][j]
        data.append(res)
    final_res = ''
    # going over the array to find dissimilarities
    for j in range(len(data)):
        count = 0
        for k in range(len(data[0])-1):
            if data[j][k] != data[j][k+1]:
                count += 1
        if count > 0:
            final_res += '?'
        else:
            final_res += data[j][0]
        
    print(final_res)