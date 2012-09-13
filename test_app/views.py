from django import forms
from django import shortcuts

from django.utils.safestring import mark_safe

from models import *

class FooForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        widgets = {
            'name': forms.Textarea(attrs={'placeholder': u'Bla bla'}),
        }

def foo(request):
    if request.method == 'POST':
        form = FooForm(request.POST)
        form.is_valid()
    else:
        form = FooForm()

    return shortcuts.render(request, 'foo.html', {'form': form})
