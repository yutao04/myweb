from django.shortcuts import render

#test.pyが開いたらtest.htmlが開かれる
def test(request):
    return render(request, 'test.html')