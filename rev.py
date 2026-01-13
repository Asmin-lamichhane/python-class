# #highorder function

# def Calc(funct):
#     def Wrapper(*args,**kwargs):
#         print(f"{funct.__name__} {args}")
#         result=funct(*args,**kwargs)
#         print(result)

#     return Wrapper
    
# # @Calc
# # def Add(a,b):
# #     return a+b
# # @Calc
# # def Sub(a,b):
# #     return a-b

# # Add(20,10)

# # Sub(20,10)

# @Calc
# def ope(a,b,operation):
#     if operation == "add":
#         return a+b
#     elif operation == "sub":
#         return a-b

# ope(20,10,"add")
# ope(20,10,"sub")


# def rev_dup(funct):
#     def wrapper(*args,**kwargs):
#         print(*args)
#         sets=set(*args)
#         print(sets)
#         result=funct(args,**kwargs)
#         print(result)
#     return wrapper
# @rev_dup
# def maximum(list):
    
#     return max(list)

# maximum([20,10,30,47,88,20,30])




# names=["asmin","ram","hari","samir","asdbhhjfd"]
# print(type(names))

# fil=filter(lambda name :len(name)<5,names  )
# print(type(fil))
# print(list(fil))


sets={2,12,5,36,4,7,66,8,9,10}

result=map(lambda x : x,sorted(sets))
print(list(result))

