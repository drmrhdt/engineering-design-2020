# Generated by Django 3.1.4 on 2021-01-05 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_equeue_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('assignment_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.TextField()),
                ('number', models.TextField()),
                ('issued_by', models.TextField()),
                ('issue_date', models.TextField()),
                ('division_code', models.TextField()),
                ('scan_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Snils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_number', models.TextField()),
                ('registration_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('patronyc', models.TextField()),
                ('birthday', models.TextField()),
                ('gender', models.TextField()),
                ('is_special_category', models.BooleanField()),
                ('phone', models.TextField()),
                ('registration_date', models.TextField()),
                ('residence_address', models.TextField()),
                ('role', models.TextField()),
                ('citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.citizenship')),
                ('inn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inn')),
                ('notification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.notificationtype')),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.passport')),
                ('place_of_birth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('snils', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.snils')),
            ],
        ),
    ]
