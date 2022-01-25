#!/usr/bin/env python3

"""Simple steganography command line utility

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
from typing import Dict
import argparse
import logging

from .convert import decode, encode
from src.types.Modes import Modes

# endregion

# region CLI stuff
__version__ = 1.0
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-m", "--mode", type=Modes,
                    choices=list(Modes), metavar="decode", required=True)
PARSER.add_argument("-p", "--payload", type=str, metavar="Test message")
PARSER.add_argument("-o", "--output", type=str, metavar="output.png")
PARSER.add_argument("-i", "--input", type=str,
                    metavar="inputFile.png", required=True)
LOGGER = logging.getLogger(__name__)
# endregion

# region CLI runner
if __name__ == "__main__":
    args: Dict[str, any] = PARSER.parse_args()
    logging.basicConfig(level=logging.DEBUG,
                        format=" %(name)s :: %(levelname)-8s :: %(message)s")
    if args.mode == Modes.ENCODE:
        if not args.payload:
            raise ValueError("Payload is required")
        elif not args.output:
            raise ValueError("output file is required")
        elif not args.output.endswith(".png"):
            raise ValueError("Output file has to be png")
        encode(args.input, args.payload, args.output)
    elif args.mode == Modes.DECODE:
        if not args.input.endswith(".png"):
            raise ValueError("Input file has to be png")
        decode(args.input)
# endregion
