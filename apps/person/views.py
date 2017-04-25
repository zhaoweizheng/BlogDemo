from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    # all_message = UserMessage.objects.all()
    # for message in all_message:
    #     print(message.name)
    user_message = UserMessage()
    user_message.name = "bobby2"
    user_message.message = "hello"
    user_message.address = "上海"
    user_message.email = "23@s.com"
    user_message.save()
    return  render(request, 'start.html')