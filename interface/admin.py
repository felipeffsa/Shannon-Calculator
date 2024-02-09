from django.contrib import admin
from interface.models import Pi,LogPi,MultLogPi,Dados
# Register your models here.

admin.site.register(Pi)
admin.site.register(LogPi)
admin.site.register(MultLogPi)
admin.site.register(Dados)