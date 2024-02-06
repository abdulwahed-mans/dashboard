from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "user",
            "postal_code",
            "address",
            "personal_identity_number",
            "city",
            "profile_picture",
            "language_preference",
            "phone_number",
            "bio",
        ]

        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
            # أضف المزيد من التخصيصات حسب الحاجة
        }

        labels = {
            'bio': 'Biography',
            # أضف تخصيصات العناوين لحقول أخرى حسب الحاجة
        }

        help_texts = {
            'bio': 'A brief introduction about yourself.',
            # أضف نصوص توضيحية لحقول أخرى حسب الحاجة
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # تخصيص queryset لحقل المستخدم إذا كنت بحاجة إلى تحديد المستخدمين من قائمة
        self.fields['user'].queryset = User.objects.all()
        # يمكن إضافة تخصيصات إضافية للحقول هنا إذا لزم الأمر
