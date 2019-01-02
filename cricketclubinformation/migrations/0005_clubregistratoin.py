# Generated by Django 2.0.5 on 2019-01-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketclubinformation', '0004_auto_20190102_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubRegistratoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_establishment', models.DateField(blank=True, null=True)),
                ('house_no', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('street', models.CharField(blank=True, max_length=20, null=True)),
                ('thana', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('president_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
