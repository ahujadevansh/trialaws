# Generated by Django 2.2.4 on 2019-09-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0010_auto_20190909_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='Activities',
            field=models.ManyToManyField(to='cities.Activities'),
        ),
    ]
