from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_html_email(subject,
                    text_template,
                    html_template,
                    context,
                    to_emails,
                    from_email=settings.DEFAULT_EMAIL):

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)

    email = EmailMultiAlternatives(subject,
                                   text_content,
                                   from_email,
                                   to_emails)

    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=True)
