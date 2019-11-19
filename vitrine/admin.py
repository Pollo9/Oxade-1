from django.contrib import admin

# Register your models here.

from .models import *

class Bdd_evenementAdmin(admin.ModelAdmin):
	search_fields = ['titre']
	list_display = ('id','titre','texte','img','date')

class Bdd_mailAdmin(admin.ModelAdmin):
	search_fields = ['mail']
	list_display = ('id','mail')


admin.site.register(Bdd_mail,Bdd_mailAdmin)

admin.site.register(Bdd_evenement,Bdd_evenementAdmin)
