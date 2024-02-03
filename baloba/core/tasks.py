from celery import shared_task
from core.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from product.models import Product
from datetime import timedelta
from users.models import User

# @shared_task
# def send_mail_to_subscribers():
#     # This code is calculating the start and end dates for a time period of 7 days ago.
#     startdate = timezone.now()
#     enddate = startdate - timedelta(days=7)
#     subscriber_emails =  Subscriber.objects.values_list('email', flat=True)
#     most_rev = Product.objects.filter(created__gte=enddate)
#     for mail in subscriber_emails:
#         body = render_to_string('email-subscribers.html', context={
#             'email': mail,
#             'most_rev': most_rev
#         })
#         msg = EmailMessage(subject='Subscriber mail', body=body,
#                            from_email=settings.EMAIL_HOST_USER,
#                            to=[mail, ])
#         msg.content_subtype = 'html'
#         msg.send(fail_silently=True)
        
# @shared_task
# def one_month_message():
#     startdate = timezone.now()
#     enddate = startdate - timedelta(days=30)
#     month_most_rev = Product.objects.filter(created__gte=enddate)
#     users = User.objects.all()
#     for user in users:
#         body = render_to_string('last_login_email.html', context={
#             'email': user,
#             'month_most_rev': month_most_rev
#         })
#         msg = EmailMessage(subject='Last login mail', body=body,
#                            from_email=settings.EMAIL_HOST_USER,
#                            to=[user, ])
#         msg.content_subtype = 'html'
#         msg.send(fail_silently=True)

@shared_task
def send_mail_to_subscribers():
    # startdate = timezone.now()
    # enddate = startdate - timedelta(days=7)
    subscribers_emails = Subscriber.objects.values_list("email", flat=True)
    most_rev = Product.objects.all()

    # most_rev = Product.objects.filter(created_at__gte=enddate).annotate(num_coms=Count("product_review")).order_by("-num_coms")[0:2]
    for mail in subscribers_emails:
        body = render_to_string("email-subscribers.html", context={
            'email':mail,
            'most_rev': most_rev
        })
        msg = EmailMessage(subject='Subscriber mail', body=body,
                           from_email=settings.EMAIL_HOST_USER,
                           to=[mail, ])
        msg.content_subtype = "html"
        msg.send(fail_silently=True)
    
    return 'completed...'