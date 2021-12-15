from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=42, unique=True)
    abi = models.JSONField()
    start_block = models.IntegerField()
    end_block = models.IntegerField()
#
# class RangeBlock(models.Model):
#     first_block = models.IntegerField(unique=True)
#     last_block = models.IntegerField(unique=True)
#     count_events = models.IntegerField()
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
#
#
# class Account(models.Model):
#     address = models.CharField(max_length=42, unique=True)
#
#
# class Trade(models.Model):
#     seller = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='seller_of')
#     buyer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='buyer_of')
#     tx = models.CharField(max_length=200, unique=True)
#     block = models.ForeignKey(RangeBlock, on_delete=models.CASCADE)


class Indexer(models.Model):
    indexer_id = models.IntegerField(unique=True)
    start_block = models.IntegerField()
    end_block = models.IntegerField()
    last_block = models.IntegerField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    step = models.IntegerField()
    target_events_per_request = models.IntegerField(default=1000)
