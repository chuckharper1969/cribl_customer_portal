# Generated by Django 4.2.4 on 2023-08-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elastic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elasticdestination',
            name='message',
            field=models.CharField(default='Waiting to be onboarded', max_length=128),
        ),
        migrations.AlterField(
            model_name='elasticdestinationupdate',
            name='message',
            field=models.CharField(default='Waiting to be onboarded', max_length=128),
        ),
    ]
