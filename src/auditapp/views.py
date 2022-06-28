from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateUserForm, CreateAuditStandardForm, CreateAuditRequirementsForm, CreateChecklistForm, CRAForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Emp,AuditStandard, AuditRequirements, Checklist
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.views import View
from .forms import EmailForm

# from django.core.files.storage import FileSystemStorage
# from simpleDjangoProject.settings import EMAIL_HOST_USER
# from settings import EMAIL_HOST_USER
from projectt import settings
from projectt.settings import EMAIL_HOST_USER
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("User:", user)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def createView(request):
    return render(request, 'create.html')


def store(request):
    emp = Emp()
    print(request)
    emp.emp_type_of_audit = request.POST.get('emp_type_of_audit')
    emp.emp_being_audited = request.POST.get('emp_being_audited')
    emp.emp_auditors = request.POST.get('emp_auditors')
    emp.emp_date_of_audit = request.POST.get('emp_date_of_audit')
    emp.emp_department_being_audited = request.POST.get('emp_department_being_audited')
    emp.emp_person_being_audited = request.POST.get('emp_person_being_audited')
    emp.emp_end_date_of_audit = request.POST.get('emp_end_date_of_audit')
    emp.emp_unique_identifier = request.POST.get('emp_unique_identifier')


    emp.save()
    messages.success(request, "Audit Added Successfully")
    return redirect('/create')


def index(request):
    emp = Emp.objects.all()
    return render(request, 'index.html', {'emp': emp})


def viewEmp(request, pk):
    emp = Emp.objects.get(id=pk)
    return render(request, 'view.html', {'emp': emp})


def deleteEmp(request, pk):
    emp = Emp.objects.get(id=pk)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('create')


def updateView(request, pk):
    emp = Emp.objects.get(id=pk)
    return render(request, 'update.html', {'emp': emp})


def update(request, pk):
    emp = Emp.objects.get(id=pk)
    emp.emp_type_of_audit = request.POST.get('emp_type_of_audit')
    emp.emp_being_audited = request.POST.get('emp_being_audited')
    emp.emp_auditors = request.POST.get('emp_auditors')
    emp.emp_date_of_audit = request.POST.get('emp_date_of_audit')
    emp.emp_department_being_audited = request.POST.get('emp_department_being_audited')
    emp.emp_person_being_audited = request.POST.get('emp_person_being_audited')
    emp.emp_end_date_of_audit = request.POST.get('emp_end_date_of_audit')
    emp.save()
    messages.success(request, "Audit Update Successfully")
    return redirect('data')

def landing(request):
    return render(request, 'main.html')

def choose(request):
    return render(request, 'choose.html')

def isago(request):
    return render(request, 'isago.html')

def iso(request):
    iso = ISO()
    iso.four_point_one_yes = request.POST.get('four_point_one_yes')
    iso.four_point_one_no = request.POST.get('four_point_one_no')
    iso.four_point_one_comments = request.POST.get('four_point_one_comments')
    iso.four_point_one_attach_documents = request.POST.get('four_point_one_attach_documents')
    iso.four_point_two_yes = request.POST.get('four_point_two_yes')
    iso.four_point_two_no = request.POST.get('four_point_two_no')
    iso.four_point_two_comments = request.POST.get('four_point_two_comments')
    iso.four_point_two_attach_documents = request.POST.get('four_point_two_attach_documents')
    iso.four_point_three_yes = request.POST.get('four_point_three_yes')
    iso.four_point_three_no = request.POST.get('four_point_three_no')
    iso.four_point_three_comments = request.POST.get('four_point_three_comments')
    iso.four_point_three_attach_documents = request.POST.get('four_point_three_attach_documents')
    iso.four_point_four_point_one_yes = request.POST.get('four_point_four_point_one_yes')
    iso.four_point_four_point_one_no = request.POST.get('four_point_four_point_one_no')
    iso.four_point_four_point_one_comments = request.POST.get('four_point_four_point_one_comments')
    iso.four_point_four_point_one_attach_documents = request.POST.get('four_point_four_point_one_attach_documents')
    iso.four_point_four_point_two_yes = request.POST.get('four_point_four_point_two_yes')
    iso.four_point_four_point_two_no = request.POST.get('four_point_four_point_two_no')
    iso.four_point_four_point_two_comments = request.POST.get('four_point_four_point_two_comments')
    iso.four_point_four_point_two_attach_documents = request.POST.get('four_point_four_point_two_attach_documents')
    iso.save()
    #return redirect('/create')
    return render(request, 'iso.html')

