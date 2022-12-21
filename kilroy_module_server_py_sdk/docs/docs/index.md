# kilroy-module-server-py-sdk

SDK for kilroy module servers in Python 🧰

## Installing

Using `pip`:

```sh
pip install kilroy-module-server-py-sdk
```

## Usage

```python
from pathlib import Path
from kilroy_module_server_py_sdk import Module, ModuleService, ModuleServer

class MyModule(Module):
    ... # Implement all necessary methods here

module = await MyModule.build()
service = ModuleService(module, Path("path/to/state/directory"))
server = ModuleServer(service)

await server.run(host="0.0.0.0", port=11000)
```
