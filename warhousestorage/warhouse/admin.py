from django.contrib import admin
from warhouse.models import Rodzajdokumentu


class RodzajdokumentuAdmin(admin.ModelAdmin):
						fieldset = [
							(None,			{'fields': ['nazwa']})
						],
						list_filter = ['nazwa']
						
						#list_display = ('nazwa',)
						#list_filter = ['nazwa']
						#search_fields = ['nazwa']

admin.site.register(Rodzajdokumentu,RodzajdokumentuAdmin)