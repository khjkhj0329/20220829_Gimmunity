from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)  #내용이 없어도 괜찮아요
    create_at = models.DateTimeField(auto_now_add=True) # 데이터 생성 시 날짜 시간 기록
    modify_at = models.DateTimeField(auto_now=True) # 데이터 수정 시 날짜 시간 기록

    class Meta:
        ordering = ('-modify_at', '-create_at', 'title')    #수정시간 내림, 생성시간 내림, 제목 오름

    def __str__(self):
        return f'{self.title} | {self.content}'