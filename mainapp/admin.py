from django.contrib import admin
from .models import *
# Register your models here.
# from ckeditor_uploader.widgets import CKEditorUploadingWidget


# class PostAdminForm(forms.ModelForm):
#     photo = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = News
#         fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    # form = AddNewsForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog)
