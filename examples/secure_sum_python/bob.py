"""
secure sum example with SIMON (SImple Multiparty computatiON)

1. run fdrtd servers (see shared.py)
2. run alice.py, bob.py, and charlie.py simultaneously
"""


import representation
import shared


SECRET_BOB = 16.0  # Bob's secret input
NETWORK_BOB = {**shared.NETWORK, 'myself': 1}  # Bob's server is node #1 of the shared network


if __name__ == "__main__":

    api = representation.Api(shared.URL_BOB)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="SecureSum",
                                  data=SECRET_BOB,
                                  network=NETWORK_BOB,
                                  uuid=shared.UUID)
    print(api.download(result))
