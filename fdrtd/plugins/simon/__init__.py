from fdrtd.plugins.simon.microservice import MicroserviceSimon


def get_classes():
    return [
        {
            "identifiers": {
                "namespace": "fdrtd",
                "protocol": "Simon",
                "version": "0.1.1"
            },
            "class": MicroserviceSimon()
        }
    ]
