from django.db import models


# Create your models here.
class CFTBase(models.Model):
    """ Abstract base model """
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Contract(CFTBase):
    """ CFT Contract """
    pass


class CreditRequest(CFTBase):
    """ CFT Credit Request """
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)


class Producer(CFTBase):
    """ CFT Goods Producer """
    pass


class Product(CFTBase):
    """ CFT Product """
    request = models.ForeignKey(CreditRequest, on_delete=models.SET_NULL, null=True, blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
