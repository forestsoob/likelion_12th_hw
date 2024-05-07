from django.shortcuts import render
from .models import Post

# Create your views here.

def mypage(request):
# 현재 로그인한 사용자의 post만 필터링하여 가져옴
    posts = Post.objects.filter(writer=request.user)
    return render(request, 'users/mypage.html', {'posts': posts})