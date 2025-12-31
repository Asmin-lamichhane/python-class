# # # # # # # # # # def student(name,age=10):
# # # # # # # # # #     # print(f"hello,{name}")
# # # # # # # # # #     name
# # # # # # # # # #     age
# # # # # # # # # #     # return f"good day,{name},age ={age}"
# # # # # # # # # #     return name,age
# # # # # # # # # # print(student())
# # # # # # # # # # # print(student("asmin",20))

# # # # # # # # # # # # print(student("ram",20))
# # # # # # # # # # # # print(student("ahri"))
# # # # # # # # # # # # print(student("sita"))
# # # # # # # # # # # # print(student("gita"))



# # # # # # # # # # # #calc volum of cuboid
# # # # # # # # # # def vol(l,b,h):
# # # # # # # # # #     return l*b*h
# # # # # # # # # # print(vol(20,10,10))


# # # # # # # # # # def rev(lis):
# # # # # # # # # #     return lis[::-1]

# # # # # # # # # # print(rev([1,2,34,4,5]))

# # # # # # # # # def msg():
    
# # # # # # # # #     for i in range(10):
# # # # # # # # #         print("hello")
# # # # # # # # #     return i
# # # # # # # # # print(msg())



# # # # # # # # #recursive function

# # # # # # # def fab(n):
# # # # # # #     if(n==0):
# # # # # # #         return 0
# # # # # # #     elif(n==1):
# # # # # # #         return 1
# # # # # # #     else:
# # # # # # #         return fab(n-1)+fab(n-2)
    
 
# # # # # # # # n=5   
# # # # # # # # for i in range(n):
# # # # # # # #     print(fab(5))

# # # # # # # #     '''
     
# # # # # # # #     '''
# # # # # # # #sum of natioral number

# # # # # # # # def sum(n):
# # # # # # # #     if n==1:
# # # # # # # #         return n
# # # # # # # #     else:
# # # # # # # #         return (n)+sum(n-1)
    
# # # # # # # # print(sum(5))

# # # # # # # def small(list):
# # # # # # #     if len(list)==1:
# # # # # # #         return list[0]
# # # # # # #     else:
# # # # # # #    #       
    





# # # # # # #high order function
# # # # # def Logger(func):
# # # # #     def wrapper(*args,**kwargs):
# # # # #         print(*args)
# # # # #         print(args[0][0])
# # # # #         result=func(*args,**kwargs)
# # # # #         print(result)
# # # # #         print(result[0])
# # # # #         return result
    


# # # # #     return wrapper

# # # # # @Logger
# # # # # def rev(name):
# # # # #     return name[::-1]
   
# # # # # rev("asmin")


# # # # # # def multiplier(factor):
# # # # # #     def multiply_by_factor(number):
# # # # # #         return number * factor 
# # # # # #     return multiply_by_factor

# # # # # # multiplier_value= multiplier(5)

# # # # # # # print(multiplier_value.__name__)
# # # # # # # print(type(multiplier_value))
# # # # # # # Result = multiplier_value(10)
# # # # # # # print(Result)
# # # # # # def greeting(name):

# # # # # #     def message():
# # # # # #         return "Hello " + name

# # # # # #     return message()

# # # # # # print(greeting("Asmin"))


# # # # # #calc
# # # # # def calc(func):
# # # # #     def wrapper(*args,**kwargs):
# # # # #         calculate=func(*args,**kwargs)
# # # # #         print(f"{func.__name__} of {args} is {calculate}")
# # # # #         return calculate
# # # # #     return wrapper

# # # # # @calc
# # # # # def add (x,y):
# # # # #     return x+y 
# # # # # @calc
# # # # # def sub(x,y):
# # # # #     return x-y
# # # # # @calc
# # # # # def mul(x,y):
# # # # #     return x*y
# # # # # add(10,2)
# # # # # sub(10,20)
# # # # # mul(20,15)





# # # # #build in high order function  map filter reduce

# # # # # def sq(num):
# # # # #     return num**2

# # # # # number=[1,2,3,4,5,6]

# # # # # squ=map(sq,number)

# # # # # print(list(squ))

# # # # def div(num):
# # # #     if (num%2==0):
# # # #         return True
# # # #     else:
# # # #         return False
    
# # # # numbers=[1,2,3,4,5,6]

# # # # di=map(div,numbers)
# # # # print(list(di))


# # # # a="asmin"
# # # # print(a.upper())

# # # def upp(str):
# # #     return str.upper()

# # # a=["as","assd","sdhsd"]
# # # uppe=map(upp,a)
# # # print(list(uppe))


# # def summ(sublist):
# #     if sum (sublist)>10:
# #         return True
# #     else:
# #         return False

# # nested_list=[[1,2,3],[4,5],[6,7,8,9]]

# # lists=map(summ,nested_list)
# # print(list(lists))

# #filter function

# # def is_even(num):
# #     return num%2==0

# # number=[1,2,3,4,5,6,7,8,9]

# # even_num=filter(is_even,number)
# # print(list(even_num))



# # def word(str):
# #     return len(str)<=3
# # words=["as","asm","asmin","asa","asdfr"]

# # fil=filter(word,words)
# # print(list(fil))
# #filter return either true or false

# def dic(item):
#     return len(item["name"])<=3


# dicti=[
#    { "name":"asmin","age":20},
#     {"name":"ramm","age":25},
#    { "name":"har","age":22},
#    { "name":"as","age":55}

# ]
# rem=filter(dic,dicti)
# print(list(rem))

#reduce function
from functools import reduce

# def add(x,y):
#     return x+y
# num=[1,2,3,4,5,6,7]

# sum=reduce(add,num)
# print(sum)
def max(x,y):
    if (x>y):
        return x
    else:
        return y

num=[1,2,3,4,5,6,7,12]

max_num=reduce(max,num)
print(max_num)
