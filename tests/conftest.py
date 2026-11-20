import pytest


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    return path
