import unittest

from mockito import mock, when

from simple_steganography.utilities.stegUtils import verify_payload


class Test_verify_payload(unittest.TestCase):
  
  def test_should_not_allow_None_payload(self):
    """Should not allow None as payload"""
    # Given
    img = mock()
    # When
    with self.assertRaises(ValueError) as ecm:
      verify_payload(None, img)
    exception = ecm.exception
    # Then
    self.assertEqual(str(exception), "Non keyword arguments can not be null")

  def test_should_not_allow_None_img(self):
    """Should not allow None as img"""
    # Given
    payload = mock()
    # When
    with self.assertRaises(ValueError) as ecm:
      verify_payload(payload, None)
    exception = ecm.exception
    # Then
    self.assertEqual(str(exception), "Non keyword arguments can not be null")

  def test_should_do_nothing_if_payload_fits_into_image(self):
    """Should do nothing if payloads fits into image"""
    # Given
    img = mock()
    img.shape =  [10, 10]
    payload = "aaa"
    # When
    verify_payload(payload, img)
    # Then ... :/

  def test_should_throw_error_if_payload_is_too_big(self):
    """Should raise error if payload does not fit into image"""
    # Given
    img = mock()
    img.shape = [1, 1]
    payload = "a" * 10
    # When
    with self.assertRaises(ValueError) as ecm:
      verify_payload(payload, img)
    exception =  ecm.exception
    # Then
    self.assertEqual(str(exception), "Payload is too big")
