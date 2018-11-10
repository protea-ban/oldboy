from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


# 组件Xadmin的配置类，在项目启动时进行加载
class XadminConfig(AppConfig):
    name = 'Xadmin'

    # 加载该类时自动执行ready函数
    def ready(self):
        # 扫描所有Xadmin的模块，启动完成后执行每个APP下的Xadmin文件
        autodiscover_modules('Xadmin')
