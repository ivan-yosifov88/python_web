from django import template

from exam_prep.online_lib.views import get_profile

register = template.Library()


@register.simple_tag()
def profile_info():
    profile = get_profile()
    return profile
