from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(required=False, allow_blank=True, max_length=100)
    pubdate = serializers.DateField(required=False, allow_blank=True,)
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.pubdate = validated_data.get('pubdate', instance.pubdate)
        instance.save()
 
        return instance

class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question =serializers.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = serializers.CharField(required=False, allow_blank=True, max_length=100)
    votes = serializers.IntegerField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance