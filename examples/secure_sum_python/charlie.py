"""
secure sum example with SIMON (SImple Multiparty computatiON)

1. run fdrtd servers (see shared.py)
2. run alice.py, bob.py, and charlie.py simultaneously
"""


import representation
import shared


SECRET_CHARLIE = 99.0  # Charlie's secret input
NETWORK_CHARLIE = {**shared.NETWORK, 'myself': 2}  # Charlie's server is node #2 of the shared network


if __name__ == "__main__":

    api = representation.Api(shared.URL_CHARLIE)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="SecureSum",
                                  data=SECRET_CHARLIE,
                                  network=NETWORK_CHARLIE,
                                  uuid=shared.UUID)
    print(api.download(result))
