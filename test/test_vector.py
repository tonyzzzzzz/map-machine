"""
Test vector operations.
"""
import numpy as np

from roentgen.vector import compute_angle, turn_by_angle

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"

ROOT: float = np.sqrt(2)


def test_compute_angle() -> None:
    """Test angle computing for all angles between 0 and 2π with step π / 4."""
    assert np.allclose(compute_angle((1, 0)), 0)
    assert np.allclose(compute_angle((ROOT, ROOT)), np.pi * 0.25)
    assert np.allclose(compute_angle((0, 1)), np.pi * 0.5)
    assert np.allclose(compute_angle((-ROOT, ROOT)), np.pi * 0.75)
    assert np.allclose(compute_angle((-1, 0)), np.pi)
    assert np.allclose(compute_angle((-ROOT, -ROOT)), np.pi * 1.25)
    assert np.allclose(compute_angle((0, -1)), np.pi * 1.5)
    assert np.allclose(compute_angle((ROOT, -ROOT)), np.pi * 1.75)


def test_turn_by_compute_angle() -> None:
    """Test turing one angle by another."""
    assert np.allclose(turn_by_angle((1, 0), np.pi / 2), np.array((0, 1)))
