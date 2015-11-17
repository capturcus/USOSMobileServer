import json, sys

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.http.response import HttpResponse

from api.models import Student
from api.serializers import StudentSerializer

from push_notifications.models import APNSDevice, GCMDevice

@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        #
        if(request.GET['send'] == "T"):
            device = GCMDevice.objects.get(registration_id=Student.objects.first().deviceid)
            #device = GCMDevice.objects.get(registration_id="APA91bH05csgC0JNu8z3k3LKFlJiqDhjr8Q3Hy98NdK0ZonrXpvwMBqT1F_fdmJBhXNvVXN7ID4UnNRL9XvEJUgHFnMAKKe8Dx4jWq47oEPsB8okxNTgK2FihKMeonpv6qm9wgjUqmwa")
            sys.stderr.write("\ndevice reg id:" + device.registration_id)
            device.send_message("USOS Bitch!")
        #
        return HttpResponse(serializer.data)

    elif request.method == 'POST':
        linestr = request.body.decode('utf8')
        linestr = linestr[4:]
	sys.stderr.write("data"+linestr)
        try:
            data = json.loads(linestr)
        except ValueError as e:
            return HttpResponse("bad data format", status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            #GCM
            reg_key = Student.objects.first().deviceid
            sys.stderr.write("reg key:" + reg_key)
            GCMDevice.objects.create(
                registration_id=reg_key,
                active=True
            )
            #

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
