# Generated by Django 3.1.4 on 2021-01-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_citizenship_city_inn_notificationtype_passport_region_requeststatus_requesttype_snils_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='equeue',
            name='registration_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='inn',
            name='assignment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='inn',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passport',
            name='division_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passport',
            name='issue_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passport',
            name='series',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='requesttype',
            name='name',
            field=models.CharField(choices=[('Консультация', 'Consulation'), ('Выдача документов', 'Issurance of documents'), ('Регистрация заявления', 'Registration of application')], default='Консультация', max_length=30),
        ),
        migrations.AlterField(
            model_name='snils',
            name='insurance_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='snils',
            name='registration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateField(),
        ),
    ]
