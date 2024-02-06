from rest_framework import serializers
from .models import Profile  # تأكد من أن هذا يشير إلى النموذج الصحيح في تطبيقك

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # يشير إلى نموذج Profile الذي تريد تسلسله
        fields = ['user', 'postal_code', 'address', 'personal_identity_number', 'city', 'profile_picture', 'language_preference', 'phone_number', 'bio']
  # يضمن تضمين جميع الحقول في النموذج، أو يمكنك تحديد قائمة الحقول يدويًا مثل ['user', 'postal_code', ...]
