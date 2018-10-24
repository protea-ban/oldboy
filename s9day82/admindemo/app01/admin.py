from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.safestring import mark_safe


# 创建一个类，用来设置在admin中的显示
class BookConfig(admin.ModelAdmin):

    def deletes(self):
        return mark_safe("<a href=''>删除</a>")

    def patch_init(self, request, queryset):
        queryset.update(price=100)

    # 设置批量处理动作的描述名称
    patch_init.short_description = "批量初始化"

    # 在展示页面会显示哪些字段内容,除了已有的字段，还可以添加自定义函数为字段显示
    list_display = ["title", "price", "publishDate", "publish", deletes]
    # 设置哪些字段内容转成可点击的链接，转到更改页面
    list_display_links = ["title", "price"]
    # 设置可以用哪些字段进行分组过滤
    list_filter = ["title", "price", "publish"]
    # 设置可以按照哪些字段进行搜索
    search_fields = ["title", "price"]
    # 设置批量处理的动作
    actions = [patch_init]

# 注册model时，可以加入显示参数
admin.site.register(Book, BookConfig)
admin.site.register(Publish)
admin.site.register(Author)
admin.site.register(AuthorDetail)

