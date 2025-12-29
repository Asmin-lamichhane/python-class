# empty={}
# print(empty)
# print(type(empty))

# dic={
#     'name':"asmin",
#     'age':23
# }
# print(dic.values())
# print(dic.keys())

# dic1={
#     "name":"asmin",
#     ("age"):23
# }
# # print(dic1.items())
# # for key,value in dic1.items():
# #     print(key)
# #     print(value)
# name=dic["name"]
# print(name)
# name=dic1.get("asm")
# print(name)

# #utility of dic

dic_1={"name":"astd",'class':26}
dic_2={'age':26,"name":"ased"}

# print(dic_1==dic_2)
# print(id(dic_1))
# print(dic_1 is dic_2)
# print(id(dic_2))


# #merge
# re=dic_2 | dic_1
# print(re)
# print(id(re))

# dic_1.update(dic_2)
# print(dic_1)
# print(id(dic_1))

#keyword argument
res={**dic_2,**dic_2}
print(res)

#removing key value pair
dic_3 = {'name ': 'asmin', 'age':26,"id":55}
value = dic_3.popitem()
print(value)
print(dic_3)