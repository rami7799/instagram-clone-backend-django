from django import forms

# Models
from .models import Post


class PostForm(forms.ModelForm):
	"""Post model form"""

	class Meta:
		"""Form settings."""
		model = Post
		fields = ('profile', 'title', 'photo')