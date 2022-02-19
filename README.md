![license](https://img.shields.io/github/license/fdrtd/simon)
![CodeQL](https://github.com/fdrtd/simon/workflows/CodeQL/badge.svg)
![unittest](https://raw.githubusercontent.com/fdrtd/simon/main/.github/badges/tests.svg)
![Pylint](https://raw.githubusercontent.com/fdrtd/simon/main/.github/badges/pylint.svg)


# description

`simon` is a **SI**mple **M**ultiparty computati**ON** protocol for `fdrtd`

# server-side installation

    pip install fdrtd
    pip install fdrtd-simon
    python -m fdrtd.webserver --port=...

# client-side usage

```python
import fdrtd.client

api = fdrtd.client.Api("https://...")
simon = api.create(protocol="Simon")
result = simon.compute(microprotocol=...,
                       data=...,
                       network=...,
                       tokens=...)
print(api.download(result))
```
