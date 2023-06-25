from django.contrib import admin
from .models import MemberPosition, MemberTenure, CommitteeMember


admin.site.register(MemberPosition)
admin.site.register(MemberTenure)
admin.site.register(CommitteeMember)

