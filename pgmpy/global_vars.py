# TODO: This variables being set in this file should move to setup.py


# This module initializes flags for optional dependencies
try:
    import pandas

    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

device = 'cpu'

dtype = float
