from django.contrib import admin
from .models import User, Company, CompanyTargeted, UserUploadPictureInServer
# Register your models here.



# Customize UserAdmin to display selected fields in the admin panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'present_location', 'current_location', 'occupation', 'position', 'gender')
    search_fields = ('name', 'present_location', 'current_location', 'occupation', 'position')
    list_filter = ('position', 'gender')
    readonly_fields = ('photos',)  # Prevent editing of photos directly


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'total_member', 'company_type')
    search_fields = ('name', 'location')
    list_filter = ('company_type',)


@admin.register(CompanyTargeted)
class CompanyTargetedAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'user')
    search_fields = ('company__name', 'user__name')
    list_filter = ('company__name',)


@admin.register(UserUploadPictureInServer)
class UserUploadPictureInServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'upload_photo')
    search_fields = ('user__name',)
    readonly_fields = ('upload_photo',)  # Prevent editing of the photo field directly