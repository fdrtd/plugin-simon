"""
OLS regression on vertically partinioned data
with fdrtd plugin 'Simon' (SImple Muliparty computatiON)

two fdrtd servers are needed for this example.
one for Alice, and one for Bob.
the easiest way is to run them all on localhost:

    pip install fdrtd
    pip install fdrtd-simon
    python -m fdrtd.webserver --port=55501 &
    python -m fdrtd.webserver --port=55502 &

then, the two scripts of Alice and Bob may be executed simultaneously.
"""


import fdrtd.clients.python
import shared


SECRET_ALICE = [[[1.0, 2.0, 0.0],
                 [2.0, 1.0, 1.0],
                 [0.0, 4.0, 3.0]]]  # Alice has three observations of three independents
NETWORK_ALICE = {**shared.NETWORK, 'myself': 0}    # Alice is no. 0 out of 0, 1.


if __name__ == "__main__":

    api = fdrtd.clients.python.Api(shared.URL_ALICE)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="StatisticsRegressionOLSVertical",
                                  data=SECRET_ALICE,
                                  network=NETWORK_ALICE,
                                  tokens=shared.TOKENS)
    print(api.download(result))
    # MLE should be [5, 6, 7]
