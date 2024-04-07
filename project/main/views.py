from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 12,
        'info':{'M': '데이터베이스와 상호작용 담당', 'T': '사용자와 상호작용 담당(보여지는 부분, 인터페이스)', 'V': '웹 서비스 내부 동작의 논리 담당(요청에 따른 적절한 로직 수행)'}
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {'members': ['현아찌', '호연오라방'],
            'family':{'1': '젤 어르신 구독', '2': '앙큼담당 진우', '3':'오빠 장발로 돌아와 호연', '4':'동갑인데 언니 현아', '5':'내가 낳을걸 효은이', '6': '대망의 감자수빈'}
               }
    return render(request, 'main/secondpage.html', context)