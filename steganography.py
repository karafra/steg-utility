#!/usr/bin/env python3

# region Imports
from enum import Enum
from typing import Dict
import numpy as np
import cv2
import argparse
import logging
# endregion

# region CLI stuff
class Modes(Enum):
    DECODE = "decode"
    ENCODE = "encode"

    def __str__(self) -> str:
        return self.value


PARSER = argparse.ArgumentParser()
PARSER.add_argument("-m", "--mode", type=Modes,
                    choices=list(Modes), metavar="decode", required=True)
PARSER.add_argument("-p", "--payload", type=str, metavar="Test message")
PARSER.add_argument("-o", "--output", type=str, metavar="output.png")
PARSER.add_argument("-i", "--input", type=str,
                    metavar="inputFile.png", required=True)
LOGGER = logging.getLogger(__name__)
# endregion

# region Conversion logic
def message2binary(message: str):
    if type(message) == str:
        result = ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        result = [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        result = format(message, "08b")
    else:
        raise TypeError("Input type is not supported")
    return result


def encode(img: any, payload: str, output: str):
    if not payload:
        raise ValueError("Payload can not be empty")
    list1 = []
    max_bytes = (img.shape[0] * img.shape[1] * 3) // 8
    LOGGER.debug(f"Maximum bytes that can be encoded {max_bytes}")
    if len(payload) > max_bytes:
        raise ValueError("Payload is too big")
    # Add terminator
    payload += "#####"
    data_binary = message2binary(payload)
    LOGGER.debug(data_binary)
    data_len = len(data_binary)
    print(f"The Length of Binary data {data_len}")
    data_index = 0
    for index in img:
        for pixel in index:
            r, g, b = message2binary(pixel)
            # Red
            if data_index < data_len:
                pixel[0] = int(r[:-1] + data_binary[data_index], 2)
                data_index += 1
                list1.append(pixel[0])
            # Green
            if data_index < data_len:
                pixel[1] = int(g[:-1] + data_binary[data_index], 2)
                data_index += 1
                list1.append(pixel[1])
            # Blue
            if data_index < data_len:
                pixel[2] = int(b[:-1] + data_binary[data_index], 2)
                data_index += 1
                list1.append(pixel[2])
            if data_index >= data_len:
                break
    cv2.imwrite(output, img)
    LOGGER.info(f"Saved as {output}")


def decode(img):

    binary_data = ""
    for i in img:
        for pixel in i:
            red, green, blue = message2binary(pixel)
            binary_data += red[-1]
            binary_data += green[-1]
            binary_data += blue[-1]

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        # Check if terminator was reached.
        if decoded_data[-5:] == "#####":
            break

    logging.info(f"Encoded data : {decoded_data[:-5]}")
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
        encode(cv2.imread(args.input), args.payload, args.output)
    elif args.mode == Modes.DECODE:
        if not args.input.endswith(".png"):
            raise ValueError("Input file has to be png")
        decode(cv2.imread(args.input))
# endregion
