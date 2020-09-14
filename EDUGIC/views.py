from .models import RegisterData, Add_Question, Video_Tutorial , Add_Job, Add_Packages, Add_Student, Add_user
from.models import Add_Exam, PDF, Topics, Addsub_Topics, Center, Coupons, Add_Subject, Subject_Toexam, Add_group
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import datetime


def index(request):
    return render(request,'index.html')


def sign_in(request):
    if request.method is 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # return render(request, "index.html")
        try:
            # RegisterData.objects.get(username=username, password=password)
            RegisterData.objects.get(username=username, password=password)
        except RegisterData.DoesNotExist:
            return render(request, "sign-in.html")
        else:
            return render(request, "index.html")

    return render(request, "sign-in.html")
    


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = RegisterData(
            username=username,email=email,password=password)
        data.save()
        return render(request, 'sign-in.html')
    else:
        return render(request,'sign-up.html')



def add_question(request):
    if request.method == 'POST':
        passage_id = request.POST['passage_id']
        question_type = request.POST['question_type']
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']
        true_false1 = request.POST['true_false']
        black_space = request.POST['black_space']
        explanation = request.POST['explanation']
        group = request.POST['group']
        subject = request.POST['subject']
        topics = request.POST['topics']
        sub_topics = request.POST['sub_topics']
        hint = request.POST['hint']
        marks = request.POST['marks']
        negative_marks = request.POST['negative_marks']
        difficulty_level = request.POST['difficulty_level']

        data = Add_Question(
            passage_id=passage_id, ques_type=question_type,question=question, option1=option1, option2=option2, option3=option3, option4=option4,
            answer=answer, true_false1=true_false1 , black_space=black_space, explanation=explanation,
            group=group,subject=subject, topics=topics, sub_topics=sub_topics, hint=hint, marks=marks, negative_marks=negative_marks,
            difficulty_level=difficulty_level
        )
        try:
            data.save()
            return render(request, 'add_question.html')
        except Add_Subject.DoesNotExist:
            return render(request,'add_question.html')

    else:
        data={
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            'd4': Add_group.objects.all()
        }
        return render(request, 'add_question.html', {'data': data})

def addsub_toexam(request):
    if request.method =="POST":
        subject = request.POST['subject']
        no_ofques = request.POST['no_of_ques']
        quest_attempt_count = request.POST['quest_attempt_count']
        ques_type = request.POST['ques_type']
        difficulty_lvl = request.POST['difficulty_level']
        a=Subject_Toexam(subject=subject, no_of_question=no_ofques, question_attempt=quest_attempt_count, question_type=ques_type, difficulty_level=difficulty_lvl)
        a.save()
        sub = Subject_Toexam.objects.all()
        return render(request,'add_exam.html', {'sub': sub})
    else:
        return render(request,'add_exam.html',{'data':Add_Subject.objects.all()})


def add_exam(request):
    if request.method =="POST":
        package = request.POST['package']
        name_of_Exam = request.POST['exam_name']
        passing_Percentage = request.POST['pass_percentage']
        instruction = request.POST['instruction']
        syllabus = request.POST['syllabus']
        exam_duration = request.POST['exam_duration']
        start_date = request.POST['start_date']
        end_Date = request.POST['end_date']
        show_Answer_Sheet = request.POST['ans_sheet']
        negative_marking = request.POST['neg_marking']
        browser_Tolerance = request.POST['brower_tol']
        result_After_Finish = request.POST['result_aftfinish']
        instant_Result = request.POST['Ins_result']
        multi_Langyage = request.POST['multi_lang']
        attempt_Count = request.POST['attempt_count']
        select_Group = request.POST['group']
        random_Question = request.POST['random_ques']
        mode = request.POST['mode']
        option_Shuffle = request.POST['ope_shuffle']
        exam = Add_Exam(
            name_of_exam=name_of_Exam, passing_percentage=passing_Percentage, instruction=instruction, syllabus=syllabus,
            exam_duration=exam_duration, attempt_count=attempt_Count, start_date=start_date, end_date=end_Date, show_answer_sheet=show_Answer_Sheet,
            negative_marking=negative_marking, browser_tolerance=browser_Tolerance,result_after_finish=result_After_Finish,
            instant_result=instant_Result, multi_languages=multi_Langyage, select_group=select_Group,random_question=random_Question,
            mode = mode, option_shuffle=option_Shuffle, package=package
        )
        exam.save()
        return render(request,'exam.html')
    else:
        return render(request,'add_exam.html',{'data':Add_Subject.objects.all()})
    sub = Subject_Toexam.objects.all()
    return render(request, 'add_exam.html', {'sub': sub})

