# Hier importeer je de functies.
from staff import get_staff_positions, get_person_profile_input
# Bibliotheek van Python tests.
import pytest


def test_get_staff_positions():
    """Test get_staff_positions() function."""
    # Arrange.
    expected_positions = [
        "junior", "medio", "senior", "team leader", "project leader", "manager"
    ]
    # Act.
    positions = get_staff_positions()
    # Assert.
    assert expected_positions == positions
