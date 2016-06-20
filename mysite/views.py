from django.shortcuts import render_to_response
from mysite.models import Activity,Practice

def stalent(request):
	mysite1 = Activity.objects.all()
	mysite2 = Practice.objects.all()
	mysite = [mysite1,mysite2]
	return render_to_response('index.html',locals())
