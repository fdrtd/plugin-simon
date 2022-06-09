"""
OLS regression on vertically partinioned data
with fdrtd plugin 'Simon' (SImple Muliparty computatiON)

1. run fdrtd servers (see shared.py)
2. run alice.py, bob.py, and charlie.py simultaneously
"""


import representation
import shared


SECRET_ALICE = [[[1.0, 2.0, 0.0],
                 [2.0, 1.0, 1.0],
                 [0.0, 4.0, 3.0]]]  # Alice has three observations of three independents
NETWORK_ALICE = {**shared.NETWORK, 'myself': 0}  # Alice's server is node #0 of the shared network


if __name__ == "__main__":

    api = representation.Api(shared.URL_ALICE)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="StatisticsRegressionOLSVertical",
                                  data=SECRET_ALICE,
                                  network=NETWORK_ALICE,
                                  uuid=shared.UUID)
    print(api.download(result))
    # MLE should be [5, 6, 7]
