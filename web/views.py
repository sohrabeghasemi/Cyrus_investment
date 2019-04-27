from django.shortcuts import render, get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
	user = User
	context = {
		'user': user,
		'request': request
	}
	return render(request, 'index.html', context)


@login_required
def web(request):
	kargar_num = models.kagar_cyrus.objects.count()
	kargar_q = models.kagar_cyrus.objects.order_by('created')
	context = {
		'kargars': kargar_q,
		'kargarcount': kargar_num
	}
	return render(request, 'web.html', context)


@login_required
def kargar_detail(request, kargar_id):
	kargar_detail_list =get_object_or_404(models.kagar_cyrus, pk=kargar_id)
	context = {
		'kargar_pick': kargar_detail_list,
	}
	return render(request, 'kargar_detail.html', context)


def project_list(request):
	p_count = models.project_cyrus.objects.count()
	p_list = models.project_cyrus.objects.all()
	context = {
		'p_count': p_count,
		'p_list': p_list,
	}

	return render(request, 'project_cyrus_list.html', context)


def kargar_input_form(request):



	form = forms.kargar_input_form()
	context = {
		'form': form
	}
	return render(request, 'kargar_input_form.html', context)

