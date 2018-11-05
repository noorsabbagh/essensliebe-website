from django.shortcuts import render, Http404, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from .models import DirectMessage
from .forms import ComposeForm, ReplyForm
import datetime
from django.contrib import  messages




# Create your views here.

def view_direct_message(request, dm_id):
    message = get_object_or_404(DirectMessage, id=dm_id)
    if not message.sender != request.user or message.receiver != request.user:
        raise Http404

    if not message.read:
        message.read = True
        message.read_at = datetime.datetime.now()
        message.save()
    direct_message = DirectMessage.objects.get_num_unread_message(request.user)
    request.session['num_of_message']= direct_message
    return render(request, 'directmessage/view.html', locals())




def compose(request):
    title = "<h1>Compose</h1>"
    form = ComposeForm(request.POST or None)
    if form.is_valid():
        send_message = form.save(commit=False)
        send_message.sender = request.user
        send_message.sent = datetime.datetime.now()
        send_message.save()
        return HttpResponseRedirect(reverse('inbox'))

    return render(request, 'directmessage/compose.html', locals())


def reply(request, dm_id):
    parent_id=dm_id
    parent = get_object_or_404(DirectMessage, id=parent_id)
    title = "<h1>Reply <small>to %s from %s</small></h1>" %(parent.subject, parent.sender)
    form = ReplyForm(request.POST or None)
    if form.is_valid():
        send_message = form.save(commit=False)
        send_message.sender = request.user
        send_message.receiver = parent.sender
        send_message.subject = "Re: " + parent.subject
        send_message.sent = datetime.datetime.now()
        send_message.parent = parent
        send_message.save()
        parent.replied = True
        parent.save()
        path = reverse('view_direct_message', args=(dm_id,))
        return HttpResponseRedirect(path)

    return render(request, 'directmessage/compose.html', locals())





def inbox(request):
    messages_in_inbox = DirectMessage.objects.filter(receiver=request.user)
    direct_message = DirectMessage.objects.get_num_unread_message(request.user)
    request.session['num_of_message']= direct_message
    return render(request, 'directmessage/inbox.html', locals())



def sent(request):
    messages_sent = DirectMessage.objects.filter(sender=request.user)

    return render(request, 'directmessage/sent.html', locals())
