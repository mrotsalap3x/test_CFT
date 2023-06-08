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
            CreditRequest(title="CFT Credit Request 3", contract=contracts[1]),
        ]
        save_list(requests)
        producers = [
            Producer(title="CFT Producer 1"),
            Producer(title="CFT Producer 2"),
            Producer(title="CFT Producer 3"),
            Producer(title="CFT Producer 4"),
            Producer(title="CFT Producer 5"),
            Producer(title="CFT Producer 6"),
            Producer(title="CFT Producer 7"),
        ]
        save_list(producers)
        products = [
            Product(title="CFT Product 01", producer=producers[0], request=requests[0]),
            Product(title="CFT Product 02", producer=producers[0], request=requests[2]),
            Product(title="CFT Product 03", producer=producers[1], request=requests[1]),
            Product(title="CFT Product 04", producer=producers[1], request=requests[2]),
            Product(title="CFT Product 05", producer=producers[2], request=requests[1]),
            Product(title="CFT Product 06", producer=producers[2], request=requests[1]),
            Product(title="CFT Product 07", producer=producers[2], request=requests[0]),
            Product(title="CFT Product 08", producer=producers[3], request=requests[1]),
            Product(title="CFT Product 09", producer=producers[3], request=None),
            Product(title="CFT Product 10", producer=producers[4], request=requests[1]),
            Product(title="CFT Product 11", producer=producers[4], request=requests[1]),
            Product(title="CFT Product 12", producer=producers[5], request=requests[0]),
            Product(title="CFT Product 13", producer=producers[5], request=requests[0]),
            Product(title="CFT Product 14", producer=producers[6], request=requests[2]),
        ]
        save_list(products)
