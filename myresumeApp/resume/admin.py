from django.contrib import admin
from . models import Profile,Experience,Educations,Certification,Projects

# # Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['picture']
#
#
# admin.site.register(Profile, ProfileAdmin)
#
#
# class ExperienceAdmin(admin.ModelAdmin):
#
#     list_display = ['jobposition','companyname','description','startdate','enddate']
# admin.site.register(Experience,ExperienceAdmin)
#
#
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ['university', 'degree', 'startdate', 'enddate']
#
#
# admin.site.register(Educations, EducationAdmin)

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Educations)

admin.site.register(Certification)
admin.site.register(Projects)

