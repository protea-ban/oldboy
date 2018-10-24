from django.shortcuts import HttpResponse, render, redirect
from django.conf.urls import url


class ModelXadmin(object):
    # 存放要显示哪些字段的列表
    list_display = ["__str__", ]

    def __init__(self, model, site):
        self.model = model
        self.site = site

    def list_view(self, request):
        # 所有的数据
        data_list = self.model.objects.all()
        # 数据表的名称
        model_name = self.model._meta.model_name

        # 处理表头
        header_list = []

        # 为list_display的每个字段都添加相应的表头
        for field in self.list_display:

            # 字段为数据表自带
            if isinstance(field, str):
                # 默认list_display
                if field == '__str__':
                    val = self.model._meta.model_name.upper()
                else:
                    field_obj = self.model._meta.get_field(field)
                    val = field_obj.verbose_name
            # 字段为自添加函数
            else:
                # is_header判断是否在传表头时调用
                val = field(self, is_header=True)
            header_list.append(val)

        # 处理表单数据的列表
        new_data_list = []

        for data_obj in data_list:
            temp = []
            for field in self.list_display:
                # 取数据对象相应的字段
                if isinstance(field, str):
                    val = getattr(data_obj, field)
                else:
                    val = field(self, data_obj)
                temp.append(val)

            new_data_list.append(temp)

        return render(request,
                      "list_view.html",
                      {
                          "data_list": data_list,
                          "model_name": model_name,
                          "new_data_list": new_data_list,
                          "header_list": header_list,
                      }
                      )

    def add_view(self, request):
        return render(request, "add_view.html")

    def change_view(self, request, id):
        return render(request, "change_view.html")

    def delete_view(self, request, id):
        return render(request, "delete_view.html")

    def get_urls2(self):
        temp = []

        temp.append(url(r'^$', self.list_view))
        temp.append(url(r'^add/$', self.add_view))
        temp.append(url(r'^(\d+)/change/$', self.change_view, name="change"))
        temp.append(url(r'^(\d+)/delete/$', self.delete_view, name="delete"))

        return temp

    @property
    def urls2(self):
        return self.get_urls2(), None, None


class XadminSite(object):
    def __init__(self):
        self._registry = {}

    def get_urls(self):
        temp = []

        for model, admin_class_obj in self._registry.items():
            app_name = model._meta.app_label
            mode_name = model._meta.model_name

            temp.append(url(r'^{}/{}/'.format(app_name, mode_name), admin_class_obj.urls2))
        return temp

    @property
    def urls(self):
        return self.get_urls(), None, None

    def register(self, model, admin_class=None, **options):
        if not admin_class:
            admin_class = ModelXadmin

        self._registry[model] = admin_class(model, self)


site = XadminSite()
