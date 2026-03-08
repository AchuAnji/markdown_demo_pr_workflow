import pytest


@pytest.fixture
def sample_defects():
    """Sample defects appearing across different lots."""
    return [
        {"id": "D001", "lot_id": "LOT001", "quantity": 1},
        {"id": "D001", "lot_id": "LOT002", "quantity": 1},  # recurring defect
        {"id": "D002", "lot_id": "LOT001", "quantity": 1},  # one-off
        {"id": "D004", "lot_id": "LOT004", "quantity": 1},  # one-off
    ]


@pytest.fixture
def empty_defects():
    """Empty defect list."""
    return []


@pytest.fixture
def single_zero_quantity():
    """Defect with zero quantity."""
    return [
        {"id": "D001", "lot_id": "LOT001", "quantity": 0}
    ]