def multistep(request):
    auditstandard = AuditStandard.objects.all()
    auditrequirements = AuditRequirements.objects.all()
    context = {'auditstandard':auditstandard, 'auditrequirements':auditrequirements}
    return render(request, 'multistepform.html')

# def report(request, pk):
    # isos = ISO.objects.all()
    # emps = Emp.objects.all()
    # total_yess = (isos.filter(four_point_one_yes='True').count()+isos.filter(four_point_two_yes='True').count()+isos.filter(four_point_three_yes='True').count()+isos.filter(four_point_four_point_one_yes='True').count()+isos.filter(four_point_four_point_two_yes='True').count())
    # total_noo = (isos.filter(four_point_one_no='False').count()+isos.filter(four_point_two_no='False').count()+isos.filter(four_point_three_no='False').count()+isos.filter(four_point_four_point_one_no='False').count()+isos.filter(four_point_four_point_two_no='False').count())
    # checklist = Checklist.objects.get(id=pk)
    # total_conformities = checklist.COMPLIANCE.count()
    # total_conformities = Checklist.objects.filter(COMPLIANCE='Conformity').count()
    # total_nonconformities = Checklist.objects.filter(COMPLIANCE='Non-Conformity').count()
    # context={'checklist':checklist, 'total_conformities':total_conformities, 'total_nonconformities': total_nonconformities}
    
    # return render(request, 'report.html', context)


def createAuditStandard(request):
    form = CreateAuditStandardForm()
    if request.method == 'POST':
        form = CreateAuditStandardForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'createaudit.html', context)

def updateAuditStandard(request, pk):
    auditstandard = AuditStandard.objects.get(id=pk)
    form = CreateAuditStandardForm(instance=auditstandard)
    
    if request.method == 'POST':
        form = CreateAuditStandardForm(request.POST, instance=auditstandard)
        if form.is_valid():
            form.save()
            return redirect('dataa')
    
    context = {'form':form}
    return render(request, 'createaudit.html', context)

def createAuditRequirements(request):
    formm = CreateAuditRequirementsForm()
    if request.method == 'POST':
        formm = CreateAuditRequirementsForm(request.POST)
        if formm.is_valid():
            formm.save()
            return redirect('createaudit2')
    context = {'formm':formm}
    return render(request, 'createaudit2.html', context)


def indexx(request):
    title = AuditStandard.objects.all()
    return render(request, 'indexx.html', {'title': title})

# def viewaudit(request, pk):
#     checklist = Checklist.objects.all()
#     audit = AuditStandard.objects.get(id=pk)
#     # audittt = AuditRequirements.objects.all()
#     # audittt = AuditRequirements.objects.get(id=pk)
#     checklists = audit.auditrequirements_set.all()
#     titles = audit.CODE + " " + "Clause" + audittt.CLAUSE
#     context = {'audit':audit, 'checklists':checklists, 'checklist':checklist, 'titles':titles}
#     return render(request, 'vieww.html', context)

def viewaudit(request, pk):
    audits = AuditStandard.objects.get(id=pk)
    things = audits.auditrequirements_set.all()
    checklist_details = audits.checklist_set.all()
    form = CreateChecklistForm()
    if request.method == 'POST':
        form = CreateChecklistForm(request.POST, request.FILES)
        print("Files:", request.FILES)
        if form.is_valid():
            form.save()
    form = CreateChecklistForm() 
        #else:
        #    print(form.errors)
        #    print(form)    
    context  = {'audits':audits, 'things':things, 'form':form, 'checklist_details':checklist_details}
    return render(request, 'cheki.html', context)

