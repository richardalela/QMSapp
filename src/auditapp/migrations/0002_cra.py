# Generated by Django 3.2.9 on 2022-03-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clause', models.TextField()),
                ('Root_Cause_Analysis', models.TextField()),
                ('Correction', models.TextField()),
                ('Corrective_Action_Plan', models.TextField()),
            ],
        ),
    ]
