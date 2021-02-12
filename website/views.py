from django.http import HttpResponse
from django.shortcuts import render, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from datetime import datetime
import re
from formdetails.models import studentdetails


def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        school = request.POST.get('school', '')
        board = request.POST.get('board', '')
        standard = request.POST.get('standard', '')
        address = request.POST.get('address', '')
        category = request.POST.get('category', '')
        number = request.POST.get('number', '')
        registerdate = datetime.now()
        data = studentdetails(name=name, number=number, school=school,
                              board=board, standard=standard, address=address, category=category, registerdate=registerdate)
        data.save()
        print(name)
        feedbackupdate = [
            {'text': 'Your response has been recieved!'}]
        response = json.dumps(feedbackupdate, default=str)
        return HttpResponse(response)
    return render(request, 'index.html')
