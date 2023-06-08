from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        from test_task.models import Contract, CreditRequest, Producer, Product

        def get_producers_by_contract(contract_id):
            #  with other db engines except sqlite we can use .distinct("producer_id") clause to
            #  get unique IDs right from the database, but with sqlite I'll use python dicts
            credit_requests = CreditRequest.objects\
                .filter(contract_id=contract_id)\
                .select_related("product")\
                .values_list("product__producer_id")

            return {cr[0]: cr[0] for cr in credit_requests}.values()


        print(get_producers_by_contract(32812))
