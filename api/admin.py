from django.contrib import admin
from .models import Transaction, Profile, Currency


class CurrencyInline(admin.TabularInline):
    model = Currency

class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        CurrencyInline,
    ]

admin.site.register(Transaction)
admin.site.register(Profile)
admin.site.register(Currency)
