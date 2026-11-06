# 오픈소스SW개발 진행 상황
마지막 업데이트: 2026-11-06 (GitHub Actions 실습 적용, 저장소 이름 git-practice로 변경)

## 수업 요약
> 자세한 내용은 [git-수업노트.md](git-수업노트.md) 를 보세요.

**1차시 – Git 기초와 원격 저장소**
- Git(내 PC의 버전 관리 도구)과 GitHub(저장소를 올려 공유하는 웹 서비스)는 다르다는 걸 배움.
- 파일은 `Working Directory → Staging Area → Local Repository → Remote` 순서로 흘러가고, commit은 "그 시점 전체의 사진(Snapshot)".
- 이후 모든 협업 기능이 이 흐름 위에서 돌아가서 "기초 체력"에 해당함.
- 핵심 명령어: `git init`, `status`, `add`, `commit -m`, `log --oneline`, `diff`, `remote add origin`, `push -u origin main`, `clone`

**2차시 – Branch · Merge · Conflict · pull · 되돌리기**
- branch는 폴더 복사가 아니라 commit을 가리키는 이름표. 갈라진 작업을 merge로 합치고, 같은 줄을 고치면 conflict를 사람이 해결.
- `git pull` = `fetch + merge/rebase`. 이력이 갈라졌을 때 `--no-rebase` / `--rebase` / `--ff-only` 중 정책을 정함.
- 되돌리기는 대상에 따라 `restore`(파일/stage), `reset`(commit, branch 이름표), `revert`(공유된 commit을 취소하는 새 commit).
- 핵심 명령어: `switch -c`, `branch`, `merge`, `merge --abort`, `pull`, `restore`, `reset --soft HEAD~1`, `revert`, `branch -d`

**3차시 – GitHub 협업과 Pull Request**
- 혼자 하던 branch/merge를 GitHub 위로 옮겨 `Issue → Branch → Push → Pull Request → Review → Merge` 팀 협업 절차로 연결.
- 권한(Role), main 보호 규칙(Ruleset), 리뷰어 자동 지정(CODEOWNERS)까지 다룸. 오픈소스·회사에서 일하는 실제 방식.
- PR에 conflict가 나면 내 branch에서 최신 main을 merge해서 해결 후 push.
- 핵심 명령어: `push -u origin 브랜치`, `fetch origin`, `merge origin/main` (나머지는 GitHub 웹 화면 작업)

**소프트웨어공학 10장 – 테스팅 (이론, 명령어 실습 없음)**
- 오류(사람 실수) → 결함(코드 문제) → 장애(눈에 보이는 오동작), 검증(올바르게 만들었나) vs 확인(올바른 걸 만들었나)을 구분.
- 테스트 수준(단위·통합·시스템·인수)과 케이스 설계 기법(동등 분할, 경계값, 결정 테이블, Pairwise, 커버리지, 상태 기반)을 배움.
- 통합 전략(빅뱅/하향식=스텁/상향식=드라이버/연쇄식)과 시스템·인수 테스트(알파/베타)까지.
- 3차시의 Actions 자동 테스트, Ruleset의 status checks가 바로 이 테스트를 merge 조건으로 쓰는 장치.

**GitHub Actions – 워크플로 자동화**
- `.github/workflows/*.yml` 에 "언제(`on`) · 어디서(`runs-on`) · 어떻게(`steps`)"를 적으면 GitHub가 빌드·테스트·배포를 자동 실행.
- 스텝은 셸 명령(`run`)이나 남이 만든 액션(`uses`)이고, YAML은 **탭 금지, 공백 2칸**. 종료 코드 0이면 성공으로 간주.
- context(`${{ github.actor }}`), 환경 변수 `env`(한 워크플로), Variables(여러 워크플로), Secrets(암호화)를 구분.
- 핵심 키워드: `name`, `on: push / workflow_dispatch`, `jobs`, `runs-on: ubuntu-latest`, `steps`, `run: |`, `uses: actions/checkout@v4`, `env`, `vars`, `secrets`

## 실습 체크리스트

### 1차시 (실습 번호는 수업노트 기준)
- [x] 실습 1: `git --version` 으로 Git 설치 확인 (git이 동작함)
- [x] 실습 2: `git config` 로 사용자 정보 설정 (commit 작성자 `jyl` 로 기록됨)
- [x] 실습 3: `git init` 으로 Local Repository 생성 (`.git` 폴더 있음)
- [x] 실습 4: `git status` 로 상태 확인 (확인 필요 – 기록은 안 남지만 이후 단계를 해냈으므로 했을 가능성 높음)
- [x] 실습 5~7: README.md 만들고 add, 첫 commit (`1dc45ec init commit`)
- [x] 실습 8~9: README.md 수정 후 diff 확인, 두 번째 commit (`5e247a5 README.md has been modified`)
- [x] 실습 10: GitHub에 빈 Repository 생성 (remote 주소 `RaccoonPrince/git-practice` 로 이름 변경됨 (원래 오타 git-pratice))
- [x] 실습 11: `git remote add origin` 으로 Remote 등록 (`git remote -v` 에 origin 있음)
- [x] 실습 12: `git push -u origin main` (`origin/main` 이 최신 commit과 같음, status "up to date")
- [ ] 실습 13: clone-test 폴더에 clone해서 확인 (확인 필요 – 이 폴더에서는 알 수 없음)

