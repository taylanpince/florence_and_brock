from django.contrib import admin

from documents.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp")


admin.site.register(Document, DocumentAdmin)