# Generated by Django 2.2.3 on 2019-07-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0003_section_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='content',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(max_length=30),
        ),
    ]