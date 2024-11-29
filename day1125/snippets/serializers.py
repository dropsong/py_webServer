from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.ModelSerializer):
#     # owner 是一个 User 对象
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
#     class Meta:
#         model = Snippet
#         # 顺序不要求
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner 是一个 User 对象
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        # 顺序不要求
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']