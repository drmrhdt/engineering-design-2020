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
    registration_date = models.DateField(auto_now=True, blank=True)
    is_priority = models.BooleanField()
    name = models.TextField()

    def __str__(self):
        return f"e-queue {self.window}"

class RequestType(models.Model):
    CONSULTATION = "Консультация"
    ISSURANCE_OF_DOCUMENTS = "Выдача документов"
    REGISTRATION_OF_THE_APPLICATION = "Регистрация заявления"

    NAME_CHOICES = [
       (CONSULTATION, 'Consulation'),
       (ISSURANCE_OF_DOCUMENTS, 'Issurance of documents'),
       (REGISTRATION_OF_THE_APPLICATION, 'Registration of application')
    ]

    name = models.CharField(
       max_length = 30,
       choices=NAME_CHOICES,
       default=CONSULTATION
    )

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
    code = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Passport(models.Model):
    series = models.IntegerField()
    number = models.IntegerField()
    issued_by = models.TextField()
    issue_date = models.DateField()
    division_code = models.IntegerField()
    scan_url = models.TextField()

    def __str__(self):
        return f"{self.series} {self.number}"

class Snils(models.Model):
    insurance_number = models.IntegerField()
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.insurance_number}"

class Inn(models.Model):
    number = models.IntegerField()
    assignment_date = models.DateField()

    def __str__(self):
        return f"{self.number}"

class User(models.Model):
    ADMIN = 'Администратор'
    USER =  'Пользователь'
    ROLE_CHOICES = [
       (ADMIN, 'Администратор'),
       (USER, 'Пользователь')
    ]

    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
       (MALE, 'Мужской'),
       (FEMALE, 'Женский')
    ]

    citizenship = models.ForeignKey(Citizenship, on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    last_name = models.TextField()
    first_name = models.TextField()
    patronyc = models.TextField()
    birthday = models.DateField()
    place_of_birth =  models.ForeignKey(City, on_delete=models.CASCADE)
    gender = models.CharField(
       max_length = 30,
       choices = GENDER_CHOICES,
       default = MALE)
    snils = models.ForeignKey(Snils, on_delete=models.CASCADE)
    inn = models.ForeignKey(Inn, on_delete=models.CASCADE)
    is_special_category = models.BooleanField()
    phone = models.TextField()
    registration_date = models.DateField()
    residence_address = models.TextField()
    role = models.CharField(
       max_length = 30,
       choices = ROLE_CHOICES,
       default = USER
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronyc}"
