from django.contrib import admin

from indexer.models import Indexer


@admin.register(Indexer)
class IndexerAdmin(admin.ModelAdmin):
    list_display = ('indexer_id', 'start_block', 'end_block', 'current_block')
