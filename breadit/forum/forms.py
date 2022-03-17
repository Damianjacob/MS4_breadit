from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Form
from .models import Post, Comment
from crispy_forms.layout import Submit


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'video']


class EditPostform(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# class CommentForm(Form):
#     model = Comment
#     fields = ['content']
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'post_comment'
#         self.helper.form_class = 'blueForms'
#         self.helper.form_method = 'post'
#         self.helper.form_action = ''

#         self.helper.add_input(Submit('submit', 'Submit'))


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )