from django import forms
from courier.models import CouriersReview


class CouriersReviewForm(forms.ModelForm):
    class Meta:
        model = CouriersReview
        fields = ['body']
        labels = {
            'body': "Your review"
        }
