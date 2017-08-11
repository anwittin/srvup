from django.contrib import admin

# Register your models here.
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_filter = ['title','timestamp', 'updated']
    list_display = ['title','timestamp', 'updated']
    readonly_fields = ['updated', 'timestamp', 'short_title']
    search_fields = ['title']
    class Meta:
        model = Video

    def short_title(self, obj):
        return obj.title[:3]

admin.site.register(Video, VideoAdmin)