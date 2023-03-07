from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    banned_words = ['пьер', 'японии', 'париж', 'текст', 'олимпийск']
    original_text = value.split()

    bad_words = []
    for indx, word in enumerate(value.lower().split()):
        for bad_word in banned_words:
            if bad_word in word:
                bad_words.append(indx)
    for bad_word in bad_words:
        original_text[bad_word] = '*нехорошее слово*'

    return ' '.join(original_text)