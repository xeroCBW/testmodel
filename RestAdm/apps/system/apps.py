from django.apps import AppConfig

class SystemConfig(AppConfig):
    name = 'system'
    verbose_name = '系统'

    # 通过ready 来导入信号量
    def ready(self):
        import system.signals

