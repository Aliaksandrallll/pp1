dict1={
    "arr1":[4,5,6],
    "arr2":[7,5]
}
dict2={
    "arr1":[2,6,5],
    "arr2":[7,1],
    "arr3":[2,9,8,1]
}
def f(dictionary,x,y):
    sum=0
    for key in dictionary:
        for value in dictionary[key]:
            if (value in range(x,y+1)):
                sum=sum+value
    return sum 

print(f(dict1,5,6))
print(f(dict2,5,10))