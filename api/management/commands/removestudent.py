from api.models import Student
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		Student.objects.get().delete()
