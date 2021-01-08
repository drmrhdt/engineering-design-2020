# Generated by Django 3.1.4 on 2021-01-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210107_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('STATUS_1', 'В обработке'), ('STATUS_2', 'Завершено'), ('STATUS_3', 'Ошибка')], default='STATUS_1', max_length=30),
        ),
    ]