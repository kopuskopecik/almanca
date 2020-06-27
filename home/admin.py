from django.contrib import admin

from .models import Setting, Partner, Service, Solution, Reference, Member, Contact, About, AboutLogo, Mission, Feature

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'icon', 'youtube_url','header', 'content', 'description']


class ServiceAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'font','image', 'content',]


class SolutionAdmin(admin.ModelAdmin):
		
	list_display = ['title', 'font','image', 'content',]

class ContactAdmin(admin.ModelAdmin):
		
	list_display = ["addresse"]




admin.site.register(Setting, SettingAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Member)
admin.site.register(About)
admin.site.register(AboutLogo)
admin.site.register(Mission)
admin.site.register(Partner)
admin.site.register(Feature)

	