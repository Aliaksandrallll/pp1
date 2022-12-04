def f(array2d):
    sum=[]
    for i in range(len(array2d[0])):
        sum.append(0)
    for i in range(len(array2d[0])):
        for j in range(len(array2d)):
           sum[i]+= array2d[j][i]
    return sum

    


a = [[3,6,2,7], [9,5,4,0], [2,8,0,9]]
print(f(a)) 
