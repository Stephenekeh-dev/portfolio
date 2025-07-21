from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ContactView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        # Construct message with sender info
        full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

        send_mail(
            subject=f"Contact Form Message from {name}",
            message=full_message,
            from_email=None,  # or use settings.DEFAULT_FROM_EMAIL
            recipient_list=["stevenadibee@yahoo.com"],
        )
        return Response({"message": "Email sent"}, status=status.HTTP_200_OK)
# Create your views here.
