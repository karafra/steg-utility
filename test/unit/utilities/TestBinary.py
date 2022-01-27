import unittest
from mockito import mock

import numpy as np

from simple_steganography.utilities.binary import message2binary


class Test_message2binary(unittest.TestCase):

  def test_should_convert_string_to_binary(self):
    """Should convert string to binary"""
    # Given
    # When
    result = message2binary("666")
    print(result)
    # Then
    self.assertEqual(result, "001101100011011000110110")
  
  def test_should_convert_int_to_bytes(self):
    """Should convert int to bytes"""
    # Given
    message = 66
    expected = "01000010"
    # When
    result = message2binary(message)
    # Then
    self.assertEqual(result, expected)

  def test_should_convert_uint8_to_bytes(self):
    """Should convert uInt8 to bytes"""
    # Given
    # When
    result = message2binary(np.uint8(66))
    self.assertEqual(result, "01000010")

  def test_should_convert_bytes_to_string_array(self):
    """Should convert bytes to string array"""
    # Given
    message = bytes("haha", encoding="ascii")
    expected = ['01101000', '01100001', '01101000', '01100001']
    # When
    result = message2binary(message)
    # Then
    self.assertEqual(result, expected)

  def test_should_raise_TypeError_if_not_supported_type(self):
    """Should raise value error when type is not supported"""
    # Given
    arg = mock()
    # When
    with self.assertRaises(TypeError) as ecm:
      message2binary(arg)
    excpetion = ecm.exception
    # Then
    self.assertEqual(str(excpetion), "Input type is not supported")
