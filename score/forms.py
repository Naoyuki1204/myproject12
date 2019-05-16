from django import forms
from.models import game


class GameForm(forms.ModelForm):
    class Meta:
        model = game
        fields = ['gamename','score','keioS','keioV','eteam','eS','eV','date']
        
        
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)# -*- coding: utf-8 -*-
