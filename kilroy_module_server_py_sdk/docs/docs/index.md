# kilroy-module-server-py-sdk

SDK for kilroy module servers in Python 🧰

## Installing

Using `pip`:

```sh
pip install kilroy-module-server-py-sdk
```

## Usage

```python
from kilroy_module_server_py_sdk import Module, ModuleServer

class MyModule(Module):
    ... # Implement all necessary methods here

module = await MyModule.build()
server = ModuleServer(module)

await server.run(host="0.0.0.0", port=11000)
```
