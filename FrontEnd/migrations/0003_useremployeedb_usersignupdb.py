# Generated by Django 4.2.6 on 2023-11-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0002_contactdb_cmessage_alter_contactdb_csubject'),
    ]

    operations = [
        migrations.CreateModel(
            name='useremployeedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('unumber', models.CharField(blank=True, max_length=50, null=True)),
                ('uemail', models.CharField(blank=True, max_length=50, null=True)),
                ('uusername', models.CharField(blank=True, max_length=50, null=True)),
                ('upassword', models.CharField(blank=True, max_length=50, null=True)),
                ('confirmpass', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usersignupdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('unumber', models.CharField(blank=True, max_length=50, null=True)),
                ('uemail', models.CharField(blank=True, max_length=50, null=True)),
                ('uusername', models.CharField(blank=True, max_length=50, null=True)),
                ('upassword', models.CharField(blank=True, max_length=50, null=True)),
                ('confirmpass', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
