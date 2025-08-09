from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline

# class MultiImageInline(admin.TabularInline):
#     model = MultiImage
#     extra = 1

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     inlines = [MultiImageInline]
#     prepopulated_fields = {"slug": ("title",)}

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     inlines = [MultiImageInline]
#     prepopulated_fields = {"slug": ("title",)}

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     inlines = [MultiImageInline]
#     prepopulated_fields = {"slug": ("title",)}

# admin.site.register(MultiImage)


# # @admin.register(Service)
# # class ServiceAdmin(admin.ModelAdmin):
# #     prepopulated_fields = {"slug": ("title",)}
# #     list_display = ("title", "is_active")
# #     list_filter = ("is_active",)
    
# admin.site.register(AgencyMeta)
# # admin.site.register(Blog)
# admin.site.register(Lead)
# admin.site.register(CookieConsentSetting)
# # @admin.register(Project)
# # class ProjectAdmin(admin.ModelAdmin):
# #     list_display = ('title', 'client_name', 'date_completed', 'is_featured')
# #     prepopulated_fields = {'slug': ('title',)}
# #     search_fields = ['title', 'technologies_used', 'client_name']
# #     list_filter = ['is_featured', 'date_completed']

# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ('title', 'subtitle', 'is_active')
#     list_filter = ('is_active',)
#     search_fields = ('title', 'subtitle')

# Inline for MultiImage
class MultiImageInline(admin.TabularInline):
    model = MultiImage
    extra = 1

# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "is_active")
    list_filter = ("is_active",)

# Blog Admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "is_featured", "created_at")
    list_filter = ("is_featured", "created_at")

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [MultiImageInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'client_name', 'date_completed', 'is_featured')
    list_filter = ['is_featured', 'date_completed']
    search_fields = ['title', 'technologies_used', 'client_name']

# MultiImage Admin
@admin.register(MultiImage)
class MultiImageAdmin(admin.ModelAdmin):
    list_display = ("get_parent", "order", "image")
    list_filter = ()
    search_fields = ("alt_text",)

    def get_parent(self, obj):
        return obj.service or obj.blog or obj.project
    get_parent.short_description = "Parent Object"

# Other models
admin.site.register(AgencyMeta)
admin.site.register(Lead)
admin.site.register(CookieConsentSetting)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
