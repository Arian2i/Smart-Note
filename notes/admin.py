from django.contrib import admin
from .models import Note, Tag


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'pinned', 'is_archived', 'created_at']
    list_filter = ['pinned', 'is_archived']
    search_fields = ['title', 'content']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

