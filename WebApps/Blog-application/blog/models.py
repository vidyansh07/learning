from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)
    
    
class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT ='DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length = 255)
    discription = models.CharField(max_length = 255, default = 'This is a discription')
    author = models.ForeignKey(
        User,
        on_delete =models.CASCADE,
        related_name ="blog_posts",
    )
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices = Status.choices, default = Status.DRAFT)

    objects = models.Manager() # The default manager
    published = PublishManager() # The costom manager
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['publish']),
        ]
    
    def __str__(self):
        return self.title

# In the job application form, you can include the following fields:

# Job Title
# Job Description
# Company Information
# Location
# Salary/Compensation
# Application Deadline
# Application Form Fields
# Resume/CV Upload
# Cover Letter
# Contact Information
# References
# Equal Opportunity Employer (EOE) Information
# Privacy Policy
# Terms and Conditions
# Submit Button

# class Job(models.Model):
    
#     class Status(models.TextChoices):
#         DRAFT ='DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'
        
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length = 255)
#     discription = models.CharField(max_length = 255, default = 'This is a discription')
#     company = models.ForeignKey(
#         User,
#         on_delete =models.CASCADE,
#         related_name ="job_posts",
#     )
#     location = models.CharField(max_length = 255)
#     salary = models.CharField(max_length = 255)
#     application_deadline = models.DateTimeField(default = timezone.now())
#     application_form_fields = models.TextField()
#     resume_cv_upload = models.BooleanField(default = False)
#     cover_letter = models.BooleanField(default = False)
#     contact_information = models.BooleanField(default = False)
#     references = models.BooleanField(default = False)
#     equal_opportunity_employer = models.BooleanField(default = False)
#     privacy_policy = models.BooleanField(default = False)
#     terms_and_conditions = models.BooleanField(default = False)
#     submit_button = models.BooleanField(default = False)
#     created = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=2,choices = Status.choices, default = Status.DRAFT)
    
#     objects = models.Manager() # The default manager
#     published = PublishManager() # The costom manager
#     class Meta:
#         ordering = ['-created']
#         indexes = [
#             models.Index(fields=['created']),
#         ]
    
#     def __str__(self):
#         return self.title