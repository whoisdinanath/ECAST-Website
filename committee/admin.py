from django.contrib import admin
from .models import CommitteeMember, SocialMedia

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


admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(SocialMedia)

