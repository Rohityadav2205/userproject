# Generated by Django 4.1.2 on 2022-10-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Photos', models.ImageField(upload_to='static/')),
                ('Email_id', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('Date_of_birth', models.DateField(max_length=200)),
            ],
        ),
    ]
