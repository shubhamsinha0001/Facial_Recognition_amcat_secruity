# Generated by Django 2.0.6 on 2019-02-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amcat_login_with_face_traker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('course', models.CharField(choices=[('btech', 'B-Tech'), ('bcom', 'B-Com'), ('mba', 'MBA')], default='btech', max_length=3)),
            ],
        ),
    ]
