from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        from test_task.models import Contract, CreditRequest, Producer, Product

        def get_producers_by_contract(contract_id):
            credit_request = CreditRequest.objects.get(contract_id=contract_id)
            #  this .distinct() clause is not supported by sqlite3 engine, will work on mysql or postgresql
            # products = credit_request.product_set.distinct("producer_id").values_list("producer_id")
            # return [p[0] for p in products]
            #  to work around this nuance in sqlite I'll use python set
            products = credit_request.product_set.values_list("producer_id")
            return [p[0] for p in set(products)]


        print(get_producers_by_contract(32812))
