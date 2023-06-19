from django.contrib import admin
from .models import MemberPosition, MemberTenure, CommitteeMembers


admin.site.register(MemberPosition)
admin.site.register(MemberTenure)
admin.site.register(CommitteeMembers)
