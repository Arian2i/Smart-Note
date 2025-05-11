from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import NoteSerializer, TagSerializer
from .models import Note, Tag


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('created_at')
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer    