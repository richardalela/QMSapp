# Generated by Django 3.2.9 on 2022-02-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLAUSE', models.CharField(max_length=5)),
                ('REQUIREMENT', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AuditStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODE', models.CharField(max_length=1000)),
                ('DESCRIPTION', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_type_of_audit', models.CharField(max_length=100)),
                ('emp_being_audited', models.TextField()),
                ('emp_auditors', models.TextField()),
                ('emp_date_of_audit', models.DateField()),
                ('emp_end_date_of_audit', models.DateField()),
                ('emp_department_being_audited', models.CharField(max_length=100)),
                ('emp_person_being_audited', models.CharField(max_length=100)),
                ('emp_unique_identifier', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMPLIANCE', models.CharField(choices=[('Conformity', 'Conformity'), ('Non-Conformity', 'Non-Conformity')], max_length=100)),
                ('COMMENTS', models.TextField()),
                ('RISK_LEVEL', models.CharField(choices=[('High Risk', 'High Risk'), ('Medium Risk', 'Medium Risk'), ('Low Risk', 'Low Risk')], max_length=100, null=True)),
                ('ATTACH_DOCUMENTS', models.FileField(null=True, upload_to='')),
                ('CLAUSE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auditapp.auditrequirements')),
                ('CODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditapp.auditstandard')),
                ('UNIQUE_IDENTIFIER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditapp.emp')),
            ],
        ),
        migrations.AddField(
            model_name='auditrequirements',
            name='CODE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditapp.auditstandard'),
        ),
    ]