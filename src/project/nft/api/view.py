from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from project.nft.api.serializers import ProfileSerializer
from project.nft.models import Profile
from django.shortcuts import get_object_or_404


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        wallet = self.kwargs.get('wallet')
        return get_object_or_404(Profile, wallet=wallet)
