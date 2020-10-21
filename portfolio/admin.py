from django.contrib import admin
from portfolio.models import Message, Mail, Test

admin.site.register(( Mail, Test))

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Enter Email's Subject:", {'fields': ['subject']}),
        ("Enter Email's Body:", {'fields': ['message']}),
    ]

admin.site.register(Message, MessageAdmin)