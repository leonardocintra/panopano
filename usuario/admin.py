from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', ]
    readonly_fields = ('user',)


admin.site.register(Cliente, ClienteAdmin)
