from django.http import HttpResponse
from django.shortcuts import render, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import datetime
import re


def index(request):
    return render(request, 'index.html')

