"""
OLS regression on vertically partinioned data
with fdrtd plugin 'Simon' (SImple Muliparty computatiON)

1. run fdrtd servers (see shared.py)
2. run alice.py, bob.py, and charlie.py simultaneously
"""


import representation
import shared


SECRET_BOB = [[17.0, 23.0, 45.0]]  # Bob has three observations of the single dependent
NETWORK_BOB = {**shared.NETWORK, 'myself': 1}  # Bob's server is node #1 of the shared network


if __name__ == "__main__":

    api = representation.Api(shared.URL_BOB)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="StatisticsRegressionOLSVertical",
                                  data=SECRET_BOB,
                                  network=NETWORK_BOB,
                                  uuid=shared.UUID)
    print(api.download(result))
    # MLE should be [5, 6, 7]
