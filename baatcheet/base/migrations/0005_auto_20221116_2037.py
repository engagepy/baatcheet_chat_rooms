# Generated by Django 3.2.7 on 2022-11-16 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='images/avatar.svg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(default='I wonder', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=35, unique=True),
        ),
    ]
