![license](https://img.shields.io/github/license/fdrtd/simon)


# description

`simon` is a **SI**mple **M**ultiparty computati**ON** protocol for `fdrtd`

# server-side installation

    pip install fdrtd
    pip install fdrtd-simon
    python -m fdrtd.webserver --port=...

# client-side usage

```python
import representation

api = representation.Api("http://localhost:...")
simon = api.create(protocol="Simon")
result = simon.compute(microprotocol=...,
                       data=...,
                       network=...,
                       tokens=...)
print(api.download(result))
```
