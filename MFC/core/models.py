from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name_plural = "People"
        ordering = ("last_name", "first_name")

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.year}"

    class Meta:
        unique_together = ("name", "year", )

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person}, {self.grade}, {self.course}"

class ServiceCategory(models.Model):
    applicant_type = models.TextField()
    name = models.TextField()
    range_of_applicants = models.TextField()
    grounds_for_refusal_to_provide_the_service: models.TextField()
    grounds_for_suspending_the_provision_of_the_service = models.TextField()
    list_of_documents_required_to_provide_the_service = models.TextField()
    reasons_for_refusing_to_accept_documents = models.TextField()
    result_of_providing_the_service = models.TextField()
    url_order = models.TextField()
    order_name = models.TextField()

    def __str__(self):
       return f"{self.name}"

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.TextField()
    service_submission_methods = models.TextField()
    ways_to_get_the_result = models.TextField()
    cost_and_payment_methods = models.TextField()
    terms_of_service_provision = models.TextField()
    url_html_template = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Window(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class EQueue(models.Model):
    window = models.ForeignKey(Window, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now=True, blank=True)
    is_priority = models.BooleanField()
    name = models.TextField()

    def __str__(self):
        return f"e-queue {self.window}"

class RequestType(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class RequestStatus(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Region(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Citizenship(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class NotificationType(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.TextField()
    code = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Passport(models.Model):
    series = models.TextField()
    number = models.TextField()
    issued_by = models.TextField()
    issue_date = models.TextField()
    division_code = models.TextField()
    scan_url = models.TextField()

    def __str__(self):
        return f"{self.series} {self.number}"

class Snils(models.Model):
    insurance_number = models.TextField()
    registration_date = models.TextField()

    def __str__(self):
        return f"{self.insurance_number}"

class Inn(models.Model):
    number = models.TextField()
    assignment_date = models.TextField()

    def __str__(self):
        return f"{self.number}"

class User(models.Model):
    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    last_name = models.TextField()
    first_name = models.TextField()
    patronyc = models.TextField()
    birthday = models.TextField()
    place_of_birth =  models.ForeignKey(City, on_delete=models.CASCADE)
    gender = models.TextField()
    snils = models.ForeignKey(Snils, on_delete=models.CASCADE)
    inn = models.ForeignKey(Inn, on_delete=models.CASCADE)
    is_special_category = models.BooleanField()
    phone = models.TextField()
    registration_date = models.TextField()
    residence_address = models.TextField()
    role = models.TextField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronyc}"
