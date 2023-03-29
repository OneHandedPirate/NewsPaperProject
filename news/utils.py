from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string

from environ import EMAIL


def get_filter_params(request):
    temp = {p: v for p, v in request.GET.copy().items() if p != 'page'}
    if any([not not v for v in temp.values()]):
        return ''.join([f'&{p}={v}' for p, v in temp.items() if v])
    else:
        return None

def send_sub_emails(post):
    subscribers = User.objects.filter(categorysubscriber__category__in=post.category.all()).distinct()
    html_content = render_to_string(
        'news/email/new_post_email.html',
        {
            'title': post.title,
            'text': post.text,
            'id': post.id,
            'category': ', '.join(map(str, post.category.all())),
        }
    )
    emails = []
    for sub in subscribers:
        msg = EmailMultiAlternatives(
            subject=f'Здравствуй, {sub}. Новая статья в твоём любимом разделе!',
            from_email=EMAIL,
            to=[sub.email],
        )

        msg.attach_alternative(html_content, "text/html")
        emails.append(msg)

    #Игнорируем ошибки, в частности - некорректные email-адреса.
    connection = get_connection(fail_silently=True)
    connection.send_messages(emails)
