# Generated by Django 4.2.6 on 2023-11-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=50, null=True)),
                ('cemail', models.CharField(blank=True, max_length=50, null=True)),
                ('cnumber', models.CharField(blank=True, max_length=50, null=True)),
                ('cnationality', models.CharField(blank=True, max_length=50, null=True)),
                ('csubject', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]