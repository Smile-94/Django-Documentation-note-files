from django.contrib import admin
from app1.models import Person
from app1.models import Runner
from app1.models import Group
from app1.models import Membership
from app1.models import Info
from app1.models import Student

# Register your models here.
admin.site.register(Person)
admin.site.register(Runner)
admin.site.register(Group)
admin.site.register(Membership)
# admin.site.register(Info)
admin.site.register(Student)

# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display=('group_name',Membership)

