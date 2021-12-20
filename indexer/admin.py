from django.contrib import admin

from indexer.models import Network, Contract, Indexer, RangeBlock, Account, Trade, Mapping



@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('network_id', 'explorer_url')
    readonly_fields = ('network_id', 'explorer_url')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contract_type', 'start_block', 'end_block')
    readonly_fields = ('id', 'name', 'address', 'contract_type', 'start_block', 'end_block', 'network', 'abi')


@admin.register(Indexer)
class IndexerAdmin(admin.ModelAdmin):
    list_display = (
        'indexer_id', 'start_block', 'end_block', 'last_block', 'step', 'target_events_per_request', 'contract'
    )
    readonly_fields = (
        'indexer_id', 'start_block', 'end_block', 'last_block', 'step', 'target_events_per_request', 'contract'
    )


@admin.register(RangeBlock)
class RangeBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_block', 'last_block', 'step', 'count_events', 'contract', 'indexer', 'created_at')
    readonly_fields = ('first_block', 'last_block', 'count_events', 'contract', 'indexer', 'step', 'created_at')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('address', 'points')
    readonly_fields = ('address', 'points')


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'buyer', 'tx', 'block_number', 'block_hash', 'range_block')
    readonly_fields = ('id', 'seller', 'buyer', 'tx', 'block_number', 'block_hash', 'range_block')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Mapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'token', 'trade')
    readonly_fields = ('exchange', 'token', 'trade')