def exam(request):
    addexam = Add_Exam.objects.all()
    return render(request,'exam.html',{'addexam':addexam})


def job(request):
    job = Add_Job.objects.all()
    return render(request,'job.html', {'job':job})


def add_job(request):
    if request.method == "POST":
        name_of_job = request.POST["name_of_job"]
        post_date = request.POST["post_date"]
        post_update_date = request.POST["post_update_date"]
        short_information = request.POST["short_information"]
        about_exam = request.POST["about_exam"]
        about_post = request.POST["about_post"]
        notification = request.POST["notification"]
        importants_dates = request.POST["importants_dates"]
        application_fee = request.POST["application_fee"]
        v_entry_type = request.POST["v_entry_type"]
        v_branch_name = request.POST["v_branch_name"]
        v_age_limit = request.POST["v_age_limit"]
        v_eligibility = request.POST["v_eligibility"]
        entry_type = request.POST["entry_type"]
        branch_name = request.POST["branch_name"]
        age_limit = request.POST["age_limit"]
        eligibility = request.POST["eligibility"]
        note = request.POST["note"]
        Some_Useful_Important_Links = request.POST["Some_Useful_Important_Links"]
        apply_online = request.POST["apply_online"]
        download_notification = request.POST["download_notification"]
        official_website = request.POST["official_website"]
        data = Add_Job(
            name_of_job=name_of_job,
            post_date=post_date,
            post_update_date=post_update_date,
            short_information=short_information,
            about_exam=about_exam,
            about_post=about_post,
            notification=notification,
            importants_dates=importants_dates,
            application_fee=application_fee,
            v_entry_type=v_entry_type,
            v_branch_name=v_branch_name,
            v_age_limit=v_age_limit,
            v_eligibility=v_eligibility,
            entry_type=entry_type,
            branch_name=branch_name,
            age_limit=age_limit,
            eligibility=eligibility,
            note=note,
            Some_Useful_Important_Links=Some_Useful_Important_Links,
            apply_online=apply_online,
            download_notification=download_notification,
            official_website=official_website,
        )
        data.save()
        return render(request, 'add_job.html')
    else:
        return render(request, 'add_job.html')


def packages(request):
    add_packages = Add_Packages.objects.all()
    return render(request, 'packages.html', {'add_packages': add_packages})
def add_packages(request):
    if request.method == "POST":
        type = request.POST['type']
        package_name = request.POST['package_name']
        exam = request.POST['exam']
        amount = request.POST['amount']
        discount_amount = request.POST['discount_amount']
        expiry_days = request.POST['expiry_days']
        upload_photo = request.POST['upload_photo']
        description = request.POST['description']
        data = Add_Packages(
            package_name=package_name,type=type,
            exam=exam, amount=amount, discount_amount = discount_amount,expiry_days=expiry_days,
            upload_photo=upload_photo, description=description)
        data.save()
        add_packages = Add_Packages.objects.all()
        return render(request, 'add_packages.html',{'add_packages':add_packages})
    else:
        add_packages = Add_Packages.objects.all()
        return render(request, 'add_packages.html',{'add_packages':add_packages})


def users(request):
    adduser = Add_user.objects.all()
    return render(request,'users.html',{'adduser':adduser})



def add_user(request):
    if request.method =='POST':
        user_level = request.POST['user_level']
        group = request.POST['group']
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        user = Add_user(user_level=user_level, group = group, username=username,  password=password, name = name, email = email, mobile = mobile)
        user.save()

        adduser =Add_user.objects.all()
        return render(request,'users.html',{'adduser':adduser})
    else:
        return render(request, 'add_user.html')
    adduser = Add_user.objects.all()
    return render(request, 'users.html', {'adduser': adduser})

