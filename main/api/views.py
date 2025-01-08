from rest_framework import generics
from .models import User, Company, CompanyTargeted, UserUploadPictureInServer
from .serializers import (
    UserSerializer,
    CompanySerializer,
    CompanyTargetedSerializer,
    UserUploadPictureInServerSerializer,
)
from django.shortcuts import render, redirect
from .forms import UserUploadPictureForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def upload_picture(request):
    if request.method == 'POST':
        form = UserUploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your desired success URL
    else:
        form = UserUploadPictureForm()
    return render(request, 'upload_picture.html', {'form': form})



class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyTargetedListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompanyTargeted.objects.all()
    serializer_class = CompanyTargetedSerializer


# class UserUploadPictureListCreateAPIView(generics.ListCreateAPIView):
    # queryset = UserUploadPictureInServer.objects.all()
    # serializer_class = UserUploadPictureInServerSerializer


class UserUploadPictureListCreateAPIView(APIView):
    def post(self, request):
        serializer = UserUploadPictureInServerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)