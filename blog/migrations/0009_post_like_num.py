# Generated by Django 2.2.2 on 2020-05-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200509_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_num',
            field=models.IntegerField(default=0),
        ),
    ]
