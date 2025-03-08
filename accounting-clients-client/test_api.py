from accounting_clients_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://accounting-clients.api.datev.de/platform-sandbox/v2",
                             token="ZDdlOWY2YzktMTBkZC00NDA4LWI3YzEtYWM0YzA0NjhjOGViOzJkYzFhZTczYmIyMTBlYmFhM2RmMDRjNzAzZWM3NzlkO2huUDhCL1lqbUtEbXVGSzIyaTIzVjBuMFZram0zNFprZmpYRWNxejUwR009",
                             headers={
                                        "x-datev-client-id": "2dc1ae73bb210ebaa3df04c703ec779d"
                                    })

from accounting_clients_client.models import Client
from accounting_clients_client.api.clients import get_clients
from accounting_clients_client.types import Response

with client as client:
    my_data: Client = get_clients.sync(client=client)
    print(my_data)
    response: Response[Client] = get_clients.sync_detailed(client=client)
    print(response)