def video_post(request):
    if request.method == "POST":
        subject_name = request.POST['subject_name']
        topic_name = request.POST['topic_name']
        details = request.POST['details']
        video_url = request.POST['video_url']
        video = Video_Tutorial(subject_name=subject_name, topic_name=topic_name, details=details, video_url=video_url)
        video.save()
        return redirect('/video_tutorial')
    else:
        data = {
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all()
        }
        return render(request, 'video_post.html',{'data':data})


def video_tutorial(request):
    retrive_video = Video_Tutorial.objects.all()
    return render(request, 'video_tutorial.html',{'retrive_video':retrive_video} )


#abhishek
def chat(request):
    return render(request,'chat.html')

def pdf_tutorial(request):
    pdf = PDF.objects.all()
    return render(request,'pdf_tutorial.html', {'pdf': pdf})


#abhishek
def add_new_pdf(request):
    if request.method =='POST':
        subject_name = request.POST['name']
        topics_name = request.POST['topics_name']
        details = request.POST['details']
        pdf_url = request.POST['pdfurl']
        # try:
        #     b = PDF(subject_name=subject_name, topics_name=topics_name, details=details, pdf_url=pdf_url)
        #     b.save()
        #     pdf = PDF.objects.all()
        #     return render(request, 'add_new_pdf.html', {'pdf': pdf})
        # except PDF.DoesNotExist:
        #     pdf = PDF.objects.all()
        #     return render(request, 'pdf_tutorial.html', {'pdf': pdf})
        b = PDF(subject_name=subject_name, topics_name=topics_name, details=details, pdf_url=pdf_url)
        b.save()
        return redirect('/pdf_tutorial')
    else:
        data = {
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all()
        }
        return render(request, 'add_new_pdf.html', {'data':data})


#abhishek
#no module yet
def file_images(request):
    return render(request,'file-images.html')

#abhiskek
#no Module yet
def file_media(request):
    return render(request,'file-media.html')


def mail_compose(request):
    return render(request,'mail-compose.html')


def student(request):
    data = Add_Student.objects.all()
    return render(request,'student.html',{'data':data})


def add_subject(request):
    if request.method=='POST':
        group_name = request.POST['group_name']
        subject_name = request.POST['subject_name']
        g = Add_Subject(group_name=group_name, subject_name= subject_name)
        g.save()
        return redirect('/subjects')
    else:
        data = {'d4': Add_group.objects.all()}
        return render(request, 'add_subject.html',{'data':data})


def subjects(request):
    addsubject = Add_Subject.objects.all()
    return render(request, 'subjects.html', {'addsubject': addsubject})


def mail_single(request):
    return render(request,'mail-single.html')





def profile(request):
    return render(request,'profile.html')


def exam_center(request):
    data = Center.objects.all()
    return render(request,'exam_center.html',{'data':data})


def add_center(request):
    if request.method == 'POST':
        state_name = request.POST['state_name']
        city_name = request.POST['city_name']
        institute_name = request.POST['institute_name']
        d = Center(state_name=state_name, city_name=city_name, institute_name=institute_name)
        try:
            d.save()
            data = Center.objects.all()
            return render(request, 'exam_center.html', {'data': data})
        except Center.DoesNotExist:
            return render(request, 'add_center.html')
    return render(request, 'add_center.html')

def coupons(request):
    coupons =Coupons.objects.all()
    return render(request,'coupons.html',{'coupons':coupons})


def add_coupons(request):
    if request.method =="POST":
        name = request.POST['name']
        description = request.POST['description']
        coupons_amount = request.POST['coupons_amount']
        amount = request.POST['amount']
        coupons_order = request.POST['coupons_order']
        couposn_code = request.POST['couposn_code']
        no_of_coupons = request.POST['no_of_coupons']
        user_per_customs = request.POST['user_per_customs']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        coupons = Coupons(
            name=name, description=description, coupons_amount=coupons_amount,
            amount=amount, coupons_order=coupons_order, couposn_code=couposn_code,
            no_of_coupons=no_of_coupons, user_per_customs=user_per_customs,
            start_date=start_date, end_date=end_date
        )
        try:
            coupons.save()
            coupon = Coupons.objects.all()
            return render(request, 'add_coupons.html',{'coupon':coupon})
        except Coupons.DoesNotExist:
            return render(request, 'add_coupons.html')
    return render(request, 'add_coupons.html')


