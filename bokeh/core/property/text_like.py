#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' ``TextLike`` is a shortcut for properties that accepts strings, parsed
strings, and text-like objects, e.g.:

* :class:`~bokeh.models.text.MathText`
* :class:`~bokeh.models.text.PlainText`

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from typing import TYPE_CHECKING, Any

# Bokeh imports
from .bases import Init, Property
from .either import Either
from .instance import Instance
from .singletons import Intrinsic
from .string import MathString

if TYPE_CHECKING:
    from ...models.text import BaseText

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    "TextLike",
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class TextLike(Either):
    """ Accept a string that may be interpreted into text models or the models themselves.

    """

    def __init__(self, default: Init[str | BaseText] = Intrinsic, help: str | None = None) -> None:
        types: list[Property[Any]] = [MathString(), Instance("bokeh.models.text.BaseText")]
        super().__init__(*types, default=default, help=help)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
