from django.contrib import admin

from .models import * 

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=("name","number","email","message")
admin.site.register(contact,contactAdmin)

class magazinesAdmin(admin.ModelAdmin):
    list_display=("name","mpic","mdate","mfile")
admin.site.register(magazines,magazinesAdmin)

class frontAdmin(admin.ModelAdmin):
    list_display=("name","ppic","branch","lan","pdate","pfile")
admin.site.register(front,frontAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("id","cname","cpic","cdate")
admin.site.register(category,categoryAdmin)


class computerscienceAdmin(admin.ModelAdmin):
    list_display=("name","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(computerscience,computerscienceAdmin)

class mechanicalautomobileAdmin(admin.ModelAdmin):
    list_display=("name","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(mechanicalautomobile,mechanicalautomobileAdmin)

class mechanicalproductionAdmin(admin.ModelAdmin):
    list_display=("name","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(mechanicalproduction,mechanicalproductionAdmin)

class electronicsAdmin(admin.ModelAdmin):
    list_display=("name","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(electronics,electronicsAdmin)

class imageAdmin(admin.ModelAdmin):
    list_display=("name","img")
admin.site.register(image,imageAdmin)

## Notes Section Start here

class csnoteAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(csnote,csnoteAdmin)

class manoteAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(manote,manoteAdmin)

class eenoteAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(eenote,eenoteAdmin)

class mpnoteAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","lan","pdate","sem","pfile")
admin.site.register(mpnote,mpnoteAdmin)

### previous year peper  start here...##

class csqpAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","year","sem","pfile")
admin.site.register(csqp,csqpAdmin)

class maqpAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","year","sem","pfile")
admin.site.register(maqp,maqpAdmin)

class mpqpAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","year","sem","pfile")
admin.site.register(mpqp,mpqpAdmin)

class eeqpAdmin(admin.ModelAdmin):
    list_display=("subject","ppic","branch","year","sem","pfile")
admin.site.register(eeqp,eeqpAdmin)