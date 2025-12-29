#remove duplicate
# num=(1,2,2,3,3,4,4,4,5)
# remove=tuple(set(num))
# print(remove)

#flatten

data=((2,3),(4,3),(1,5))
# flatten=sum(data,())
# print(flatten)
 
flatt=()
for i in data:
    flatt+=i
    print(flatt)



