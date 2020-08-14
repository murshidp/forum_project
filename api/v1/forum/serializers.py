from rest_framework import serializers
from forum.models import Forum,Subforum,Thread
from django.contrib.auth.models import User


class ForumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forum
        fields = ('id','master')


class SubforumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subforum
        fields = ('id','forum','name')

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ('title','description','haederimage')
        read_only_fields = ('id','forum_category')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password')


    


       

