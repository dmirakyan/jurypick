from django.contrib import admin
from jurorsearch.models import Query, Human, UserDetail

# Register your models here.


class QueryAdmin(admin.ModelAdmin):
    readonly_fields = ['search_id']
    def display_id(self, obj):
        return obj.id

class HumanAdmin(admin.ModelAdmin):
    readonly_fields = ['search_id']
    def display_id(self, obj):
        return obj.id



    # UserDetail
# class QueryAdmin(admin.ModelAdmin):
#     readonly_fields = ('search_id',)


# admin.site.register(QueryAdmin)
admin.site.register(Query,QueryAdmin)
admin.site.register(Human,HumanAdmin)
admin.site.register(UserDetail)

