from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for the Profile class"""

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    