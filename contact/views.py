from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print 'Sending mail from ' + request.POST.get('email', 'noreply@example.com') + ' to siteowner@example.com with subject "'+ request.POST['subject'] + '" with message "' + request.POST['message'] + '"...'
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={ 'subject': 'I love your site!' })
    return render(request, 'contact_form.html', { 'form': form })

def contact_thanks(request):
    return render(request, 'contact_thanks.html')