from django.conf.urls import url,include
from api.views import course, account, shoppingcar, payment

urlpatterns = [
    # 方式一 分配两个url
    # url(r'^course/$', CourseView.as_view()),
    # url(r'^course/(?P<pk>\d+)/$', CourseView.as_view()),

    # 方式二 用list和retrieve函数分配url
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),


    url(r'^auth/$', account.AuthView.as_view()),
    url(r'^micro/$', course.MicroView.as_view()),
    url(r'^shoppingcar/$', shoppingcar.ShoppingCarViewSet.as_view()),
    url(r'^payment/$', payment.PaymentViewSet.as_view())
]
