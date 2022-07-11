from django.shortcuts import render
import random
import datetime

users = {}

def index(request):
    print(users)
    user_id = request.COOKIES.get('user_id')
    session = users.get(user_id)
    if not session:
        user_id = str(random.randint(100000,999999))
        
        users[user_id] = {
            'count': 1,
            'start_time': datetime.datetime.now()
        }
    else:
        users[user_id]['count'] += 1
    response = render(request, 'counter_app/index.html', users[user_id])
    response.set_cookie('user_id', user_id)
    return response
