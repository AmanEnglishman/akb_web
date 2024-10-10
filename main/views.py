from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackAPIView(APIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})