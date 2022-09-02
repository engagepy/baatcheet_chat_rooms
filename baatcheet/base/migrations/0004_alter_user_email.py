# Generated by Django 4.0.5 on 2022-09-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True, verbose_name='Email'),
        ),
    ]
