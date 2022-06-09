"""
OLS regression on vertically partinioned data
with fdrtd plugin 'Simon' (SImple Muliparty computatiON)

this example requires a shared network of two fdrtd servers.

the settings below describe a situation where they are all run on localhost,
on ports 55501 and 55502, respectively.

please see https://github.com/fdrtd/docs/wiki/how-to-run-a-fdrtd-server
and set up two local servers accordingly. or set them up elsewhere and
chance settings accordingly.

if you use public test servers or servers shared by other people,
you may want to set your own unique UUID as well.
"""


URL_ALICE = "http://127.0.0.1:55501"
URL_BOB = "http://127.0.0.1:55502"

NETWORK = {'nodes': [URL_ALICE, URL_BOB]}
UUID = "60293b2d-e375-40c5-96ea-1e4c85a2012e"  # unique identifier to match participants
