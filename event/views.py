from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'event/index.html')


def about(request):
    return render(request, 'event/about.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message = request.POST['message']

        message = message + '\n\nFrom :- ' + message_email + '\n' + message_name
        # send mail
        if message_name != "" and message_email != "" and message_subject != "":
            send_mail(message_subject, message, message_email,
                      ['invictus.bsss@gmail.com'])

        return render(request, 'event/contact.html', {})

    return render(request, 'event/contact.html', {})


def contact_thanks(request):
    return render(request, 'event/contact2.html')


def events(request):
    return render(request, 'event/events.html', {})


def cultural_events(request):
    return render(request, 'event/cultural.html', {})


def informal_events(request):
    return render(request, 'event/informal.html', {})


def finearts_events(request):
    return render(request, 'event/finearts.html', {})


def formal_events(request):
    return render(request, 'event/formal.html', {})


def literary_events(request):
    return render(request, 'event/literary.html', {})
