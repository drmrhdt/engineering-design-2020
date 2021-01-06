from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from core.models import Person, Course, Grade, ServiceCategory, Service, Window, EQueue, Passport, Snils, Inn, User, NotificationType, Citizenship, City, RequestType, RequestStatus, Region, Passport, Snils, Inn


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

class ServiceCategoryResource(resources.ModelResource):

   class Meta:
       model = ServiceCategory

class ServiceCategoryAdmin(ImportExportModelAdmin):
   resource_class = ServiceCategoryResource

class ServiceResource(resources.ModelResource):

   class Meta:
       model = Service

class ServiceAdmin(ImportExportModelAdmin):
   resource_class = ServiceResource

class WindowResource(resources.ModelResource):

   class Meta:
       model = Window

class WindowAdmin(ImportExportModelAdmin):
   resource_class = WindowResource

class EQueueResource(resources.ModelResource):

   class Meta:
       model = EQueue

class EQueueAdmin(ImportExportModelAdmin):
   resource_class = EQueueResource

class UserResource(resources.ModelResource):

   class Meta:
       model = User

class UserAdmin(ImportExportModelAdmin):
   resource_class = UserResource

   list_display = ('last_name','first_name', 'patronyc', 'gender', 'birthday', 'is_special_category', 'passport', 'role')
   search_fields = ('first_name', 'last_name', 'patronyc')

class NotificationTypeResource(resources.ModelResource):

   class Meta:
       model = NotificationType

class NotificationTypeAdmin(ImportExportModelAdmin):
   resource_class = NotificationTypeResource

class CitizenshipResource(resources.ModelResource):

   class Meta:
       model = Citizenship

class CitizenshipAdmin(ImportExportModelAdmin):
   resource_class = CitizenshipResource

class CityResource(resources.ModelResource):

   class Meta:
       model = City

class CityAdmin(ImportExportModelAdmin):
   resource_class = CityResource


class RequestTypeResource(resources.ModelResource):

   class Meta:
       model = RequestType

class RequestTypeAdmin(ImportExportModelAdmin):
   resource_class = RequestTypeResource

class RequestStatusResource(resources.ModelResource):

   class Meta:
       model = RequestStatus

class RequestStatusAdmin(ImportExportModelAdmin):
   resource_class = RequestStatusResource

class RegionResource(resources.ModelResource):

   class Meta:
       model = Region

class RegionAdmin(ImportExportModelAdmin):
   resource_class = RegionResource


class PassportResource(resources.ModelResource):

   class Meta:
       model = Passport

class PassportAdmin(ImportExportModelAdmin):
   resource_class = PassportResource

   search_fields = ('number', 'series')

class SnilsResource(resources.ModelResource):

   class Meta:
       model = Snils

class SnilsAdmin(ImportExportModelAdmin):
   resource_class = SnilsResource

   search_fields = ('insurance_number', 'registration_date')

class InnResource(resources.ModelResource):

   class Meta:
       model = Inn

class InnAdmin(ImportExportModelAdmin):
   resource_class = InnResource

   search_fields = ('number', 'assignment_date')

admin.site.register(Inn, InnAdmin)
admin.site.register(Snils, SnilsAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(RequestStatus, RequestStatusAdmin)
admin.site.register(RequestType, RequestTypeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(NotificationType, NotificationTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(EQueue, EQueueAdmin)
admin.site.register(Window, WindowAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
