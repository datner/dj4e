from django.shortcuts import render

# Create your views here.

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    request.session['dj4e_cookie'] = '91c77393'
    return render(request, 'hello/index.html', { 'count': request.session['count'] }) 
