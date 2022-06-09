"""
secure sum example with SIMON (SImple Multiparty computatiON)

this example requires a shared network of three fdrtd servers.

the settings below describe a situation where they are all run on localhost,
on ports 55501, 55502, and 55503, respectively.

please see https://github.com/fdrtd/docs/wiki/how-to-run-a-fdrtd-server
and set up three local servers accordingly. or set them up elsewhere and
chance settings accordingly.

if you use public test servers or servers shared by other people,
you may want to set your own unique UUID as well.
"""


URL_ALICE = "http://127.0.0.1:55501"
URL_BOB = "http://127.0.0.1:55502"
URL_CHARLIE = "http://127.0.0.1:55503"

NETWORK = {'nodes': [URL_ALICE, URL_BOB, URL_CHARLIE]}
UUID = "387a7282-c380-44c9-aede-08da7e931931"  # unique identifier to match participants
