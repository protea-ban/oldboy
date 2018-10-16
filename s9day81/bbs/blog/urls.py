from django.conf.urls import url
from blog import views


urlpatterns = [
    # 添加文章用的url
    url(r'backend/add_article/', views.add_article),
    url(r'up_down/', views.up_down),
    url(r'comment/', views.comment),
    url(r'comment_tree/(\d+)/', views.comment_tree),
    # 文章详情页的url
    url(r'(\w+)/article/(\d+)/$', views.article_detail),
    url(r'(\w+)/', views.home),

]