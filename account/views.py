from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
import datetime

from .models import UserProfile
class RegisterView(GenericAPIView):
  permission_classes = (permissions.AllowAny,)

  def post(self, request, *args, **kwargs):
    try:
      email = request.data.get('email')
      questions = request.data.get('questions')
      qs = UserProfile.objects.filter(email=email)
      if qs.exists():
        qs.update(last_activity = datetime.datetime.now(), email_sent = False)
      else:
        UserProfile.objects.create(email=email, questions = questions, last_activity = datetime.datetime.now(),email_sent=False)
      return Response({"Status": "True"})
    except Exception as e:
      raise e