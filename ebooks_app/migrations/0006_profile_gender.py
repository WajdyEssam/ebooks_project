# Generated by Django 2.2.3 on 2019-07-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks_app', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
