import json, sys, copy

from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response
from django.http.response import HttpResponse

from api.models import Student
from api.serializers import StudentSerializer

from push_notifications.models import APNSDevice, GCMDevice

def sendall(request):
    devices = GCMDevice.objects.all()
    devices.send_message("whatever")
    return HttpResponse("sendall")

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        linestr = request.body.decode('utf8')
        #linestr = linestr[4:]
        #sys.stderr.write("data"+linestr)
        try:
            data = json.loads(linestr)
        except ValueError as e:
            sys.stderr.write("\n\njson load failed")
            return HttpResponse("bad data format", status=status.HTTP_400_BAD_REQUEST)

        try:
            usosid = int(data["usosid"])
            deviceid = data["deviceid"]
        except:
            sys.stderr.write("\n\nparsing failed")
            return Response("bad data format or student not found", status=status.HTTP_400_BAD_REQUEST)
        try:
            Student.objects.get(usosid=usosid).delete()
        except:
            sys.stderr.write("nie ma studenta")
        s = Student(usosid=usosid, deviceid=deviceid)
        s.save()

        #GCM
        reg_key = Student.objects.get(usosid=usosid).deviceid
        #sys.stderr.write("reg key:" + reg_key)
        try:
            GCMDevice.objects.get(registration_id=reg_key).delete()
        except:
            sys.stderr.write("nie bylo device")
        GCMDevice.objects.create(registration_id=reg_key,active=True)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse("no")

def student_list(request):
    """
    List all snippets, or create a new snippet.
    """
    students = Student.objects.all()
    response = "<html><body><table>"
    for student in students:
        response += "<tr><td>"+str(student.usosid)+"</td><td>"+student.deviceid+"</td></tr>"
    response += "</table></body></html>"
    return HttpResponse(response)

def deb(s):
    sys.stderr.write("DEBUG: "+str(s)+"\n")

@api_view(['POST','GET'])
def usos_callback(request):
    if request.method == 'POST':
        deb(request.body)
        data = json.loads(request.body)
	deb(data)
#        deb(data["event_type"])
        for i in data["entry"]:
            ret_ = {"operation": i["operation"], "node_id":i["node_id"],"type":data["event_type"]}
            if data["event_type"] == "grades/grade":
                ret_["grade"] = i["grade"]
            for j in i["related_user_ids"]:
                ret = copy.deepcopy(ret_)
                ret["id"] = j
                deb(j)
                student = Student.objects.get(usosid=int(j))
                deb("DEVICEID:" + student.deviceid)
                device = GCMDevice.objects.get(registration_id=student.deviceid)
		deb(json.dumps(ret))
                device.send_message(json.dumps(ret))
        return HttpResponse()
    elif request.method == 'GET':
        return HttpResponse(request.GET['hub.challenge'])

