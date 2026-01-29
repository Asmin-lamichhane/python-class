# from rest_framework import serializers
# class SimpleResponseSerilizer(serializers.Serializer):
#     messages=serializers.CharField()
#     class Meta():
#         fields=['message']

    
from rest_framework import serializers

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     grade=serializers.IntegerField()
#     gpa=serializers.IntegerField()

class PizzaSerializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    size=serializers.CharField()