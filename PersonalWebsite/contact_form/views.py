from django.shortcuts import render, HttpResponse
from contact_form.forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = request.POST.get('name')
            sender_email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            email = EmailMessage(
                    'Message From Website.',
                    message, sender_email, ['shresthaNischalLal@gmail.com', 'aakrist666@gmail.com', 'hi@nischal.info.np'],
                    headers  = {'Reply-To': sender_email}
                )
            email.send()

            # if sender_name and sender_email and subject and message:
            #     try:
            #         send_mail(subject, message, sender_email, ['shresthaNischalLal@gmail.com'],
            #         fail_silently=False,
            #         )
            #     except BadHeaderError:
            #         return HttpResponse("Bad Header")
            return render(request, 'contact_form/mail_received.html', {})
    form = ContactForm()
    return render(request, 'contact_form/contact_form.html', {'form':form})
       