__version__ = "0.23.0"

from .client import LLMWhispererClient  # noqa: F401
from .client_v2 import LLMWhispererClientV2  # noqa: F401


def get_llmw_py_client_version():
    """Returns the SDK version."""
    return __version__
