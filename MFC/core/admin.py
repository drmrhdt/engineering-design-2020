from django.contrib import admin

from core.models import Person, Course, Grade, ServiceCategory, Service, Window, EQueue, Passport, Snils, Inn, User, NotificationType, Citizenship, City, RequestType, RequestStatus, Region

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceCategory)
class ServiceCategory(admin.ModelAdmin):
    pass

@admin.register(Service)
class Service(admin.ModelAdmin):
    pass

@admin.register(Window)
class Window(admin.ModelAdmin):
    pass

@admin.register(EQueue)
class EQueue(admin.ModelAdmin):
    pass

@admin.register(User)
class User(admin.ModelAdmin):
    pass

@admin.register(NotificationType)
class NotificationType(admin.ModelAdmin):
    pass

@admin.register(Citizenship)
class Citizenship(admin.ModelAdmin):
    pass

@admin.register(City)
class City(admin.ModelAdmin):
    pass

@admin.register(RequestType)
class RequestType(admin.ModelAdmin):
    pass

@admin.register(RequestStatus)
class RequestStatus(admin.ModelAdmin):
    pass

@admin.register(Region)
class Region(admin.ModelAdmin):
    pass

