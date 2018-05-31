from django.shortcuts import render, redirect
from .models import User, Message
from django.contrib import messages

def home(request):
    if 'user_id' not in request.session:
        messages.add_message(request, messages.ERROR, "You have to log in first")
        return redirect('/')
    
    if request.method == 'GET':
        users = User.userManager.all().exclude(id=request.session['user_id']) 
        #excludes current user from populating in the option box....can't send message to yourself...
        user = User.userManager.get(id=request.session['user_id'])

        sent_messages = user.from_user.all()
        received_messages = user.to_user.all()
    
        for msg in sent_messages:
            users = users.exclude(id=msg.user_to_id)
        for msg in received_messages:
            users = users.exclude(id=msg.user_from_id)
        # the for loops exclude users from the list that you already have a conversation with
        
        context = {
            'users': users,
            'user': user
        }
        return render(request, 'message_app/home.html', context)
    
    elif request.method =='POST':
        print Message.messageManager.send(request.POST['message'], request.session['user_id'], request.POST['user_to'])
        return redirect('/home')

def chat(request, user_id):
    if request.method == 'GET':
        sent_messages = Message.messageManager.filter(user_from_id=request.session['user_id']).filter(user_to_id=user_id)
        
        received_messages = Message.messageManager.filter(user_to_id=request.session['user_id']).filter(user_from_id=user_id)
        
        conversation = [msg for msg in sent_messages] +[msg for msg in received_messages]

        conversation.sort(key=lambda x: x.created_at) #sorts conversation to chronological order

        context = {
            'conversation': conversation,
            'user_id': user_id
        }
        return render(request, 'message_app/chat.html', context)

    elif request.method == 'POST':
        print Message.messageManager.send(request.POST['message'], request.session['user_id'], user_id)
        return redirect('/chat/{}'.format(user_id))



       