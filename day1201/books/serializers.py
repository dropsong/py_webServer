from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from books.models import BookInfo

class BookInfoSerializer(serializers.ModelSerializer):
    # 和 models.py 不能冲突
    btitle = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=BookInfo.objects.all())])

    # 显示登录的用户（仅展示功能，这个效果意味不明）
    owner = serializers.CharField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        # 当前序列化器在序列化数据的时候,使用哪个模型
        model = BookInfo
        fields = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'owner']