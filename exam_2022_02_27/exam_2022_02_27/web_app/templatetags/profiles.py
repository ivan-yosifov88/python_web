from django import template

from exam_2022_02_27.web_app.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0
