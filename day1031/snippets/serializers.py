from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# 在序列化类中没有的字段，查询时得不到，新增也不需要提交这个字段
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # readonly GET 时需要，POST 时不需要
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'}) # style 是为了测试方便
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # validated 验证后的
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        # 现在这个函数好像没做什么，但是之后我们会填写自己的逻辑

        # 数据已经经过序列化的验证。若验证后想做一些自己的操作，然后再 save ，就可以在这里写代码
        return Snippet.objects.create(**validated_data)

    # instance 用来帮我们查出实例（想想 books/2 这个链接）
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # 如果前端提交为空，也不会赋空值，而是原来的值
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance