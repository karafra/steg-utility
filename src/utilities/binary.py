#!/usr/bin/env python3

"""Utilities related to binary

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
from typing import List, Union
import numpy as np
# endregion 

# region Logic
def message2binary(message: Union[str, bytes, np.ndarray, int, np.uint8]) -> Union[str, List[str]]:
  """Utility function for converting strings into their bit representation
  ----------
  Parameters
  ----------
  message: str
    Message to be converted into bitlike format
  -------
  Returns
  -------
  str
    bit like representation of given string
  ------
  Raises
  ------
  TypeError
    when type of message is nor string, int like or bytelike object.
  """
  if type(message) == str:
      result = ''.join([format(ord(char), "08b") for char in message])
  elif type(message) in (bytes, np.ndarray):
      result = [format(char, "08b") for char in message]
  elif type(message) in (int, np.uint8):
      result = format(message, "08b")
  else:
      raise TypeError("Input type is not supported")
  return result
# endregion
