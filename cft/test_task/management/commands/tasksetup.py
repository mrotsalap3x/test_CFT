from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        from test_task.models import Contract, CreditRequest, Producer, Product

        def save_list(objects: list = None):
            for o in objects:
                o.save()

        #  Setup models
        contracts = [
            Contract(title="CFT Contract 1"),
            Contract(id=32812, title="CFT Contract 2"),
            Contract(title="CFT Contract 3"),
        ]
        save_list(contracts)
        requests = [
            CreditRequest(title="CFT Credit Request 1", contract=contracts[0]),
            CreditRequest(title="CFT Credit Request 2", contract=contracts[1]),
        ]
        save_list(requests)
        producers = [
            Producer(title="CFT Producer 1"),
            Producer(title="CFT Producer 2"),
            Producer(title="CFT Producer 3"),
            Producer(title="CFT Producer 4"),
        ]
        save_list(producers)
        products = [
            Product(title="CFT Product 1", producer=producers[0], request=requests[0]),
            Product(title="CFT Product 2", producer=producers[0], request=None),
            Product(title="CFT Product 3", producer=producers[1], request=requests[1]),
            Product(title="CFT Product 4", producer=producers[1], request=requests[0]),
            Product(title="CFT Product 5", producer=producers[2], request=requests[1]),
            Product(title="CFT Product 6", producer=producers[2], request=requests[1]),
            Product(title="CFT Product 7", producer=producers[2], request=requests[0]),
            Product(title="CFT Product 8", producer=producers[3], request=requests[1]),
            Product(title="CFT Product 9", producer=producers[3], request=None),
        ]
        save_list(products)
