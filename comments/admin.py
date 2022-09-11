from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from comments.models import Comment


class CommentMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Comment, CommentMPTTModelAdmin)
