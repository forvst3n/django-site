# Generated by Django 3.2.4 on 2022-05-17 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220516_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpu',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2022, 5, 17, 20, 50, 39, 30450)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=350)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2022, 5, 17, 20, 50, 39, 31452))),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.gpu')),
            ],
        ),
    ]