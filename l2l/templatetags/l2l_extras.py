from django import template
from datetime import datetime

register = template.Library()

def l2l_dt(value):
    if isinstance(value, str):
        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

    return value.strftime("%Y-%m-%d %H:%M:%S")

register.filter('l2l_dt', l2l_dt)