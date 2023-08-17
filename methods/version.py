'''
Version information.
'''

import pkg_resources
import methods

__all__ = ['__version__']

__version__ = pkg_resources.get_distribution("methods").version