"""
secure sum example with Simon (SImple Multiparty computatiON)

1. run fdrtd servers (see shared.py)
2. run alice.py, bob.py, and charlie.py simultaneously
"""


import representation
import shared


SECRET_ALICE = 42.0  # Alice's secret input
NETWORK_ALICE = {**shared.NETWORK, 'myself': 0}  # Alice's server is node #0 of the shared network


if __name__ == "__main__":

    api = representation.Api(shared.URL_ALICE)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="SecureSum",
                                  data=SECRET_ALICE,
                                  network=NETWORK_ALICE,
                                  uuid=shared.UUID)
    print(api.download(result))
