# Generated by Django 4.2.6 on 2023-10-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_propertydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='propertytype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptname', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
