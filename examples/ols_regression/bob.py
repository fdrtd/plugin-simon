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


SECRET_BOB = [[17.0, 23.0, 45.0]]  # Bob has three observations of the single dependent
NETWORK_BOB = {**shared.NETWORK, 'myself': 1}  # Bob is no. 1 out of 0, 1.


if __name__ == "__main__":

    api = fdrtd.clients.python.Api(shared.URL_BOB)
    microservice = api.create(protocol="Simon")
    result = microservice.compute(microprotocol="StatisticsRegressionOLSVertical",
                                  data=SECRET_BOB,
                                  network=NETWORK_BOB,
                                  tokens=shared.TOKENS)
    print(api.download(result))
    # MLE should be [5, 6, 7]
