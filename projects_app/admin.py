from django.contrib import admin

from projects_app.models import Project

class ProjectAdmin(admin.ModelAdmin):
      fields=['projectname','summary']

admin.site.register(Project)


