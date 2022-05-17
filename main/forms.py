from django import forms
from .models import Comment


class CommentInputForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author','content']
        widgets = {
            'content':forms.Textarea(attrs={
                'style':'color:red;resize:none;',
                'placeholder':'please enter comment',
                'value':''
            })
        }