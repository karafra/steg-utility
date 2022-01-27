#!/usr/bin/env python3

"""Convertors
File storing functions for encoding and decoding messages into/from images

--------
Version: 1.0
------------
----------
Since: 1.0
----------
---------------
Author: Karafra
---------------
"""

# region Imports
import logging
from typing import Optional

import cv2

from simple_steganography.decorators.notNone import NotNone
from simple_steganography.types.ColorComponents import RGB
from simple_steganography.utilities.binary import message2binary
from simple_steganography.utilities.stegUtils import verify_payload

# endregion 

# region Constants
LOGGER = logging.getLogger(__name__)
# endregion

# region Logic
@NotNone()
def encode(input_path: any, payload: str, output_path: str, terminator: str = "#####") -> str:
    """
    ------
    Encode
    ------

    Encodes string into given image and saves as output image.

    ----------
    Parameters
    ----------
    img: any
      image to which payload is to be hidden
    pyaload: str
      payload to hide
    output: str
      path to output file
    terminator: str (optional)
      terminator of message
    --------
    Returns:
      path to output file
    --------
    """
    # Check is payload can fit into image
    img = cv2.imread(input_path)
    verify_payload(payload, img)
    
    BINARY_DATA = message2binary(payload)
    LOGGER.debug(f"Binary payload: {BINARY_DATA}")
    
    # Append terminator and convert payload to list
    payload_finalized = list(message2binary(payload + terminator))
    for line in img:
        for pixel in line:
            bit_encoded = message2binary(pixel)
            for component in list(RGB):
              if not payload_finalized:
                cv2.imwrite(output_path, img)
                LOGGER.info(f"Saved as {output_path}")
                return output_path
              bit = payload_finalized.pop(0)
              pixel[component.value] = int(
                bit_encoded[component.value][:-1] + bit,
                2
              )


@NotNone()
def decode(input_path: any, terminator: str = "#####") -> Optional[str]:
  """
  -------------
  Decodes image
  -------------

  Decodes image and returns message hidden in it if any exists

  ----------
  Parameters
  ----------
  img: any
    image object to check for information
  teminator: str
    terminator of message
  --------
  Returns:
  --------
    Encoded message
  """
  img = cv2.imread(input_path)
  retrieved_data = ""
  for line in img:
      for pixel in line:
          bit_encoded = message2binary(pixel)
          for component in list(RGB):
            retrieved_data += bit_encoded[component.value][-1]
  all_bytes = [
    retrieved_data[i: i+8] for i in range(0, len(retrieved_data), 8)
  ]
  decoded_data = ""
  for byte in all_bytes:
      # Convert from base 2
      decoded_data += chr(int(byte, 2))
      # Check if terminator was reached.
      if decoded_data[-5:] == terminator:
          break
  logging.info(f"Encoded data : {decoded_data[:-5]}")
  try:
    return decoded_data[:-5]
  except IndexError as err:
    LOGGER.error(str(err))
    return ""
 
# endregion
