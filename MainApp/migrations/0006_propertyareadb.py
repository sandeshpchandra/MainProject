# Generated by Django 4.2.6 on 2023-10-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_rename_propertytype_propertytypedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='propertyareadb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paname', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
