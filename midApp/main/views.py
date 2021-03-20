from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from main.models import Book, Journal
from main.serializers import BookSerializer,  JournalSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'create':
            return Book.objects.all()
        return Journal.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return BookSerializer
        elif self.action == 'list':
            return JournalSerializer

    @action(methods=['get'], detail=True)
    def completed(self, request, *args, **kwargs):
        serializer = JournalSerializer(self.get_queryset().filter(id=kwargs['pk']), many=True
                                    )
        return Response(serializer.data)