def topics(request):
    topics = Topics.objects.all()
    return render(request,'topics.html',{'topics':topics})


def add_topics(request):
    if request.method =='POST':
        subject_name = request.POST['subject_name']
        topic_name = request.POST['topic']
        topic = Topics(subject_name=subject_name, topic_name = topic_name)
        try:
            topic.save()
            return redirect('/topics')
        except Topics.DoesNotExist:
            return render(request, 'add_topics.html')
    else:
        return render(request, 'add_topics.html', {'data':Add_Subject.objects.all()})


def sub_topics(request):
    subtopic = Addsub_Topics.objects.all()
    return render(request,'sub_topics.html',{'subTopic':subtopic})


def add_sub_topic(request):
    if request.method =="POST":
        sub_name = request.POST['subject_name']
        topic_name = request.POST['topic_name']
        sub_topic = request.POST['sub_topic']
        addsub = Addsub_Topics(sub_name=sub_name, topic_name=topic_name, sub_topic=sub_topic)
        addsub.save()
        return redirect('/sub_topics')
    else:
        data = {
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
        }
        return render(request, 'add_sub_topic.html', {'data': data})
    return render(request,'add_sub_topic.html')



def add_group(request):
    if request.method == 'POST':
        group = request.POST['group_name']
        description = request.POST['description']
        data = Add_group(group_name=group, description=description)
        data.save()
        return render(request, 'add_group.html')
    else:
        return render(request, 'add_group.html')
    return render(request, 'add_group.html')


def add_grouptable(request):
    add_group = Add_group.objects.all()
    return render(request, 'add_grouptable.html', {'add_group': add_group})


def result(request):
    return render(request,'result.html')



def file_dashboard(request):
    return render(request,'file-dashboard.html')


def file_documents(request):
    return render(request,'file-documents.html')


def qestions(request):
    addquestion = Add_Question.objects.all()
    return render(request,'questions.html',{'addquestion':addquestion})