### 2차시 (2026-10-16 Claude가 대신 실행, 따라 하기: [실습기록-2차시.md](실습기록-2차시.md))
- [x] 단계 1: baseline commit (`c800137`)
- [x] 단계 2: multiply 추가 → diff → add → diff --staged → commit (`377ef58 Add multiply function`)
- [x] 단계 3: Branch 개념 이해 (개념, 본인 확인 필요)
- [x] 단계 4: 자동 merge (`feature/mod` Fast-forward, `feature/pow` merge commit `a9649f1`; sub/div는 이미 main에 있어 mod/pow로 대체)
- [x] 단계 5: Conflict (`feature/add-validation`, `feature/add-message` → 충돌 → `merge --abort` 연습 → 해결 commit `50865e2`)
- [ ] 단계 6: pull 전략 개념 이해 (실행 없음, 본인이 읽고 이해)
- [x] 단계 7: restore / restore --staged / reset --soft / revert (`eb782fe`)
- [x] 단계 8: `git branch -d` 로 feature branch 정리 (main만 남음)
- [ ] 혼자 연습하기 ①② (직접 다시 해 보기)
- [ ] 확인 질문 5개에 내 말로 답해 보기

### 3차시 (대부분 GitHub 웹 화면 + 개념)
- [ ] 개념 이해: GitHub 저장소 탭(Code/Issues/Pull requests/Actions/Settings 등)
- [ ] 개념 이해: Role 5단계(Read/Triage/Write/Maintain/Admin)와 Ruleset
- [ ] 실습 ①: GitHub에서 Issue 생성
- [ ] 실습 ②: `git switch main` → `git pull` → `git switch -c feature/...`
- [ ] 실습 ③: 코드 수정 → `add .` → commit
- [ ] 실습 ④: `git push -u origin feature/...`
- [ ] 실습 ⑤: Pull Request 생성 (base: main ← compare: feature/..., 본문에 `Closes #번호`)
- [ ] 실습 ⑥~⑦: Files changed 리뷰, 추가 commit 후 `git push` 로 PR 업데이트
- [ ] 실습 ⑧: Merge 후 Issue 자동 Close 확인
- [ ] 실습 ⑨: `git switch main` → `git pull` → `git branch -d` 로 정리
- [ ] 개념 이해: CODEOWNERS
- [ ] 실습: PR conflict 해결 (`git fetch origin` → `git merge origin/main` → 해결 → add, commit, push)

### GitHub Actions (2026-11-06 Claude가 대신 적용, 내용은 [git-수업노트.md](git-수업노트.md) 의 "GitHub Actions")
- [x] `.github/workflows/hello.yml` (push 이벤트, echo + checkout)
- [x] `shell-command.yml` (셸 명령, if, for, env — 수동 실행)
- [x] `env-vars.yml` (job env, setup-python, calculator.py 실행 — 수동 실행)
- [x] `variables.yml` + 저장소 변수 `USERNAME` 등록 (수동 실행)
- [ ] GitHub 저장소 Actions 탭에서 실행 결과를 직접 눈으로 확인 (확인 필요)
- [ ] 개념 이해: 이벤트 종류, runner, context, env/Variables/Secrets 차이
- [ ] 스스로 점검 질문 8개에 답해 보기

### 소프트웨어공학 10장 – 테스팅 (개념 이해)
- [ ] 개념 이해: 오류·결함·장애, 검증 vs 확인, 테스팅 vs 디버깅
- [ ] 개념 이해: 테스트 원칙 6가지, 테스트 케이스/오라클, 테스트 수준 4단계
- [ ] 개념 이해: 블랙박스 기법 (동등 분할, 경계값, 원인-결과 그래프, 결정 테이블, Pairwise)
- [ ] 개념 이해: 화이트박스 기법 (문장/분기/경로 커버리지)과 상태 기반 테스팅
- [ ] 개념 이해: 통합 테스트 (드라이버/스텁/목, 빅뱅·하향식·상향식·연쇄식)
- [ ] 개념 이해: 시스템·인수 테스트 (기능/성능/보안/UI, 알파·베타)
- [ ] 스스로 점검 질문 10개에 답해 보기

## 현재 저장소 상태
- 현재 branch: `main` (push 완료, 최신 상태는 아래 `git log` 로 확인)
- 남아 있는 branch: `main` 하나 (+ 원격 `origin/main`)
- remote 주소: `origin` → https://github.com/RaccoonPrince/git-practice.git (GitHub 저장소 이름을 git-pratice → git-practice 로 변경함)
- 로컬 폴더 이름: `git-pratice` → `git-practice` 로 변경 시도 (결과는 아래 "다음에 할 일" 참고)
- 정리 안 된 변경 파일: 없음 (모두 commit/push)

## 다음에 할 일
1. VS Code에서 폴더가 `git-practice` 로 바뀌었는지 확인하고, 바뀌었으면 **File > Open Folder** 로 새 이름의 폴더를 다시 열기.
2. GitHub 저장소 > **Actions** 탭에서 `hello` 실행 결과 확인, 나머지 3개는 **Run workflow** 버튼으로 직접 실행해 보기.
3. 3차시 실습: GitHub 웹에서 Issue 만들기 → `git switch main` → `git pull` → `git switch -c feature/...` → push → Pull Request.
4. [실습기록-2차시.md](실습기록-2차시.md) 를 보며 혼자 연습하기.

## 막혔던 점 / 질문 기록
- (처음엔 비워 둠)
