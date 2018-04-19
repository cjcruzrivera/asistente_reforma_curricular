# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def index(request):
    usuario = request.user
    return render(request,'index.html' ,{'usuario': usuario})
