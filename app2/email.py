from django.template import context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings


def send_review_email(name, email, review):
    context = {"name": name, "email": email, "review": review}
    email_subject = "Thanks you for your Review"
    html_content = render_to_string("email_message.txt", context)
    # email = EmailMessage(email_subject, email_body, "kalideveloper865@gmail.com")
    print(context)
    email_sent = send_mail(
        email_subject,
        review,
        settings.DEFAULT_FROM_EMAIL,
        [
            email,
        ],
        html_message=html_content,
    )
    return email_sent
    # return email.send(fail_silently=False)
