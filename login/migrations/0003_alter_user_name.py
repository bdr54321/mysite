# Generated by Django 3.2.3 on 2021-05-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
