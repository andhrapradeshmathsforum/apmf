from django.forms import ModelForm
from . models import Video




class VideoForm(ModelForm):
    """Form definition for videos."""

    class Meta:
        """Meta definition for VideoForm."""

        model = Video
        fields = ('title','description','video')