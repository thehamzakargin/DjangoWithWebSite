from django.contrib import admin
from .models import syntheticPlayer, categories

# Register your models here.
@admin.register(syntheticPlayer)
class syntheticPlayerAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category_list")
    list_display_links = ("title","slug",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title","isActive")
    list_editable = ("isActive",)
    search_fields = ("title","descriptions")

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html
        
@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = ("name","slug","subscriptions_count")
    prepopulated_fields = {"slug": ("name",),}
    def subscriptions_count(self, obj):
        return obj.syntheticplayer_set.count()
    
