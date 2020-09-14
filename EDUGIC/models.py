from django.db import models

class RegisterData(models.Model):
    username=models.CharField(max_length=100, primary_key=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)

class Add_Question(models.Model):
    passage_id=models.CharField(max_length=100)
    ques_type = models.CharField(max_length=50)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    true_false1 = models.CharField(max_length=20)
    black_space = models.CharField(max_length=50)
    explanation = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    topics = models.CharField(max_length=50)
    sub_topics = models.CharField(max_length=50)
    hint = models.CharField(max_length=50)
    marks = models.CharField(max_length=50)
    negative_marks = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=50)

class Add_Job(models.Model):
    name_of_job = models.CharField(max_length=50)
    post_date = models.CharField(max_length=50)
    post_update_date = models.CharField(max_length=50)
    short_information = models.CharField(max_length=50)
    about_exam = models.CharField(max_length=50)
    about_post = models.CharField(max_length=50)
    notification = models.CharField(max_length=50)
    importants_dates = models.CharField(max_length=50)
    application_fee = models.IntegerField()
    v_entry_type = models.CharField(max_length=50)
    v_branch_name = models.CharField(max_length=50)
    v_age_limit = models.IntegerField()
    v_eligibility = models.CharField(max_length=50)
    entry_type = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    age_limit = models.IntegerField()
    eligibility = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    Some_Useful_Important_Links = models.CharField(max_length=50)
    apply_online = models.CharField(max_length=50)
    download_notification = models.CharField(max_length=50)
    official_website = models.CharField(max_length=50)

class Add_Packages(models.Model):
    type = models.CharField(max_length=10)
    package_name = models.CharField(max_length=50)
    exam = models.CharField(max_length=50)
    amount = models.IntegerField()
    discount_amount = models.IntegerField()
    expiry_days = models.IntegerField()
    upload_photo = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

class Add_Student(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    alternate = models.IntegerField()
    admission_date = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=100)
    upload_photo = models.ImageField(upload_to='images/')
    group = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

class Add_user(models.Model):
    user_level = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)

class Video_Tutorial(models.Model):
    subject_name = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    video_url = models.TextField()

class Add_Exam(models.Model):
    package = models.CharField(max_length=30)
    name_of_exam = models.CharField(max_length=60)
    passing_percentage = models.IntegerField()
    instruction = models.CharField(max_length=70)
    syllabus = models.TextField()
    exam_duration = models.IntegerField()
    attempt_count = models.IntegerField()
    start_date = models.DateField(max_length=100)
    end_date = models.CharField(max_length=100)
    show_answer_sheet = models.CharField(max_length=10)
    negative_marking = models.CharField(max_length=10)
    browser_tolerance = models.CharField(max_length=10)
    result_after_finish = models.CharField(max_length=10)
    instant_result = models.CharField(max_length=10)
    multi_languages = models.CharField(max_length=10)
    select_group = models.CharField(max_length=100)
    random_question = models.CharField(max_length=10)
    mode = models.CharField(max_length=10)
    option_shuffle = models.CharField(max_length=10)


class PDF(models.Model):
    subject_name = models.CharField(max_length=100)
    topics_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    pdf_url = models.TextField()

class Center(models.Model):
    state_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)

class Coupons(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    coupons_amount = models.IntegerField()
    amount  =  models.CharField(max_length=100)
    coupons_order = models.CharField(max_length=100)
    couposn_code =models.CharField(max_length=100)
    no_of_coupons = models.CharField(max_length=100)
    user_per_customs= models.IntegerField()
    start_date = models.CharField(max_length=100)
    end_date  = models.CharField(max_length=100)


class Add_Subject(models.Model):
    group_name = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=100)


class Subject_Toexam(models.Model):
    subject = models.CharField(max_length=100, primary_key=True)
    no_of_question = models.IntegerField()
    question_attempt = models.IntegerField()
    question_type = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)


class Addsub_Topics(models.Model):
    sub_name = models.CharField(max_length=100)
    topic_name  = models.CharField(max_length=100)
    sub_topic = models.CharField(max_length=100)

class Topics(models.Model):
    subject_name =  models.CharField(max_length=100)
    topic_name =  models.CharField(max_length=100)

class add_video(models.Model):
    subject_Name = models.CharField(max_length=100)
    topic_Name = models.CharField(max_length=100)
    job_name = models.CharField(max_length=100)

class Add_group(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)




class Collegues(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
    bugs = models.TextField()