def add_student(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        address = request.POST['address']
        alternate = request.POST['alt_number']
        expiry_date = request.POST['expiry_date']
        upload_photo = request.POST['myFile']
        group = request.POST['group']
        password = request.POST['password']
        phone = request.POST['phone']
        enrollment_number = request.POST['enroll_number']
        status = request.POST['status']
        admission_date = request.POST['admission_date']

        student = Add_Student(
            email=email, name=name, address=address, alternate=alternate,
            expiry_date=expiry_date, upload_photo=upload_photo, group=group, password=password,
            phone=phone, enrollment_number=enrollment_number, status=status, admission_date=admission_date
        )

        student.save()
        return redirect('/student')
    else:
        return render(request,'add_student.html')


def used_coupons(request):
    return render(request,'used_coupons.html')


def dpf_delete(request):
    if request.method == 'GET':
        subject_name = request.GET["subject_name"]
        PDF.objects.filter(subject_name=subject_name).delete()
        # PDF.objects.filter(subject_name)
        return pdf_tutorial(request)


def delete_packages(request):
    if request.method == 'GET':
        id = request.GET["id"]
        Add_Packages.objects.filter(id=id).delete()
        return packages(request)


def delete_subject(request):
    if request.method =="GET":
        id = request.GET['id']
        Add_Subject.objects.filter(id=id).delete()
        return subjects(request)


def delete_videotutorial(request):
    if request.method =="GET":
        id = request.GET['id']
        Video_Tutorial.objects.filter(id=id).delete()
        return video_tutorial(request)


def delete_subtopic(request):
    if request.method =="GET":
        id = request.GET['id']
        Addsub_Topics.objects.filter(id = id).delete()
        return sub_topics(request)


def detele_questions(request):
    id = request.GET['id']
    Add_Question.objects.filter(id = id).delete()
    return qestions(request)


def delete_topics(request):
    id = request.GET['id']
    Topics.objects.filter(id=id).delete()
    return topics(request)


def delete_Excenter(request):
    id = request.GET['id']
    Center.objects.filter(id=id).delete()
    return exam_center(request)


def delete_exam(request):
    select_group = request.GET['group']
    Add_Exam.objects.filter(select_group=select_group).delete()
    return exam(request)


def subject_chk_delete(request):

    return None


def delete_coupons(request):
    id = request.GET['id']
    Coupons.objects.filter(id=id).delete()
    return coupons(request)


def delete_job(request):
    if request.method == "GET":
        job_name = request.GET['job_name']
        Add_Job.objects.filter(job_name=job_name).delete()
        return job(request)


def detele_student(request):
    id = request.GET['id']
    Add_Student.objects.filter(id=id).delete()
    return student(request)


def delete_user(request):
    email = request.GET['email']
    Add_Student.objects.filter(email=email).delete()
    return users(request)


def delete_group(request):
    if request.method == 'GET':
        id = request.GET["id"]
        Add_group.objects.filter(id=id).delete()
        return add_grouptable(request)


def multiple_delete_subject(request):
    if request.method == 'POST':
        a = request.POST.getlist('id')
        for x in a:
            Add_Subject.objects.get(id=x).delete()
    return subjects(request)


def multiple_delete_packages(request):
    if request.method == 'POST':
        a = request.POST.getlist('selectAll')
        for x in a:
            Add_Packages.objects.get(package_name=x).delete()
    return packages(request)


def multiple_delete_video(request):
    if request.method == 'POST':
        a = request.POST.getlist('selectAll')
        for x in a:
            Video_Tutorial.objects.get(id=x).delete()
            return topics(request)


def multiple_delete_pdftutorial(request):
    if request.method == 'POST':
        a = request.POST.getlist('selectAll')
        for x in a:
            PDF.objects.get(subject_name=x).delete()
    return pdf_tutorial(request)


def multiple_delete_job(request):
    if request.method == 'POST':
        a = request.POST.getlist('selectAll')
        for x in a:
            Add_Job.objects.get(job_name=x).delete()
    return job(request)


def multiple_delete_topics(request):
    if request.method == 'POST':
        a= request.POST.getlist('selectAll')
        for x in a:
            Topics.objects.get(subject_name=x).delete()
    return topics(request)


def multiple_delete_subtopic(request):
    if request.method =="POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Addsub_Topics.objects.get(sub_name=x).delete()
    return sub_topics(request)


def multiple_delete_question(request):
    if request.method =="POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Add_Question.objects.get(id=x).delete()
    return qestions(request)


def multiple_delete_examcenter(request):
    if request.method =="POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Center.objects.get(state_name=x).delete()
    return exam_center(request)


def multiple_delete_users(request):
    if request.method == "POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Add_user.objects.get(username=x).delete()
    return users(request)


def multiple_delete_exam(request):
    if request.method =="POST":
        a = request.POST.getlist("selectAll")
        for x in a:
            Add_Exam.objects.get(name_of_exam=x).delete()
    return exam(request)


def multiple_delete_coupons(request):
    if request.method =="POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Coupons.objects.get(name=x).delete()
    return coupons()


def multiple_delete_student(request):
    if request.method == "POST":
        a = request.POST.getlist("selectAll")
        for x in a:
            Add_Student.objects.get(email=x).delete()
    return student(request)


def multiple_delete_group(request):
    if request.method == "POST":
        a = request.POST.getlist('selectAll')
        for x in a:
            Add_group.objects.get(group_name=x).delete()
    return add_grouptable(request)


def edit_student(request):
    id = request.GET['id']
    data = Add_Student.objects.get(id=id)
    return render(request,'edit_student.html',{'data':data})


def update_student(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        email = request.POST['email']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        alternate = request.POST['alt_number']
        admission_date = request.POST['admission_date']
        expiry_date = request.POST['expiry_date']
        upload_photo = request.POST['myFile']
        group = request.POST['group']
        password = request.POST['password']
        enrollment_number = request.POST['enroll_number']
        status = request.POST['status']
        Add_Student.objects.filter(id=id).update(email=email,name=name,phone=phone,address=address,alternate=alternate,admission_date=admission_date,expiry_date=expiry_date,upload_photo=upload_photo,group=group, password=password, enrollment_number=enrollment_number,status=status)
        data = Add_Student.objects.all()
        return render(request, 'student.html',{'data':data})
    else:
        return  render(request,'edit_student.html')


def edit_center(request):
    id = request.GET['id']
    data = Center.objects.get(id=id)
    return render(request,'edit_center.html',{'data':data})


def update_center(request):
    if request.method == 'POST':
        id=int(request.POST['id'])
        state_name = request.POST['state_name']
        city_name = request.POST['city_name']
        institute_name = request.POST['institute_name']
        Center.objects.filter(id=id).update(city_name=city_name,institute_name=institute_name,state_name=state_name)
        data = Center.objects.all()
        return render(request,'exam_center.html',{'data':data})


def update_coupons(request):
    if request.method == "POST":
        id= int(request.POST['id'])
        name = request.POST['name']
        description = request.POST['description']
        amount = request.POST['amount']
        couposn_code = request.POST['couposn_code']
        no_of_coupons = request.POST['no_of_coupons']
        user_per_customs = request.POST['user_per_customs']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Coupons.objects.filter(id=id).update(name=name, description=description,amount=amount, couposn_code = couposn_code, no_of_coupons=no_of_coupons, user_per_customs=user_per_customs,start_date=start_date, end_date=end_date)
        return redirect('coupons')


def edit_coupons(request):
    id = request.GET['id']
    data = Coupons.objects.get(id=id)
    return render(request, 'edit_coupons.html', {'data': data})


def edit_exam(request):
    select_group = request.GET['select_group']
    data = Add_Exam.objects.get(select_group=select_group)
    return render(request, 'edit_exam.html', {'data': data})


def update_exam(request):
    if request.method == "POST":
        # select_group = request.POST['select_group']
        package = request.POST['package']
        name_of_exam = request.POST['name_of_exam']
        passing_percentage = request.POST['passing_percentage']
        instruction = request.POST['instruction']
        syllabus = request.POST['syllabus']
        exam_duration = request.POST['exam_duration']
        attempt_count = request.POST['attempt_count']
        end_date = request.POST['end_date']
        show_answer_sheet = request.POST['show_answer_sheet']
        negative_marking = request.POST['negative_marking']
        browser_tolerance = request.POST['browser_tolerance']
        result_after_finish = request.POST['result_after_finish']
        instant_result = request.POST['instant_result']
        multi_languages = request.POST['multi_languages']
        select_group = request.POST['select_group']
        random_question = request.POST['random_question']
        mode = request.POST['mode']
        option_shuffle = request.POST['option_shuffle']
        Add_Exam.objects.filter(select_group=select_group).update(select_group=select_group, package=package,name_of_exam=name_of_exam, passing_percentage=passing_percentage, attempt_count=attempt_count,end_date=end_date,negative_marking=negative_marking,browser_tolerance=browser_tolerance, result_after_finish=result_after_finish, instant_result=instant_result, multi_languages=multi_languages,show_answer_sheet=show_answer_sheet,random_question=random_question,mode=mode, option_shuffle=option_shuffle,instruction=instruction,syllabus=syllabus, exam_duration=exam_duration,)
        return render(request, 'exam.html')


def update_group(request):
    id = int(request.POST['id'])
    group_name = request.POST['group_name']
    description = request.POST['description']
    Add_group.objects.filter(id=id).update(group_name=group_name, description=description)
    return redirect('/add_grouptable')


def edit_group(request):
    id = request.GET["id"]
    data = Add_group.objects.get(id=id)
    return render(request, 'edit_group.html', {'data': data})


def edit_job(request):
    job_name = request.GET['job_name']
    data = Add_Job.objects.get(job_name=job_name)
    return render(request, 'edit_job.html', {'data': data})


def update_job(request):
    if request.method == "POST":
        job_name = request.POST['job_name']
        subject_name = request.POST['subject_name']
        category_name = request.POST['category_name']
        Add_Job.objects.filter(job_name=job_name).update(job_name=job_name, subject_name=subject_name, category_name=category_name)
        return redirect('job')


def edit_packages(request):
    id = request.GET['id']
    data = Add_Packages.objects.get(id=id)
    return render(request, 'edit_packages.html',{'data':data})


def update_packages(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        type = request.POST['gender']
        exam = request.POST['exam']
        amount = request.POST['amount']
        discount = request.POST['discount_amount']
        expiry_days = request.POST['expiry_days']
        description = request.POST['description']
        package_name = request.POST['package_name']
        Add_Packages.objects.filter(id=id).update(
            type=type, exam=exam, amount=amount,discount_amount=discount,expiry_days=expiry_days,description=description,
            package_name=package_name
        )
    else:
        data = {
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            'd4': Add_group.objects.all(),
            'd5': Add_Question.objects.all(),
        }
        return redirect('packages',{'data':data})


def edit_question(request):
    id = request.GET['id']
    data = {
        'd1': Add_Subject.objects.all(),
        'd2': Addsub_Topics.objects.all(),
        'd3': Topics.objects.all(),
        'd4': Add_group.objects.all(),
        'd5': Add_Question.objects.filter(id=id),
    }
    return render(request, 'edit_question.html',{'data' :data})


def update_question(request):
    if request.method =='POST':
        id = request.POST['id']
        passage_id = request.POST['passage_id']
        question_type = request.POST['question_type']
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']
        true_false1 = request.POST['true_false']
        black_space = request.POST['black_space']
        explanation = request.POST['explanation']
        group = request.POST['group']
        subject = request.POST['subject']
        topics = request.POST['topics']
        sub_topics = request.POST['sub_topics']
        hint = request.POST['hint']
        marks = request.POST['marks']
        negative_marks = request.POST['negative_marks']
        difficulty_level = request.POST['difficult_level']

        Add_Question.objects.filter(id=id).update(
            passage_id=passage_id, ques_type=question_type,question=question, option1=option1, option2=option2, option3=option3, option4=option4,
            answer=answer, true_false1=true_false1 , black_space=black_space, explanation=explanation,
            group=group,subject=subject, topics=topics, sub_topics=sub_topics, hint=hint, marks=marks, negative_marks=negative_marks,
            difficulty_level=difficulty_level
        )
        data = {
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            'd4': Add_group.objects.all(),
            'd5': Add_Question.objects.all(),
        }
    return redirect('/questions', {'data':data})


def update_subject(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        subject_name = request.POST['subject_name']
        group_name = request.POST['group_name']
        Add_Subject.objects.filter(id=id).update(subject_name=subject_name, group_name=group_name)
        return redirect('subjects')
    else:
        data = {
            'd4': Addsub_Topics.objects.all(),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            'd5': Add_group.objects.all(),
        }
        return render(request,'student.html',{'data':data})


def edit_subject(request):
    id = request.GET['id']
    data = {
        'd1':Add_Subject.objects.filter(id=id),
        'd5': Add_group.objects.all(),
    }
    return render(request,'edit_subject.html',{'data':data})


def update_sub_topics(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        sub_name = request.POST['subject_name']
        topic_name = request.POST['topic_name']
        sub_topic = request.POST['sub_topic']
        Addsub_Topics.objects.filter(id=id).update(sub_name=sub_name, topic_name=topic_name, sub_topic=sub_topic)
        return redirect('/sub_topics')
    else:
        data = {
            'd4': Addsub_Topics.objects.all(),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
        }
        return render(request, 'add_sub_topic.html', {'data': data})
    return render(request, 'add_sub_topic.html')


def edit_sub_topics(request):
    id = request.GET['id']
    data = {'d4': Addsub_Topics.objects.get(id=id),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
    }
    return render(request, 'edit_sub_topic.html', {'data': data})


def view_topic(request):
    id = request.GET['id']
    data = {'d4': Topics.objects.get(id=id),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            }
    return render(request, 'view_topics.html', {'data': data})


def edit_topics(request):
    id = request.GET['id']
    data = {'d4': Topics.objects.get(id=id),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            }
    return render(request, 'edit_topics.html', {'data': data})


def update_topics(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        subject_name = request.POST['subject_name']
        topic_name = request.POST['topic_name']
        Topics.objects.filter(id=id).update(subject_name=subject_name, topic_name=topic_name)
        return redirect('/topics')
    else:
        return render(request, 'add_topics.html')


def edit_user(request):
    email = request.GET['email']
    data = Add_user.objects.get(email=email)
    # print(data)
    return render(request, 'edit_user.html', {'data':data})


def update_user(request):
    if request.method == "POST":
        user_level = request.POST['user_level']
        group = request.POST['group']
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        Add_user.objects.filter(email=email).update(name=name,mobile=mobile,user_level=user_level,group=group,username=username,password=password,email=email)
        adduser = Add_user.objects.all()
        return render(request,'users.html',{'adduser':adduser})
    else:
        return  render(request,'users.html')


def edit_videotutorial(request):
    id = request.GET['id']
    data = Video_Tutorial.objects.get(id=id)
    return render(request,'edit_video.html',{'data':data})


def update_videotutorial(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        subject_name = request.POST['subject_name']
        topic_name = request.POST['topic_name']
        details = request.POST['details']
        video_url = request.POST['video_url']
        Video_Tutorial.objects.filter(id=id).update(subject_name=subject_name, topic_name=topic_name, details=details, video_url=video_url)
        return redirect('video_tutorial')
    else:
        return render(request, 'edit_video.html')


def edit_pdf(request):
    id = request.GET['id']
    data = PDF.objects.get(id=id)
    return render(request,'edit_pdf.html',{'data':data})


def update_pdf(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        subject_name = request.POST['name']
        topics_name = request.POST['topics_name']
        details = request.POST['details']
        pdf_url = request.POST['pdfurl']
        try:
            PDF.objects.filter(id=id).update(subject_name=subject_name ,topics_name=topics_name, details=details, pdf_url=pdf_url)
            return redirect('pdf_tutorial')
        except PDF.DoesNotExist:
            pdf = PDF.objects.all()
            return render(request, 'pdf_tutorial.html', {'pdf': pdf})
    return  render(request,'edit_pdf.html')


def user_view(request):
    id = request.GET['id']
    data = Add_user.objects.get(id)
    return render(request, 'user_view.html', {'data': data})


def view_package(request):
    id = request.GET['id']
    data = Add_Packages.objects.get(id=id)
    return render(request, 'view_package.html',{'data':data})


def view_subject(request):
    id=request.GET['id']
    data=Add_Subject.objects.get(id=id)
    return render(request, 'view_subject.html', {'data':data})


def view_video(request):
    id = request.GET['id']
    data = Video_Tutorial.objects.get(id=id)
    return render(request,'view_video.html',{'data':data})


def view_pdf(request):
    id = request.GET['id']
    data = PDF.objects.get(id=id)
    return render(request,'view_pdf.html',{'data':data})


def view_sub_topic(request):
    id = request.GET['id']
    data = {'d4': Addsub_Topics.objects.get(id=id),
            'd1': Add_Subject.objects.all(),
            'd2': Addsub_Topics.objects.all(),
            'd3': Topics.objects.all(),
            }
    return render(request, 'view_sub_topic.html', {'data': data})


def view_question(request):
    passage_id = request.GET['passage_id']
    data = Add_Question.objects.get(passage_id=passage_id)
    return render(request, 'view_question.html', {'data': data})


def view_center(request):
    id = request.GET['id']
    data = Center.objects.get(id=id)
    return render(request,'view_center.html',{'data':data})





def view_student(request):
    id = request.GET['id']
    data = Add_Student.objects.get(id=id)
    return render(request,'view_student.html',{'data':data})


def view_group(request):
    id = request.GET["id"]
    data=Add_group.objects.get(id=id)
    return render(request, 'view_group.html', {'data': data})


def view_job(request):
    job_name = request.GET['job_name']
    data = Add_Job.objects.get(job_name=job_name)
    return render(request, 'edit_job.html', {'data': data})


def view_coupons(request):
    id = request.GET['id']
    data = Coupons.objects.get(id=id)
    return render(request, 'view_coupons.html', {'data': data})


def view_exam(request):
    select_group = request.GET['select_group']
    data = Add_Exam.objects.get(select_group=select_group)
    return render(request, 'view_exam.html', {'data': data})


def job_details(request):
    name_of_job = request.GET['name_of_job']
    data = Add_Job.objects.get(name_of_job=name_of_job)
    return render(request, 'job_details.html', {'data': data})



