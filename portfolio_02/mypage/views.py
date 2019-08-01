from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Section
from .forms import SectionForm
# Create your views here.

def home(request):
	context = {
		"title_msg": "Welcome to my Portfolio ..",
		"CV_link": "My Resume",
		"CV_link2": "My CV",
		"Media": "Media",
	}
	return render(request, 'home.html', context)

def resume(request):
	context = {
		"CV_link2": "My CV",
	}
	return render(request, 'resume.html', context)
	
def list_view(request):
	context = {
		"mypage_list": Section.objects.all(),
		"CV": "Resume",
	}
	return render(request, 'list.html', context)

def detail_view(request, section_id):
	context = {
		"section": Section.objects.get(id=section_id)
	}
	return render(request, 'detail.html', context)

def section_create(request):
	form = SectionForm()
	if request.method == "POST":
		form = SectionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("sections")
	context = {
	"form": form
	}

	return render(request, 'section_form.html', context)