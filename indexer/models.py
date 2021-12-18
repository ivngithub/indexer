from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=42, unique=True)
    abi = models.JSONField()
    start_block = models.IntegerField()
    end_block = models.IntegerField()


class Token(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=42, unique=True)
    abi = models.JSONField()
    start_block = models.IntegerField()
    end_block = models.IntegerField()
    coefficient = models.IntegerField(default=1)


class Indexer(models.Model):
    indexer_id = models.IntegerField()
    start_block = models.IntegerField()
    end_block = models.IntegerField()
    last_block = models.IntegerField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    step = models.IntegerField()
    target_events_per_request = models.IntegerField(default=1000)


class RangeBlock(models.Model):
    first_block = models.IntegerField()
    last_block = models.IntegerField()
    step = models.IntegerField()
    count_events = models.IntegerField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    indexer = models.ForeignKey(Indexer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    address = models.CharField(max_length=42, unique=True)
    points = models.IntegerField(default=0)


class Trade(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='seller_of')
    buyer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='buyer_of')
    tx = models.CharField(max_length=200, unique=True)
    block_number = models.IntegerField()
    block_hash = models.CharField(max_length=200)
    range_block = models.ForeignKey(RangeBlock, on_delete=models.CASCADE)

