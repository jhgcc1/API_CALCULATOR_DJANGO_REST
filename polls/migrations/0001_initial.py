# Generated by Django 3.1 on 2020-08-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('var1', models.IntegerField()),
                ('var2', models.IntegerField()),
            ],
        ),
    ]
