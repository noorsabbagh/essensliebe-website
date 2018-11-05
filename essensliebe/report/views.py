from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime
from .forms import ReportForm
from .models import UserReport
from django import forms
from report.models import UserReport

User = get_user_model()



def report_user(request, user_id, username):
    user = User.objects.get(id=user_id)
    #id=28 admin user
    admin = User.objects.get(id=28)
    form = ReportForm(request.POST or None)
    if form.is_valid():
        report_message = form.save(commit=False)
        report_message.reporter = user
        report_message.receiver = admin
        report_message.report_url = "http://127.0.0.1:8000/profile/" + username
        report_message.sent = datetime.datetime.now()
        report_message.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'report_user.html', locals())


