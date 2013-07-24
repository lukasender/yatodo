from django.http import HttpResponse
from django.views.generic.base import View
#from app.models import Task#, TaskForm

class HomeView(View):
		def get(self, request):
			# <view logic>
			return HttpResponse('Good day to you, kind Sir.')