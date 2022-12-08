from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
# 메인 페이지
def index(request):
    return render(request, 'emotion/index.html', {'content' : 'content'})

# 영상 스트리밍 페이지
def main(request):
    # return render(request, 'feature/index.html')
    # 프레임 조정을 위한 값 전달
    content = {'fps': 1.2,'time_limit': 10 ,'data': None}
    return render(request, 'emotion/main.html', content)

# canvas를 통해 전송된 이미지 처리
def stream(request):
    if (request.method == 'POST'):
        try:
            frame_ = request.POST.get('image')
            # call model here?
            frame_=str(frame_)
            data=frame_.replace('data:image/jpeg;base64,','')
            data=data.replace(' ', '+')
            imgdata = base64.b64decode(data)
            filename = f'{"tmp"}.jpg'
            with open(filename, 'wb') as f:
                f.write(imgdata)
        except:
            print('Error')

    # return JsonResponse({'Json':data})
    return JsonResponse({'Json':frame_})

# 기능 추가를 위한 테스트 페이지
def test(request):
    return render(request, 'emotion/test.html', {'content':'content'})
