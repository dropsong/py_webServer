from rest_framework import serializers
from guide.models import Album, Comment, Event, Event1, Account, Track
from django.contrib.auth.models import User

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    # content = serializers.ChoiceField(choices=[100, 101])
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def validate_content(self, value):
        """
        Check that the comment is about nihao.
        """
        if 'nihao' not in value.lower():
            raise serializers.ValidationError("not about nihao")
        return value


class EventSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = ['id', 'description', 'start', 'finish']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}} # 如果没有这句，会露出密码(密文)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['album', 'order', 'title', 'duration']


import time
# 自定义关系字段，之前都是 CharField 之类的，这里我们自定义
class TrackListingField(serializers.RelatedField):
    # 改变查询时显示的样式
    def to_representation(self, value):
        # 时长格式： 秒 -> 几分几秒
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return 'Track %d: %s (%s)' % (value.order, value.title, duration)

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackListingField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']