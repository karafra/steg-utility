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

import cv2

from src.decorators.notNone import NotNone
from src.types.ColorComponents import RGB
from src.utilities.binary import message2binary
from src.utilities.stegUtils import verify_payload

# endregion 

# region Constants
LOGGER = logging.getLogger(__name__)
# endregion

# region Logic
@NotNone()
def encode(input_path: any, payload: str, output_path: str, terminator: str = "#####") -> None:
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
                return LOGGER.info(f"Saved as {output_path}")
              bit = payload_finalized.pop(0)
              pixel[component.value] = int(
                bit_encoded[component.value][:-1] + bit,
                2
              )


@NotNone()
def decode(input_path: any, terminator: str = "#####") -> None:
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
# endregion
