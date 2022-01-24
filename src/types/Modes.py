#!/usr/bin/env python3

"""Type representing modes in which can be script run.

----------
Since:
  1.0
----------
------------
Version:
  1.0
------------
---------------
Author:
  Karafra
---------------
"""

# region Imports
from enum import Enum
# endregion

# region Logic
class Modes(Enum):
  """
  ----------
  Modes enum
  ----------
  Enum for modes in which script can be run
  
  ----------
  Attributes
  ----------
  ENCODE : str
    encode mode
  DECODE: str
    decode mode
  """
  DECODE = "decode"
  ENCODE = "encode"

  def __str__(self) -> str:
      """String representation of mode
      -------
      Returns
      -------
      string: str
        string representation of given mode
      """
      return self.value
# endregion