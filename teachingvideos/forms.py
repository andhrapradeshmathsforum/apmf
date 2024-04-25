from django.forms import ModelForm
from . models import Teachingvideo




class TeachingvideoForm(ModelForm):
    """Form definition for Teachingvideos."""

    class Meta:
        """Meta definition for TeachingvideoForm."""

        model = Teachingvideo
        fields = ('standard','title','description','video')