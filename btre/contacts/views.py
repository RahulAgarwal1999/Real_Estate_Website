from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request, 'Your request has been submitted, a realtor will get back to you soon')
                return redirect('/listings/'+listing_id)

        # Saving the data from the inquiry form in the model in the database
        contact=Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        # Send mail
        # Format
        # def send_email(request):
        #     subject = request.POST.get('subject', '')
        #     message = request.POST.get('message', '')
        #     from_email = request.POST.get('from_email', '')
        #     if subject and message and from_email:
        #         try:
        #             send_mail(subject, message, from_email, ['admin@example.com'])
        #         except BadHeaderError:
        #             return HttpResponse('Invalid header found.')
        #         return HttpResponseRedirect('/contact/thanks/')
        #     else:
        #         # In reality we'd use a form class
        #         # to get proper validation errors.
        #         return HttpResponse('Make sure all fields are entered and valid.')

        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for '+listing+'. Sign into the admin panel for more info',
        #     'rahul@gmail.com',
        #     [realtor_email,'rahul.agarwal@gmail.com'],
        #     fail_silently=False
        # )


        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
