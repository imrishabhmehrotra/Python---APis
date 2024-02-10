from rest_framework import serializers
from rest_framework.decorators import api_view

from .models import Greeting
from .serializers import GreetingSerializer
@api_view(['GET'])
def greet(request):
    
    greeting = Greeting(message='Ahoy, World!')
    serializer = GreetingSerializer(greeting)
    
    return Response(serializer.data)
        