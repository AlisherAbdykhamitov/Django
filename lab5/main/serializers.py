from rest_framework import serializers

from auth_.serializers import MainUserSerializer
from main.models import Task, Todo


class TaskSerializer(serializers.ModelSerializer):

    owner = MainUserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'due', 'owner', 'completed')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        task = Task.objects.create(**validated_data)
        task.save()
        return task


class TodoSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('get_tasks')

    class Meta:
        model = Todo
        fields = ('id', 'name', 'tasks')

    def get_tasks(self, obj):
        only_completed = self.context.get("only_completed")
        tasks = Task.objects.filter(todo_id=obj.id)
        if only_completed:
            tasks = tasks.filter(completed=True)
        return TaskSerializer(tasks, many=True).data




