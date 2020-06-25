# Description

Gobits is a very small module, which acts as a metadata carrier for pub/sub messages. It automatically adds fields that may be useful downstream to determine the origin of a pub/sub message.

# Usage

Cloud function with http trigger:

```python
from gobits import Gobits


def handler(request):

    bits = Gobits(request=request)

    message = {
      'gobits': bits,
      'data': 'message-to-send'
    }

```

Cloud funciton with storage trigger:

```python
from gobits import Gobits


def handler(data):

    bits = Gobits(data=data)

    message = {
      'gobits': bits,
      'data': 'message-to-send'
    }

```
