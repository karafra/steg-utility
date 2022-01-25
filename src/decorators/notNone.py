#!/usr/bin/env python3

"""Decorator for arguments which can not be null.

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
# endregion

# region Constants
LOGGER = logging.getLogger(__name__)
# endregion

# region Logic
def NotNone(*names):
  """
  -------
  NotNone
  -------
  
  Decorator that throws ValueError if any on non keyword arguments are None of keywords with given names are None
  
  ----------
  Parameters
  ----------
  names: List[str]
    names of keyword arguments to validate
  ------
  Raises
  ------
  ValueError:
    if any of non keyword arguments are None or any keyword argument with given name are None 
  """
  def _notNone(function):
    def __notNone(*args, **kwargs):
      for arg in args:
        try:
          not arg
        except ValueError:
          continue
        if not arg:
          LOGGER.error("Non keyword arguments can not be null")
          raise ValueError("Non keyword arguments can not be null")
      if names:
        for name in names:
          if not kwargs.get(name):
            LOGGER.error(f"Argument `{name}` can not be None")
            raise ValueError(f"Argument `{name}` can not be None")
      return function(*args, **kwargs)
    return __notNone
  return _notNone
# endregion
