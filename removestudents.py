from api.models import Student
for i in xrange(10):
	Student.objects.get().delete()
