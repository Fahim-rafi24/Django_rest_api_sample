from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Company(models.Model):   # Company Model
    TYPES = [
        ("IT", "IT"),
        ("NON-IT", "Non-IT"),
        ("AGRICULTURAL", "Agricultural"),
        ("LOW-FARM", "Low-Farm"),
        ("PUBLIC-SERVICE", "Public Service"),
        ("GOV.", "Government"),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    total_member = models.IntegerField(default=0)
    company_type = models.CharField(max_length=20, choices=TYPES)

    def __str__(self):
        return self.name



class User(models.Model):   # User Model
    POSITIONS = [
        ("CEO", "CEO"),
        ("CTO", "CTO"),
        ("MANAGER", "Manager"),
        ("MARKETING-TEAM", "Marketing Team"),
        ("TEAM-LEADER", "Team Leader"),
        ("EMPLOYEE", "Employee"),
        ("CUSTOMER-CARE", "Customer Care"),
    ]

    GENDERS = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=100)
    present_location = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDERS)
    about_me = models.TextField(null=True, blank=True)
    # which_company = models.CharField(max_length=100, null=True, blank=True)
    which_company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees"
    )  # Connect to Company model
    position = models.CharField(max_length=20, choices=POSITIONS)
    password = models.CharField(max_length=255)  # Use Django's built-in authentication for hashing passwords
    photos = models.JSONField(default=list, blank=True)  # Store multiple photo URLs

    def __str__(self):
        return self.name



class CompanyTargeted(models.Model):   # CompanyTargeted Model
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="targeted_members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="targeted_company")

    def __str__(self):
        return f"{self.company.name} - {self.user.name}"



class UserUploadPictureInServer(models.Model):   # UserUploadPictureInServer Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_pictures")
    upload_photo = CloudinaryField("image")

    def __str__(self):
        return f"{self.user.name} - {self.upload_photo.url}"