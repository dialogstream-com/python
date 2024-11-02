"""
dialogstream
~~~~~~~~~~~~~~~~~~~

A flexible stream routing and filtering system with support for scheduled tasks and event reactions.

:copyright: (c) 2024 by pipexy
:license: MIT, see LICENSE for more details.
"""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from .main import main
from .process import Process
from .router import Router
from .process_utils import ProcessUtils

__all__ = ['main', 'Process', 'Router', 'ProcessUtils']
