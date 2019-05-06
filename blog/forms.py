from django.forms import ModelForm
from blog.models import Post


class Updateform(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
