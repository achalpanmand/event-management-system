from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Registration, Speaker, Gallery
from .form import RegistrationForm, FeedbackForm
import uuid

def event_list(request):
    events = Event.objects.all()
    return render(request,'eventlist.html', {'events': events})

def register_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.ticket_code = str(uuid.uuid4())[:8]
            registration.save()
            return render(request, 'ticket.html', {'registration': registration})
    else:
        form = RegistrationForm(initial={'event': event})
    return render(request, 'register.html', {'form': form, 'event': event})

def event_schedule(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'schedule.html', {'event': event})

def speakers(request, event_id):
    speakers = Speaker.objects.filter(event_id=event_id)
    return render(request, 'speakers.html', {'speakers': speakers})

def gallery(request, event_id):
    gallery = Gallery.objects.filter(event_id=event_id)
    return render(request, 'gallery.html', {'gallery': gallery})

def feedback(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.event = event
            fb.save()
            return redirect('event_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'event': event})

def search_event(request):
    query = request.GET.get('q')
    events = Event.objects.filter(title__icontains=query)
    return render(request, 'event_list.html', {'events': events})

def filter_events(request, category):
    events = Event.objects.filter(category=category)
    return render(request, 'event_list.html', {'events': events})
