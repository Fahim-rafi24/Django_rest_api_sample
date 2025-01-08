
from django.urls import path
from .views import (
    UserListCreateAPIView,
    CompanyListCreateAPIView,
    CompanyTargetedListCreateAPIView,
    UserUploadPictureListCreateAPIView,
)



urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("companies/", CompanyListCreateAPIView.as_view(), name="company-list-create"),
    path("company-targeted/", CompanyTargetedListCreateAPIView.as_view(), name="company-targeted-list-create"),
    path("user-uploads/", UserUploadPictureListCreateAPIView.as_view(), name="user-upload-list-create"),
]
# urlpatterns = [
#     # path('testing/root/', Testing_api, name="testing-api"),
# ]