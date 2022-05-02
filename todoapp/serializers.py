from rest_framework import serializers

from todoapp.models import TODO

class TODOSerializer(serializers.ModelSerializer):

    class Meta:
        model=TODO
        fields="__all__"
        #fields=['title','description']
        #exclude=['created_on','is_active']