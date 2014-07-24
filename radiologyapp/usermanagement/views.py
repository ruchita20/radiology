# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from forms import signupform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from usermanagement.models import *
from django.core.mail import send_mail, BadHeaderError

from django.template import loader, RequestContext
from django.contrib import auth

from usermanagement.models import *


def home(request):
	return render_to_response("home.html")


def login(request):
	return render_to_response("login.html")

