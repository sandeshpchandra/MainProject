# Generated by Django 4.2.6 on 2023-10-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_propertyareadb'),
    ]

    operations = [
        migrations.CreateModel(
            name='selltypedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slname', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
