name : jyl
date : 20260911


## OrderLab: Python CI/CD 실습

계산(Level 1) → 할인·배송 규칙(2) → CSV 집계(3) → FastAPI(4) → 정적 보고서 배포(5)

- 배포 URL: https://raccoonprince.github.io/git-practice/

### 실행 방법 (Python 3.14)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python -m pytest -q
python -m pytest --cov=orderlab --cov-report=term-missing
python generate_report.py   # site/index.html 생성
```

### 워크플로
- `ci.yml`: push·PR에서 lint + test(ubuntu/windows)
- `ci-cd.yml`: PR은 quality만, main push는 quality 통과 후 Pages 배포

### 실패 재현과 해결

| 상황 | 결과 | 해결 |
|---|---|---|
| PR #10에서 회귀 테스트 기댓값 변경 | `assert 85000 == 99000`, [quality 실패](https://github.com/RaccoonPrince/git-practice/actions/runs/45767153712) | revert 후 통과 |
| main에서 샘플 데이터 변경 | [quality 실패, deploy 건너뜀](https://github.com/RaccoonPrince/git-practice/actions/runs/45767411684), 사이트 유지 | revert 후 재배포 |

### 참고
- `calculator.py`는 Git 실습용 파일이라 `pyproject.toml`에서 Ruff 검사 대상에서 제외
- `if: github.event_name == 'push'`: GitHub 표현식의 문자열은 작은따옴표를 사용
