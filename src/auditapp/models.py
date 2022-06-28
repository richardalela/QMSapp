from django.db import models


# Create your models here.


# class ISO(models.Model):
#     four_point_one_yes = models.BooleanField(null=True)
#     four_point_one_no = models.BooleanField(null=True)
#     four_point_one_comments = models.TextField(null=True)
#     four_point_one_risk_level = models.BooleanField(null=True)
#     four_point_one_attach_documents = models.FileField(blank=True)
#     four_point_two_yes = models.BooleanField(null=True)
#     four_point_two_no = models.BooleanField(null=True)
#     four_point_two_comments = models.TextField(null=True)
#     four_point_two_risk_level = models.BooleanField(null=True)
#     four_point_two_attach_documents = models.FileField(blank=True)
#     four_point_three_yes = models.BooleanField(null=True)
#     four_point_three_no = models.BooleanField(null=True)
#     four_point_three_comments = models.TextField(null=True)
#     four_point_three_risk_level = models.BooleanField(null=True)
#     four_point_three_attach_documents = models.FileField(blank=True)
#     four_point_four_point_one_yes = models.BooleanField(null=True)
#     four_point_four_point_one_no = models.BooleanField(null=True)
#     four_point_four_point_one_comments = models.TextField(null=True)
#     four_point_four_point_one_risk_level = models.BooleanField(null=True)
#     four_point_four_point_one_attach_documents = models.FileField(blank=True)
#     four_point_four_point_two_yes = models.BooleanField(null=True)
#     four_point_four_point_two_no = models.BooleanField(null=True)
#     four_point_four_point_two_comments = models.TextField(null=True)
#     four_point_four_point_two_risk_level = models.BooleanField(null=True)
#     four_point_four_point_two_attach_documents = models.FileField(blank=True)

# class ISAGO(models.Model):
#     one_point_one_point_one_yes = models.BooleanField()
#     one_point_one_point_one_no = models.BooleanField()
#     one_point_one_point_one_comments = models.TextField()
#     one_point_one_point_one_attach_documents = models.FileField()
#     one_point_one_point_two_yes = models.BooleanField()
#     one_point_one_point_two_no = models.BooleanField()
#     one_point_one_point_two_comments = models.TextField()
#     one_point_one_point_two_attach_documents = models.FileField()
#     one_point_one_point_three_yes = models.BooleanField()
#     one_point_one_point_three_no = models.BooleanField()
#     one_point_one_point_three_comments = models.TextField()
#     one_point_one_point_three_attach_documents = models.FileField()
#     one_point_one_point_four_yes = models.BooleanField()
#     one_point_one_point_four_no = models.BooleanField()
#     one_point_one_point_four_comments = models.TextField()
#     one_point_one_point_four_attach_documents = models.FileField()
#     one_point_one_point_five_yes = models.BooleanField()
#     one_point_one_point_five_no = models.BooleanField()
#     one_point_one_point_five_comments = models.TextField()
#     one_point_one_point_five_attach_documents = models.FileField()
#     one_point_one_point_six_yes = models.BooleanField()
#     one_point_one_point_six_no = models.BooleanField()
#     one_point_one_point_six_comments = models.TextField()
    # one_point_one_point_six_attach_documents = models.FileField()

class Emp(models.Model):
    emp_type_of_audit = models.CharField(max_length=100)
    emp_being_audited = models.TextField()
    emp_auditors = models.TextField()
    emp_date_of_audit = models.DateField()
    emp_end_date_of_audit = models.DateField()
    emp_department_being_audited = models.CharField(max_length=100)
    emp_person_being_audited = models.CharField(max_length=100)
    emp_unique_identifier = models.CharField(max_length=5, unique=True)
    def __str__(self):
        return self.emp_unique_identifier


class AuditStandard(models.Model):
    CODE = models.CharField(max_length=1000)
    DESCRIPTION = models.CharField(max_length=1000)
    def __str__(self):
        return self.CODE

    

class AuditRequirements(models.Model):
    CODE = models.ForeignKey(AuditStandard, on_delete=models.CASCADE)
    CLAUSE = models.CharField(max_length=5)
    REQUIREMENT = models.TextField()
    
    def __str__(self):
        return "Clause" + " " + self.CLAUSE

class Checklist(models.Model):
    RISK_LEVEL = (
        ('High Risk', 'High Risk'),
        ('Medium Risk', 'Medium Risk'),
        ('Low Risk', 'Low Risk'),
    )
    COMPLIANCE = (
        ('Conformity', 'Conformity'),
        ('Non-Conformity', 'Non-Conformity'),
    )
    UNIQUE_IDENTIFIER = models.ForeignKey(Emp, on_delete=models.CASCADE)
    CODE = models.ForeignKey(AuditStandard, on_delete=models.CASCADE)
    CLAUSE = models.OneToOneField(AuditRequirements, on_delete=models.CASCADE)
    COMPLIANCE = models.CharField(max_length=100, choices=COMPLIANCE)
    COMMENTS = models.TextField()
    RISK_LEVEL = models.CharField(max_length=100, choices=RISK_LEVEL, null=True)
    ATTACH_DOCUMENTS = models.FileField(null=True)

    def __str__(self):
        return self.CLAUSE.CODE.CODE +  " " + "Clause" + " " + self.CLAUSE.CLAUSE + " " + "checklist"


class CRA(models.Model):
    Clause = models.CharField(max_length=15)
    Root_Cause_Analysis = models.TextField()
    Correction = models.TextField()
    Corrective_Action_Plan = models.TextField()





    




    

        

    

