import unittest
from mockito import mock, verify, when

from simple_steganography.decorators.notNone import NotNone


class Test_NotNone(unittest.TestCase):

    def test_should_not_allow_None_in_non_keyword_arguments(self):
        """Should not allow None in non keyword arguments"""
        # Given
        @NotNone()
        def test_function(argument: any) -> None:
            ...

        should_throw = lambda: test_function(None)
        # When
        with self.assertRaises(ValueError) as ecm:
            should_throw()
        exception = ecm.exception
        # Then
        self.assertEqual("Non keyword arguments can not be null",
                         str(exception))

    def test_should_skip_param_if_has_no_boolean_value(self):
        """Should skip if argument boolean value is ambiguous"""
        # Given
        arg = mock()
        when(arg).get().thenReturn("value")
        when(arg).__bool__().thenRaise(ValueError("Test error"))

        @NotNone()
        def test_function(argument: any) -> any:
            return argument

        # When
        response = test_function(arg)
        # Then
        self.assertEqual(response.get(), "value")
        verify(response).__bool__()

    def test_should_execute_function(self):
        """Should execute function if all non keyword arguments are not None"""
        # Given
        arg = mock()
        when(arg).get().thenReturn("value")
        when(arg).__bool__().thenReturn(True)

        @NotNone()
        def test_function(arg: any) -> any:
            return arg

        # When
        response = test_function(arg)
        # Then
        verify(arg, times=2).__bool__()
        self.assertEqual(response.get(), "value")

    def test_should_validate_keyword_arguments(self):
        """Should check if any keyword arguments are None (only keyword)"""
        # Given
        arg = mock()
        when(arg).get().thenReturn("value")
        when(arg).__bool__().thenReturn(True)

        @NotNone("arg")
        def test_function(arg=None):
            return arg

        # When
        response = test_function(arg=arg)
        # Then
        verify(arg).__bool__()
        self.assertEqual(response.get(), "value")

    def test_should_validate_keyword_arguments_throws(self):
        """Should check if any keyword arguments are None (only keyword) and raise"""
        # Given
        arg = mock()
        when(arg).__bool__().thenReturn(True)

        @NotNone("arg")
        def test_function(arg=None):
            return arg

        should_throw = lambda: test_function()
        # When
        with self.assertRaises(ValueError) as ecm:
            should_throw()
        exception = ecm.exception
        # Then
        self.assertEqual(str(exception), "Argument `arg` can not be None")

    def should_validate_both_keyword_and_positional_arguments_at_the_same_time(
            self):
        """Should validate both positional and keyword arguments at the same time"""
        # Given
        arg = mock()
        when(arg).__bool__().thenReturn(True)
        when(arg).get().thenReturn("arg")
        kwarg = mock()
        when(kwarg).__bool__().thenReturn(True)
        when(kwarg).get().thenReturn("kwarg")
        
        @NotNone("arg")
        def test_function(arg, kwarg=kwarg):
            return arg, kwarg
        # When
        arg_response, kwarg_response = test_function(arg)
        # Then
        verify(arg).__bool__()
        verify(kwarg).__bool()
        self.assertEqual(arg_response.get(), "arg")
        self.assertEqual(kwarg_response.get(), "kwarg")
