A = [3,1,2,5,3] 
repeat = []
k = dict()
j = 2
count = 1
for i in A:
    # print(i,k,j,count)
    if i not in k.keys():
        k[i] = 0
        count = count + j - i
    else:
        repeat.append(i)
    j+=1
repeat.append(count)
print(repeat)
