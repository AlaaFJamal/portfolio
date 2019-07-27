from django.shortcuts import render
from django.http import HttpResponse
from .models import Section
from .forms import SectionForm
# Create your views here.

def home(request):
	context = {
		"title_msg": "Welcome to my Portfolio .. new version",
		"CV_link": "My Resume",
	}
	return render(request, 'home.html', context)

def list_view(request):
	context = {
		"mypage_list": Section.objects.all()
	}
	return render(request, 'list.html', context)

def detail_view(request, section_id):
	context = {
		"section": Section.objects.get(id=section_id)
	}
	return render(request, 'detail.html', context)

def section_create(request):
	form = SectionForm()
	context = {
	"form": form
	}

	return render(request, 'section_form.html', context)