from rest_framework import serializers
from .models import UserFb
from services import obter_dados_userFb


class UserFbSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFb
        fields = ('fb_id',)

    def create(self, instance):
        dados = obter_dados_userFb(instance['fb_id'])
        return UserFb.objects.create(**dados)
