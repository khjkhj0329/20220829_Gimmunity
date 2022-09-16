from django.views.generic import ListView, DetailView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice #DB에서 notice 전체 가져와서
                    # notice_list라는 변수로
                    # notice_list.html 파일로 전달

class NoticeDetailView(DetailView):
    model = Notice  #DB에서 pk에 해당하는 notice 가져와서
                    # notice라는 변수로
                    #notice_detail.html 파일로 전달
