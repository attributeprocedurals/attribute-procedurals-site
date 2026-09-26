from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import ContactForm


def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


def contact(request):
    if request.method != 'POST':
        return redirect('home')
    form = ContactForm(request.POST)
    if form.is_valid():
        obj = form.save()
        try:
            send_mail(
                subject=f'New Attribute Procedurals enquiry: {obj.project_type}',
                message=f'Name: {obj.name}\nEmail: {obj.email}\nCompany: {obj.company}\nProject type: {obj.project_type}\n\n{obj.message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_TO_EMAIL],
                fail_silently=True,
            )
        finally:
            messages.success(request, 'Thanks — your enquiry has been received.')
    else:
        messages.error(request, 'Please complete all required fields with valid information.')
    return redirect('/#contact')
