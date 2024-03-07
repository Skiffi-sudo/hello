from django.shortcuts import render

def hello_recruto(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить')
    context = {'name': name, 'message': message}
    return render(request, 'myapp/index.html', context)
