from django.contrib import admin

from indexer.models import Contract, Indexer, RangeBlock, Account, Trade, Token


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'start_block', 'end_block')


@admin.register(Indexer)
class IndexerAdmin(admin.ModelAdmin):
    list_display = (
        'indexer_id', 'start_block', 'end_block', 'last_block', 'step', 'target_events_per_request', 'contract'
    )


@admin.register(RangeBlock)
class RangeBlockAdmin(admin.ModelAdmin):
    list_display = ('first_block', 'last_block', 'count_events', 'contract', 'indexer', 'created_at')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('address', 'points')


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'buyer', 'tx', 'block_number', 'block_hash', 'range_block')


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'start_block', 'end_block', 'coefficient')
