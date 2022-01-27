#!/usr/bin/env python3

"""File holding utilities related to image processing.

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
import logging

from simple_steganography.decorators.notNone import NotNone

# endregion

# region Constants 
LOGGER = logging.getLogger(__name__)
# endregion

# region Logic
@NotNone()
def verify_payload(payload: str, img: any) -> None:
  """
  ----------------
  Verifies payload
  ----------------

  Checks if input image is big enough to write given payload in

  ----------
  Parameters
  ----------
  payload: str
    payload to write into image
  img: Image
    image object representing image into which payload is to be written
  ------
  Raises
  ------
  ValueError:
    if payload is too big for given image
  """
  max_bytes = (img.shape[0] * img.shape[1] * 3) // 8
  LOGGER.debug(f"Maximum bytes that can be encoded {max_bytes}")
  if len(payload) > max_bytes:
    LOGGER.error(f"Payload is too big (Max bytes: {max_bytes})")
    raise ValueError("Payload is too big")
# endregion
