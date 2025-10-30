from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Todos
from rest_framework import status
from .serializer import TodoSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '' : 'all api Overview to execute',
        'create/' : 'to create a todo',
        'all/' : 'to get all the todos',
        'get/<int:pk>' : 'to get a single todo',
        'update/<int:pk>' : 'to update a todo',
        'delete/<int:pk>' : 'to delete a todo',
    }
    return Response(api_urls,status=status.HTTP_200_OK)

@api_view(['POST'])
def createTodo(request):
    if Todos.objects.all().filter(title=request.data['title']):
        return Response({'error':'Todo already exists'},status=status.HTTP_400_BAD_REQUEST)
    else:
        todo = Todos(**request.data)
        todo.save()

    return Response(request.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getTodos(request):
    todo = Todos.objects.all().order_by('completed')
    serializer = TodoSerializer(todo,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def getSingleTodo(request,pk):
    try:
        todo = Todos.objects.all().get(id=pk)
        serializer = TodoSerializer(todo,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateTodo(request,pk):
    try:
        todo = Todos.objects.all().get(id=pk)
        serializer = TodoSerializer(instance = todo ,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteTodo(request,pk):
    try:
        todo = Todos.objects.all().get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)