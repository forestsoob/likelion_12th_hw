from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from main.models import Post

# Create your views here.

# 현재 로그인한 사용자의 post만 필터링하여 가져옴
def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    current_user = request.user
    followings = user.profile.followings.all()
    followers = user.profile.followers.all()

    context = {
        'user':user,
        'current_user': current_user,
        'followings':followings,
        'followers':followers,

}
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', id=followed_user.id)