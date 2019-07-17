"""
pre-defined convenience potential functions
"""
import numpy as np
from fplanck.utility import value_to_vector

def harmonic_potential(center, k):
    """A harmonic potential

    Arguments:
        center    center of harmonic potential (scalar or vector)
        k         spring constant of harmonic potential (scalar or vector)
    """

    center = np.atleast_1d(center)
    ndim = len(center)
    k = value_to_vector(k, ndim)

    def potential(*args):
        U = np.zeros_like(args[0])

        for i, arg in enumerate(args):
            U += 0.5*k[i]*(arg - center[i])**2

        return U

    return potential

def gaussian_potential(center, width, amplitude):
    """A Gaussian potential

    Arguments:
        center    center of Gaussian (scalar or vector)
        width     width of Gaussian  (scalar or vector)
        amplitude amplitude of Gaussian, (negative for repulsive)
    """

    center = np.atleast_1d(center)
    ndim = len(center)
    width = value_to_vector(width, ndim)
    amplitude = value_to_vector(amplitude, ndim)

    def potential(*args):
        U = np.ones_like(args[0])

        for i, arg in enumerate(args):
            U *= np.exp(-np.square((arg - center[i])/width[i]))

        return -amplitude*U

    return potential

def uniform_potential(func, U0):
    """A uniform potential
    
    Arguments:
        func    a boolean function specifying region of uniform probability (default: everywhere)
        U0      value of the potential
    """

    def potential(*args):
        U = np.zeros_like(args[0])
        idx = func(*args)
        U[idx] = U0

        return U

    return potential