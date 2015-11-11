import json

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.http.response import HttpResponse

from api.models import Student
from api.serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return HttpResponse(serializer.data)

    elif request.method == 'POST':
        linestr = request.body.decode('utf8')
        data = json.loads(linestr)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
