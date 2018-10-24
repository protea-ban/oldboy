from django.shortcuts import HttpResponse, render, redirect
from django.conf.urls import url


class ModelXadmin(object):
    def __init__(self, model, site):
        self.model = model
        self.site = site

    def list_view(self, request):

        data_list = self.model.objects.all()
        return render(request, "list_view.html", locals())

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
        temp.append(url(r'^(\d+)/change/$', self.change_view))
        temp.append(url(r'^(\d+)/delete/$', self.delete_view))

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
