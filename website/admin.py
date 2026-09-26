from django.contrib import admin
from .models import (
    ContactMessage,
    Project,
    ResearchProject,
    Insight,
    Technology,
    TeamMember,
    SiteSetting,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'status', 'is_read', 'created_at')
    list_filter = ('status', 'project_type', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status', 'is_read')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'is_published', 'published_at')
    list_filter = ('is_featured', 'is_published', 'category')
    search_fields = ('title', 'summary', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'research_area', 'status', 'is_published', 'published_at')
    list_filter = ('research_area', 'status', 'is_published')
    search_fields = ('title', 'summary', 'methodology')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_at')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'excerpt', 'body', 'author')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sort_order', 'is_visible')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'category')
    list_editable = ('sort_order', 'is_visible')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'sort_order', 'is_visible')
    list_filter = ('is_visible', 'role')
    search_fields = ('name', 'role', 'bio')
    list_editable = ('sort_order', 'is_visible')


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')
    search_fields = ('key', 'value', 'description')
