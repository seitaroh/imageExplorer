from rest_framework import serializers

from .models import Image, Video, Card, Main, Page, Address, Zoo, Animal

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class MainSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Main
        fields = ['title', 'cards']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
