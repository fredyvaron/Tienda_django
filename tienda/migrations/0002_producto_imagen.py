# Generated by Django 3.2.1 on 2021-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]