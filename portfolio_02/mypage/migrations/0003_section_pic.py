# Generated by Django 2.2.3 on 2019-07-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_auto_20190727_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]