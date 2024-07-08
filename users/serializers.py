from rest_framework import serializers
from posts.models import Post
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id','username', 'nickname', 'email', 'gender', 'age', 'profile_image', 'password', 'followers_count', 'following_count', 'posts_num']
        extra_kwargs = {
            'username': {'write_only': True, 'error_messages': {'blank': '아이디를 입력해야 합니다.'}},
            'password': {'write_only': True, 'error_messages': {'blank': '비밀번호를 입력해야 합니다.'}},
            'nickname': {'error_messages': {'blank': '닉네임을 입력해야 합니다.'}},
            'email': {'error_messages': {'blank': '이메일을 입력해야 합니다.'}},
            'age': {'error_messages': {'invalid': '나이를 선택해야 합니다.'}},
        }

    # 유저의 포스트 개수
    def get_posts_num(self, obj):
        return Post.objects.filter(user=obj).count()
    # 유저의 팔로워 수
    def get_followers_count(self, obj):
        return obj.followers.count()
    # 유저의 팔로잉 수
    def get_following_count(self, obj):
        return obj.followings.count()

    def create(self, validated_data):
        # 비밀번호를 해시 처리하여 저장
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
