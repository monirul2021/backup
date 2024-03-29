from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RestrictedEmail)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    search_fields = ['title','user__email','user__username']
    list_per_page = 100
admin.site.register(Blog,BlogAdmin)


admin.site.register(Category)
admin.site.register(Tag)



admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Site)

admin.site.register(Ugv_Ad)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Wishlist)

#report blog
class BlogReportAdmin(admin.ModelAdmin):
    list_display = ['reason','blog','user', 'status']
admin.site.register(BlogReport,BlogReportAdmin)


#trash
@admin.register(BlogTrash)
class BlogTrashAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'deleted_at']
    search_fields = ['title', 'user__username']
    date_hierarchy = 'deleted_at'


