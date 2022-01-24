#!/urs/bin/env python3

"""Type representing RGB color components with order in pixel

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
from enum import IntEnum
# endregion

class RGB(IntEnum):
  """
  --------
  RGB enum
  --------
  Enum that represents color components in each pixel.

  Attributes
  ----------
  RED: int
    index of red component in pixel
  GREEN: int
    index of green component
  BLUE: int
    index of blue component in pixel
  """
  RED = 0;
  GREEN = 1;
  BLUE = 2;