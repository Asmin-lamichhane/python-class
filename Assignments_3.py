# #task 1
student_score={
    "asmin":[20,50,60],
    "ram":[40,50,60],
    "hari":[70,80,45]
    
}
#average of asmin
average=sum(student_score["asmin"])/len(student_score["asmin"])
print(average)

if (average>=60):
    print("true")
else:
    print("false")

average=sum(student_score["ram"])/len(student_score["ram"])
print(average)


if (average>=60):
    print("true")
else:
    print("false")

average=sum(student_score["hari"])/len(student_score["hari"])
print(average)

if (average>=60):
    print("true")
else:
    print("false")

#task 2

stock={
    "apple":10,
    "banana":2,
    "orange":0
}
if("pears"in stock):
    print("available")
else:
    print("not available")


if ("banana"in stock and stock["banana"]<5):
    print("time to restock banans !")



#task 3
users={
    "admin":"1234",

}
users["teacher"]="password123"
print(users)

input_user="admin"


input_pass="1234"


if(input_user in users and users[input_user]==input_pass):
    print("access Granted")
else:
    print("try again")