def CRA(request):
    form = CRAForm()
    if request.method == 'POST':
        form = CRAForm(request.POST)
        if form.is_valid():
            form.save()
    form = CRAForm()

    context = {'form': form}
    return render(request, 'cra.html', context)


def gotochecklist(request, pk):
    audits = AuditRequirements.objects.get(id=pk)
    # things = audits.auditrequirements_set.all()
    form = CreateChecklistForm()
    if request.method == 'POST':
        form = CreateChecklistForm(request.POST)
        if form.is_valid():
            form.save()
    context  = {'audits':audits, 'form':form}
    return render(request, 'chekii.html', context)

# def dothechecklist(request):
#     form = CreateChecklistForm()
#     if request.method == 'POST':
#         form = CreateChecklistForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'chekii.html', context)

def report(request, pk):
    # auditstandard = AuditStandard.objects.get(id=pk)
    # checklist_details = auditstandard.checklist_set.all()
    emps = Emp.objects.all()
    emp1 = Emp.objects.get(id=pk)
    chklist1 = Checklist.objects.filter(UNIQUE_IDENTIFIER=emp1)
    # chklist2 = Checklist.objects.all()
    pdfid=1
    
    

    # nonconformity_objects = checklist_details.filter(COMPLIANCE='Non-Conformity')
    nonconformity_objects = chklist1.filter(COMPLIANCE='Non-Conformity')
    
    # print(emp1.emp_person_being_audited)
    # print(nonconformity_objects)
    print(emp1.id)
        
    conformity_objects = chklist1.filter(COMPLIANCE='Conformity')
    # nonconformity_objects1 = chklist1.filter(COMPLIANCE='Non-Conformity').count()

    # print("emp1", emp1.emp_unique_identifier)
    # print(nonconformity_objects1)

    # print("chk2",chklist2)
    # cnt1=0
    # cnt2=0
    # chk3 = []
    # for i in chklist2:
        
    #     print("I:",i.UNIQUE_IDENTIFIER, "EMP1",emp1)
    #     if i.UNIQUE_IDENTIFIER == emp1:
    #         if i.COMPLIANCE=="Non-Conformity":
    #             print("FALSE")
    #             cnt1 = cnt1 + 1
    #             print("cnt1",cnt1)
    #         elif i.COMPLIANCE =="Conformity":
    #             cnt2= cnt2+1
    #             print("TRUE") 
    #             print("cnt2",cnt2)
           

    #         #print("C", i.COMPLIANCE)    
    #     #else:

    # print("cnt1", cnt1)
    # print("cnt2", cnt2)



    # conformity_objects = checklist_details.filter(COMPLIANCE='Conformity') 
    total_conformities = conformity_objects.count()
    total_nonconformities = nonconformity_objects.count()
    context = {
        # 'auditstandard':auditstandard, 
        # 'checklist_details':checklist_details, 'total_nonconformities':total_nonconformities, 'nonconformity_objects':nonconformity_objects, 'emps':emps, 
        'emp1': emp1,
        'chklist1': chklist1,
        'nonconformity_objects':nonconformity_objects,
        'total_conformities': total_conformities,
        'total_nonconformities':total_nonconformities,
        'emps': emps,
        'pdfid':pdfid
        }
    return render(request, 'report.html', context)

def email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, settings.EMAIL_HOST_USER,[email],fail_silently=False)
    return render(request, 'email.html', {})

