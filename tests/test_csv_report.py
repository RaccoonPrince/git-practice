import pytest

from orderlab.csv_report import revenue_from_csv


def test_csv_revenue(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "price,quantity\n10000,2\n5000,3\n",
        encoding="utf-8",
    )
    assert revenue_from_csv(csv_file) == 35_000


def test_csv_empty(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("price,quantity\n", encoding="utf-8")
    assert revenue_from_csv(csv_file) == 0


def test_csv_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        revenue_from_csv(tmp_path / "nope.csv")


def test_csv_bad_number(tmp_path):
    csv_file = tmp_path / "bad.csv"
    csv_file.write_text("price,quantity\nabc,2\n", encoding="utf-8")
    with pytest.raises(ValueError):
        revenue_from_csv(csv_file)


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000


def test_sample_orders_regression():
    # 배포 보고서에 들어가는 샘플 데이터의 합계가 바뀌면 알 수 있게 한다
    assert revenue_from_csv("data/sample_orders.csv") == 99_000
