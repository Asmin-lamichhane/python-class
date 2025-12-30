# # # # def student(name,age=10):
# # # #     # print(f"hello,{name}")
# # # #     name
# # # #     age
# # # #     # return f"good day,{name},age ={age}"
# # # #     return name,age
# # # # print(student())
# # # # # print(student("asmin",20))

# # # # # # print(student("ram",20))
# # # # # # print(student("ahri"))
# # # # # # print(student("sita"))
# # # # # # print(student("gita"))



# # # # # #calc volum of cuboid
# # # # def vol(l,b,h):
# # # #     return l*b*h
# # # # print(vol(20,10,10))


# # # # def rev(lis):
# # # #     return lis[::-1]

# # # # print(rev([1,2,34,4,5]))

# # # def msg():
    
# # #     for i in range(10):
# # #         print("hello")
# # #     return i
# # # print(msg())



# # #recursive function

# def fab(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
    
 
# # n=5   
# # for i in range(n):
# #     print(fab(5))

# #     '''
     
# #     '''
# #sum of natioral number

# # def sum(n):
# #     if n==1:
# #         return n
# #     else:
# #         return (n)+sum(n-1)
    
# # print(sum(5))

# def small(list):
#     if len(list)==1:
#         return list[0]
#     else:
#    #       
    





# #high order function
def Logger(func):
    def wrapper(*args,**kwargs):
        print(*args)
        # print(*args[0])
        result=func(*args,**kwargs)
        print(result)
        # print(res)
        return result
    


    return wrapper

@Logger
def rev(name):
    return name[::-1]
   
rev("asmin")




































































































