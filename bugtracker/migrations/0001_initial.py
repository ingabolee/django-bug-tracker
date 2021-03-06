# Generated by Django 3.2 on 2021-04-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('bug_id', models.AutoField(primary_key=True, serialize=False)),
                ('bug_type', models.CharField(max_length=100)),
                ('bug_description', models.TextField()),
                ('company_affected', models.CharField(max_length=50)),
                ('domains_affected', models.TextField()),
                ('date_of_capture', models.DateTimeField()),
                ('resolved', models.BooleanField(default=False)),
            ],
        ),
    ]
