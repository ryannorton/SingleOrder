from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from app.models import Meal, Order, Item

def index(request):
	messages.get_messages(request).used = True
	return render(request, 'index.html')

def joinmeal(request):
	try:
		group = request.POST['group']
		meal = Meal.objects.get(group=group)
		return HttpResponseRedirect('/meal/'+group)
	except:
		messages.add_message(request, messages.INFO, "Oops! This meal doesn't exist!>")	
		return HttpResponseRedirect('/')

def createmeal(request):
	group = request.POST['group']
	if group == '':
		messages.add_message(request, messages.INFO, "Invalid name. Please try again.")
		return HttpResponseRedirect('/')
	
	elif Meal.objects.filter(group=group).exists():
		messages.add_message(request, messages.INFO, "Already exists!")
		return HttpResponseRedirect('/')
	
	else:
		# success
		new_meal = Meal(group=group, restaurant="Ryan's Gourmet Hotdogs")
		new_meal.save()
		return HttpResponseRedirect('/meal/'+group)

def meal(request, group):
	meal = Meal.objects.get(group=group)
	return render(request, 'meal.html', {
		'meal': meal,
	})
