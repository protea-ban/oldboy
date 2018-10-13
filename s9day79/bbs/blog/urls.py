from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'up_down/', views.up_down),
    # 文章详情页的url
    url(r'(\w+)/article/(\d+)/$', views.article_detail),
    url(r'(\w+)/', views.home),

]