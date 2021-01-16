from django.contrib import admin


admin.site.index_title="Todo Admin"
admin.site.site_title="Todo Admin"
admin.site.site_header='Welcome to Todo Admin'


from .models import Group,Item
# admin.site.register(Group)

class ItemInline(admin.TabularInline):
    model=Item
    extra=1


class GroupAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['title']}),
    ]

    inlines=[ItemInline]

admin.site.register(Group,GroupAdmin)

