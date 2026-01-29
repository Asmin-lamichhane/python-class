from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import PizzaSerializer
from .random_class import Pizza
# # class SimpleResponseView(APIView):
# #     def get(self,request):
# #         data={
# #             'message':'hello world'
# #         }
        

# #         serilizer=SimpleResponseSerilizer(data=data)
# #         serilizer.is_valid(raise_exception=True)
# #         return Response(serilizer.data)
        
# class SimpleResponseView(APIView):
#     def get(self, request):
#         data = {
#             'messages': 'hello world'
#         }

#         serializer = SimpleResponseSerilizer(data=data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)

# @api_view("GET","POST") 
#creat a class name with stusent
# @api_view(['GET'])
# def display_student_data(request):
#     first_student =Student("asmin",10,3)
#     #validate data
#     # serializer.is_valid(raise_exception)
#     serializer=StudentSerializer(first_student)
#     return Response(serializer.data)

@api_view(['GET'])
def Display_Pizza(request):
    pizza1=Pizza("abc",100,"medium")
    serializer=PizzaSerializer(pizza1)
    return Response(serializer.data)

@api_view(["POST"])
def creat_data(request):
    serializer=PizzaSerializer(data=request.data,many=True)
    if serializer.is_valid():
        print(serializer.validated_data)
        container=[]
        for data in serializer.validated_data:
            instance=Pizza(data['name'],data['price'],data['size'])
            

            