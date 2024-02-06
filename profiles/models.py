from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Profile(models.Model):
    # Relationships
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))

    # Personal Information
    personal_identity_number = models.CharField(_("Personal Identity Number"), max_length=12, unique=True)
    bio = models.TextField(_("Biography"), null=True, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=True)
    language_preference = models.CharField(_("Language Preference"), max_length=10, choices=[('sv', _('Swedish')), ('en', _('English'))], default='sv')
    
    # Address Fields
    address = models.CharField(_("Address"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=50, blank=True)
    postal_code = models.CharField(_("Postal Code"), max_length=10, blank=True)
    
    # Media
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='profile_pics/', null=True, blank=True)
    
    # Metadata
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        return reverse("profiles_Profile_detail", args=[self.pk])

    def get_update_url(self):
        return reverse("profiles_Profile_update", args=[self.pk])
