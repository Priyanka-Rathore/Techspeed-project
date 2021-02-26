# Generated by Django 3.0.13 on 2021-02-23 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0017_auto_20210222_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_data', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Online_Gd_For_Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gd_topic_name', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_of_paticipate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Online_Gd_For_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_date_time', models.CharField(max_length=500)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Online_Gd_For_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='online_group_discussion',
        ),
    ]