def emaill(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        mail_id = request.POST.get('email')
        email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
        
        email.content_subtype = 'html'
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        return HttpResponse("Sent")
    return render(request, 'emaill.html', {})
        



def pdf(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3",
    # ]
    # auditstandard = AuditStandard.objects.get(id=pk)
    emp1 = Emp.objects.get(id=pk)
    chklist1 = Checklist.objects.filter(UNIQUE_IDENTIFIER=emp1)
    nonconformity_objects = chklist1.filter(COMPLIANCE='Non-Conformity')
    conformity_objects = chklist1.filter(COMPLIANCE='Conformity')
    total_conformities = conformity_objects.count()
    total_nonconformities = nonconformity_objects.count()

    # checklist_details = auditstandard.checklist_set.all()
    # nonconformity_objects = checklist_details.filter(COMPLIANCE='Non-Conformity')
    # conformity_objects = checklist_details.filter(COMPLIANCE='Conformity')
    lines = []
    # for audit in auditstandard:
    #     lines.append(audit.CODE)
    #     lines.append(audit.DESCRIPTION)
    # for detail in checklist_details:
    lines.append("------------REPORT------------")
    lines.append("Type of Audit- "+ emp1.emp_type_of_audit)
    lines.append("Company Being Audited- "+ emp1.emp_being_audited)
    lines.append("Auditors- "+ emp1.emp_auditors)
    lines.append("Start Date- "+ str(emp1.emp_date_of_audit))
    lines.append("End Date of Audit- "+ str(emp1.emp_end_date_of_audit))
    lines.append("Department Being Audited- "+ emp1.emp_department_being_audited)
    lines.append("Person Being Audited- "+ emp1.emp_person_being_audited)
    lines.append("Unique Identifier- "+ emp1.emp_unique_identifier)
    lines.append("==========================================")
    lines.append("==========================================")
    lines.append("==========================================")
    lines.append("Conformities- "+ str(total_conformities))
    lines.append("Non-Conformities- "+ str(total_nonconformities))
    lines.append("==========================================")
    lines.append("==========================================")
    lines.append("==========================================")
    for object in nonconformity_objects:
        lines.append("N.C Clause -"+str(object.CLAUSE)+"  "+ "Person N.C assigned to " + emp1.emp_person_being_audited)

    
        # checklist_details = Checklist.objects.all()
        # nonconformity_objects = checklist_details.filter(COMPLIANCE='Non-Conformity')
        # conformity_objects = checklist_details.filter(COMPLIANCE='Conformity')
        # lines = []
        # for nonconformity in nonconformity_objects:
        # lines.append(nonconformity)
        # for conformity in conformity_objects:
        # lines.append(conformity)

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='test.pdf')


# def pdf(request):
#     persons = Person.objects.all()
#     template = get_template('plapp/person_list.html')
#     html = template.render({'persons': persons})
#     options = {
#         'page-size': 'Letter',
#         'encoding': "UTF-8",
#     }
#     pdf = pdfkit.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment;
#     filename="pperson_list_pdf.pdf"'
#     return response    



# def SendPlainEmail(request):
#     message=request.POST.get('message','')
#     subject=request.POST.get('subject','')
#     mail_id=request.POST.get('email','')
#     email=EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
#     email.content_subtype='html'
#     email.send()
#     return HttpResponse("Sent")

# def send_mail_plain_with_stored_file(request):
#     message=request.POST.get('message','')
#     subject=request.POST.get('subject','')
#     mail_id=request.POST.get('email','')
#     email=EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
#     email.content_subtype='html'

#     file=open("README.md","r")
#     file2=open("manage.py","r")
#     email.attach("README.md",file.read(),'text/plain')
#     email.attach("manage.py",file2.read(),'text/plain')

#     email.send()
#     return HttpResponse("Sent")


# def send_mail_plain_with_file(request):
#     message = request.POST.get('message', '')
#     subject = request.POST.get('subject', '')
#     mail_id = request.POST.get('email', '')
#     email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
#     email.content_subtype = 'html'

#     file = request.FILES['file']
#     email.attach(file.name, file.read(), file.content_type)

#     email.send()
#     return HttpResponse("Sent")

# def emaill(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         subject = request.POST.get('subject')
#         mail_id = request.POST.get('email')
#         email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
#         email.content_subtype = 'html'

#         email.attach_file('auditapp/pdfs/test.pdf')
#         email.send()
#         return HttpResponse("Sent")
#     return render(request, 'emaill.html', {})



