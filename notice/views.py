from django.views.generic import ListView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice #DB에서 notice 전체 가져와서
                    # notice_list라는 변수로
                    # notice_list.html 파일로 전달

