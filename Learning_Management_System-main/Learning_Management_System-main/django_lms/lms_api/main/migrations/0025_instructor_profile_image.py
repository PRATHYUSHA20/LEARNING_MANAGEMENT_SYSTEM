# Generated by Django 4.1.7 on 2023-04-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_studentcourseenrollment_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='instructor_profile_imgs/'),
        ),
    ]
