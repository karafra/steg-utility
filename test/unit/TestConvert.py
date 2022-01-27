
import imp
import unittest
from unittest.mock import MagicMock, Mock, patch
from cv2 import imread



from mockito import mock, when
import numpy as np

from simple_steganography.convert import decode, encode
from simple_steganography.utilities.stegUtils import verify_payload


class Test_encode(unittest.TestCase):
  
  def test_should_not_allow_empty_input_path(self):
    """Should not allow None as input path"""
    # Given
    input_path = None
    payload = mock()
    output_path = mock()
    # When
    with self.assertRaises(ValueError) as ecm:
      encode(input_path, payload, output_path)
    exception = ecm.exception
    # Then
    self.assertEqual(str(exception), "Non keyword arguments can not be null")

  def test_should_not_allow_empty_payload(self):
    """Should not allow None as payload"""
    # Given
    input_path = mock()
    payload = None
    output_path = mock()
    # When
    with self.assertRaises(ValueError) as ecm:
      encode(input_path, payload, output_path)
    exception = ecm.exception
    # Then
    self.assertEqual(str(exception), "Non keyword arguments can not be null")
    
  def test_should_not_allow_empty_output_path(self):
      """Should not allow None as output path"""
      # Given
      input_path = mock()
      payload = mock()
      output_path = None
      # When
      with self.assertRaises(ValueError) as ecm:
        encode(input_path, payload, output_path)
      exception = ecm.exception
      # Then
      self.assertEqual(str(exception), "Non keyword arguments can not be null")
  
  @patch("src.convert.cv2.imwrite")
  @patch("src.convert.verify_payload", autospec=True)
  @patch("src.convert.cv2.imread")
  def test_should_encrypt_message(self, mock_imread: MagicMock, mock_verify_payload: Mock, mock_imwrite: MagicMock):
    """Should encrypt message"""
    # Given
    input_path = "intput_path"
    payload = "adam"
    output_path = "output_path"
    img = np.array([
      [ 
       # R, G, B  |  R, G, B    
        [1, 0, 1], [1, 0, 0], 
      ] * 255
    ])
    mock_imread.return_value = img
    # When
    encode(input_path, payload, output_path)
    # Then
    mock_verify_payload.assert_called_once_with(payload, img)
    mock_imread.assert_called_once_with(input_path)
    mock_imwrite.assert_called_once_with(output_path, img)
  
  @patch("src.convert.cv2.imwrite")
  @patch("src.convert.verify_payload", autospec=True)
  @patch("src.convert.cv2.imread")
  def test_should_decrypt_message(self, mock_imread: MagicMock, mock_verify_payload: Mock, mock_imwrite: MagicMock):
    """Should decrypt message"""
    # Given
    input_path = "intput_path"
    img = np.array([
      [ 
       # R, G, B  |  R, G, B    
        [1, 0, 1], [1, 0, 0], 
      ] * 255
    ])
    mock_imread.return_value = img
    # When
    decode(input_path)
    # Then
    mock_verify_payload.assert_not_called()
    mock_imread.assert_called_once_with(input_path)
    mock_imwrite.assert_not_called()
    
  def test_should_not_allow_empty_input_path_decode(self):
    """Should not allow None as input path"""
    # Given
    input_path = None
    # When
    with self.assertRaises(ValueError) as ecm:
      decode(input_path)
    exception = ecm.exception
    # Then
    self.assertEqual(str(exception), "Non keyword arguments can not be null")
