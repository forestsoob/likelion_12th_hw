from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Tag

# Create your views here.
def mainpage(request):
    context = {
        'generation': 12,
        'info':{'M': '데이터베이스와 상호작용 담당', 'T': '사용자와 상호작용 담당(보여지는 부분, 인터페이스)', 'V': '웹 서비스 내부 동작의 논리 담당(요청에 따른 적절한 로직 수행)'}
    }
    return render(request, 'main/mainpage.html', context)
def secondpage(request):
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html', {'posts': posts})
def new_post(request):
    return render(request, 'main/new-post.html')
def detail(request, id):
    post = get_object_or_404(Post, pk = id)

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post': post, 'comments': comments})
    
    if request.method == 'POST':
        if 'delete_comment_id' in request.POST:
            comment_id = request.POST['delete_comment_id']
            comment_to_delete = get_object_or_404(Comment, pk=comment_id)
            if request.user == comment_to_delete.writer:
                comment_to_delete.delete()
            return redirect('main:detail', id=id)
        
        elif 'content' in request.POST:
            new_comment = Comment(
                post=post,
                writer=request.user,
                content=request.POST['content'],
                pub_date=timezone.now()
            )
            new_comment.save()
            return redirect('main:detail', id=id)
    
def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post' : edit_post})
def create(request):
        if request.user.is_authenticated:
            new_post = Post()

            new_post.title = request.POST['title']
            new_post.writer = request.user
            new_post.body = request.POST['body']
            new_post.pub_date = timezone.now()
            new_post.image = request.FILES.get('image')
            new_post.weather = request.POST['weather']

            new_post.save()

            # 본문을 띄어쓰기 기준으로 나누기
            words = new_post.body.split(' ')
            tag_list = []

            for w in words:
                if len(w)>0:
                    if w[0] == '#':
                        tag_list.append(w[1:])

            for t in tag_list:
                tag, boolean = Tag.objects.get_or_create(name=t)
                new_post.tags.add(tag.id)

            return redirect('main:detail', new_post.id)

        else:
            return redirect('accounts:login')

def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.body = request.POST['body']
        update_post.pub_date = timezone.now()

        if 'weather' in request.POST:
            update_post.weather = request.POST['weather']

        if request.FILES.get('image'):
            update_post.image = request.FILES['image']

        update_post.save()
        return redirect('main:detail', update_post.id)
    return redirect('accounts:detail', update_post.id)



def delete(request, id):
    delete_post = Post.objects.get(pk=id)

    delete_post.delete()
    return redirect('main:secondpage')

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.user == comment.writer:
        comment.delete()
    return redirect('main:detail', id=post_id)


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', { 'tags' : tags })

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts
    })