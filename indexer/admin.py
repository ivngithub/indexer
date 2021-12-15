from django.contrib import admin

from indexer.models import Indexer, Contract


@admin.register(Indexer)
class IndexerAdmin(admin.ModelAdmin):
    list_display = ('indexer_id', 'start_block', 'end_block', 'last_block', 'step')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'start_block', 'end_block')

