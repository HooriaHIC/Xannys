from django import template
import random

register = template.Library()


@register.simple_tag
def random_quote():
    my_strings = ['Be yourself', 'Unique and Unrepeatable', 'Just do it',
                  'Start where you are. Use what you have. Do what you can', 'Believe you can and you’re halfway there', 'If you can dream it, you can do it.', 'Being unique is better than being perfect', 'There is only one you in all time', 'Enjoy life', 'Be happy', 'Dream Big', "Don't Stop", 'Let it go', 'Be a giver', 'Block out haters', 'All is well', 'Never give up', 'Nobody is perfect', 'You are enough', 'Smile. Sparkle. Shine', 'Winners never quit']
    return random.choice(my_strings)
