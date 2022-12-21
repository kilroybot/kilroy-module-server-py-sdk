# Usage

You can use this package to easily create a module server
that complies with the **kilroy** module API.

The easiest way to do this is to create a class
that inherits from `Module` class and implement all the necessary methods.
All methods are either simple coroutines or async generators.

Here is an example:

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
