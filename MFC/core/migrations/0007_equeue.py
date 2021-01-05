# Generated by Django 3.1.4 on 2021-01-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_window_name1'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now=True)),
                ('is_priority', models.BooleanField()),
                ('window', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.window')),
            ],
        ),
    ]