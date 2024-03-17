from django.contrib import admin
from .models import  Post

@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','discription','author','publish','status']
    list_filter =['status','publish','created','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':  ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    # these are optional fields that are not required 

# @admin.register(Job)
# # Register your models here.
# class JobAdmin(admin.ModelAdmin):
#     list_display = ['job_title','company','location','salary','application_deadline','status']
#     list_filter = ['status','created','update','company']
#     search_fields = ['job_title','location','company']
#     prepopulated_fields = {'slug':  ('job_title',)}
#     date_hierarchy = 'created'
#     ordering = ['status','created']
#     filter_horizontal = ['application_form_fields']
#     fieldsets = (
#         (None, {
#             'fields': ('job_title','slug','discription','company','location','salary','application_deadline','application_form_fields','resume_cv_upload','cover_letter','contact_information','references','equal_opportunity_employer','privacy_policy','terms_and_conditions','submit_button')
#         }),
#         ('Status', {
#             'fields': ('status',)
#         }),
#     )
#     actions = ['make_published']
#     def make_published(self, request, queryset):
#         queryset.update(status = Job.Status.PUBLISHED)
#     make_published.short_description = "Mark selected stories as published"

# The following is the code for the admin.py file.