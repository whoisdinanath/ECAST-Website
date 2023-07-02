from django.contrib import admin
from .models import MemberPosition, CommitteeMember, SocialMedia

class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    extra = 4

class CommitteeMemberAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline]
    list_display = ['name', 'position']
    list_filter = ['name', 'position']
    search_fields = ['name', 'position']

class CommitteeMemberInline(admin.StackedInline):
    model = CommitteeMember
    extra = 3

class PositionAdmin(admin.ModelAdmin):
    inlines = [CommitteeMemberInline]
    list_display = ['position']
    search_fields = ['position']

admin.site.register(MemberPosition, PositionAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(SocialMedia)

