from django.contrib import admin
from .models import TodoList, Comment, TodoList_files, TodoList_images
# Register your models here.

class TodoList_imageInline(admin.StackedInline):
    model = TodoList_files

class TodoList_filesInline(admin.StackedInline):
    model = TodoList_images

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoList_filesInline, TodoList_imageInline]
    list_display = ('title', 'content', 'date_created', 'date_deadline')
    list_filter = ['date_created']

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Comment)

# admin.site.register(TodoList_images, TodoList_imageAdmin)
# admin.site.register(TodoList_files, TodoList_filesAdmin)

