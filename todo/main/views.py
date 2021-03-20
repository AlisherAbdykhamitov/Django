from django.shortcuts import render


def dataBase():
    tasks = []
    for i in range(5):
        complete = False
        if i == 0:
            complete = True
        tasks.append({
            "name": "Task {}".format(i),
            "created": "11/12/2018",
            "due": "15/12/2018",
            "owner": "admin",
            "complete": complete
        })
    return tasks


def todo_tasks(request):
    tasks = dataBase()
    tasks = [i for i in tasks if not i["complete"]]
    context = {"tasks": tasks, "complete": False}
    return render(request, 'todo_list.html', context=context)


def completed_tasks(request):
    tasks = dataBase()
    tasks = [i for i in tasks if i["complete"]]
    context = {"tasks": tasks, "complete": True}
    return render(request, 'todo_list_start.html', context=context)