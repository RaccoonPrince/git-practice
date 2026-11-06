# 오픈소스SW개발 수업노트: Git 1~3차시 + 소프트웨어공학 10장(테스팅)

> 원본 자료: `git_lesson_1.pdf` (1차시, 33쪽), `git_lesson_2_fix.pdf` (2차시, 68쪽), `git_lesson_3.pdf` (3차시, 50쪽), `소프트웨어공학_10.pdf` (10장 테스팅, 47쪽)
> GitHub를 처음 쓰는 사람 기준으로, 슬라이드 순서대로 정리했습니다. 슬라이드에 없는 설명은 **💡 보충** 으로 표시했습니다.

---

## 0. 먼저 알아두면 좋은 기본 용어

| 용어 | 쉬운 뜻 |
|---|---|
| **터미널(Terminal)** | 마우스 대신 글자로 명령을 입력하는 창. Windows는 *Git Bash* 나 *VS Code 터미널*, Mac은 *터미널* 앱을 씁니다. |
| **디렉터리(Directory)** | 폴더와 같은 말입니다. |
| **Git** | 내 컴퓨터에서 파일의 변경 이력을 기록하는 **프로그램** |
| **GitHub** | Git으로 만든 저장소를 인터넷에 올려 **공유·협업하는 웹사이트** |
| **Repository(저장소, repo)** | Git이 이력을 관리하는 프로젝트 하나 |
| **Commit(커밋)** | "이 시점의 상태를 저장"하는 행위, 또는 그 저장 기록 하나. 게임의 세이브 포인트와 비슷합니다. |
| **Branch(브랜치)** | 작업 흐름을 여러 갈래로 나누는 것 |
| **Merge(머지)** | 갈라진 작업 흐름을 다시 합치는 것 |

💡 **보충: 터미널 기초 명령어** (Git 명령이 아니라 운영체제 명령입니다)
- `cd 폴더명` : 그 폴더로 들어가기. `cd ..` 는 한 단계 위(부모 폴더)로 나가기
- `mkdir 폴더명` : 새 폴더 만들기
- `ls -la` : 현재 폴더의 파일 목록 보기 (`-a` 는 숨김 파일까지, `-l` 은 자세히)
- `echo "글자" > 파일명` : 그 글자를 내용으로 하는 파일을 만들기 (이미 있으면 덮어씀)

---

# 1차시: Git 기초와 원격 저장소

> **한 줄 요약:** GitHub를 쓰기 전에 "Git이 무엇을, 어떻게 기록하는 도구인지"를 이해하고, 내 컴퓨터에서 첫 commit을 만든 뒤 GitHub에 올리는(push) 기본 흐름을 익히는 챕터입니다.
>
> **의의:** 앞으로 배울 branch, merge, Pull Request 같은 협업 기능은 모두 이번 시간의 `수정 → add → commit → push` 흐름 위에서 돌아갑니다. 즉 Git 사용의 "기초 체력"을 만드는 시간입니다.

## Part I. 이론

### 1. 왜 버전 관리가 필요한가? (3~5쪽)

소프트웨어는 개발 중에도, 배포 후에도 계속 바뀝니다 (고객 요구 변경, 일정 변경, OS·라이브러리 변경, 버그 수정 등). 그래서 늘 다음 질문에 답할 수 있어야 합니다.

- **무엇이** 바뀌었나? **누가** 바꿨나? **언제** 바꿨나? **이전 상태로 돌아갈 수 있나?**

버전 관리를 안 하면 이렇게 됩니다.

```
project/
├── main.py
├── main_final.py
├── main_final2.py
├── main_final_REAL.py
└── main_final_REAL_LAST.py
```

파일 이름만으로는 "왜 바꿨는지, 무엇이 달라졌는지"를 알 수 없습니다.

협업에서는 더 심각합니다. 학생 A와 B가 공유 폴더의 `main.py` 를 동시에 고치면, 나중에 저장한 사람이 앞 사람 작업을 **덮어써** 버립니다. 즉 **공유 폴더 ≠ 버전 관리** 입니다.

### 2. VCS(버전 관리 시스템)가 하는 일 (6쪽)

| 기능 | 설명 |
|---|---|
| 이력 저장 | 변경 내용을 시간 순서로 저장 |
| 비교 | 특정 시점과 현재 상태를 비교 |
| 복구 | 필요하면 이전 상태로 되돌림 |
| 병합 | 여러 개발자의 변경을 합침 |
| 충돌 확인 | 같은 부분을 서로 다르게 바꾸면 알려줌 |
| 협업 | 팀 단위 개발 흐름을 만듦 |

대표적인 VCS로 Git, Subversion(SVN) 등이 있습니다.

### 3. Git이란? (7쪽)

Git은 **분산(Distributed) 버전 관리 시스템** 입니다.
- 개발자 **각자의 PC에 전체 이력**이 있습니다.
- 그래서 **인터넷이 없어도 commit** 할 수 있습니다.
- 필요할 때만 다른 저장소와 동기화합니다.

### 4. ⭐ Git ≠ GitHub (8쪽) — 이번 시간 핵심 메시지

| Git | GitHub |
|---|---|
| 버전 관리 **도구(프로그램)** | Git 저장소를 올려두는 **호스팅 서비스(웹사이트)** |
| 내 PC에서도 동작 | 웹 화면(UI) 제공 |
| commit, branch, merge 수행 | Pull Request, Issue 제공 |
| 명령어로 사용 | Actions 등 자동화 제공 |

💡 비유하면 Git은 "한글/워드 프로그램", GitHub는 "구글 드라이브" 같은 관계입니다. 문서는 프로그램으로 만들고, 드라이브는 그걸 올려서 공유하는 곳이죠.

### 5. Repository는 어디에 있을 수 있나? (9쪽)

- **Local Repository**: 내 컴퓨터에 있는 저장소
- **Remote Repository**: 다른 곳(학교·회사 서버, GitHub, GitLab 등)에 있는 저장소

주의: **Remote Repository = GitHub 가 아닙니다.** GitHub는 원격 저장소를 둘 수 있는 여러 장소 중 하나일 뿐입니다.

### 6. Git Repository의 정체: `.git` 폴더 (10쪽)

프로젝트 폴더에서 `git init` 을 실행하면 숨김 폴더 `.git` 이 생깁니다. **이 `.git` 폴더가 바로 Repository** 입니다.

```
project/
├── .git/        ← Git Repository (이력이 저장되는 곳)
├── README.md    ← Working Directory의 파일 (내가 편집하는 파일)
├── main.py
└── src/
```

`.git` 안에 있는 것들:
- `objects/` : 파일 내용과 commit 같은 객체
- `refs/` : branch/tag가 어떤 commit을 가리키는지
- `HEAD` : 지금 내가 있는 branch(또는 commit)
- `config` : 이 저장소의 설정
- `index` : Staging Area 정보

➡ 내가 보고 편집하는 파일(Working Directory)과, Git이 기록한 이력(Repository)은 **서로 다른 것** 입니다. `.git` 을 지우면 파일은 남아도 이력은 전부 사라집니다.

### 7. Git은 commit을 어떻게 저장할까? — Snapshot 모델 (11~14쪽)

두 가지 흔한 오해:
- ❌ 오해 1: commit할 때마다 프로젝트 폴더 전체를 통째로 복사한다.
- ❌ 오해 2: 처음 파일 하나 + 이후 변경점(diff)만 계속 저장한다.

✅ 정답: Git은 각 commit을 **그 시점 프로젝트 전체의 사진(Snapshot)** 으로 취급합니다. 다만 **바뀌지 않은 파일은 이전 것을 재사용** 합니다.

| | main.py | util.py | README |
|---|---|---|---|
| Commit A (최초) | Blob A | Blob B | Blob R |
| Commit B (util.py만 변경) | Blob A 재사용 | **Blob B2 (새로 생성)** | Blob R 재사용 |
| Commit C (main.py만 변경) | **Blob C (새로 생성)** | Blob B2 재사용 | Blob R 재사용 |

Git 내부 객체 3가지 (13쪽):
- **Commit 객체**: 작성자, 메시지, 부모(Parent) commit, Tree를 가리킴
- **Tree 객체**: 폴더 구조와 파일 이름, 각 파일의 Blob을 가리킴
- **Blob 객체**: 실제 파일 내용

각 commit은 이전 commit(부모)을 가리키므로 이력이 **그래프(A → B → C)** 로 연결됩니다. 나중에 branch/merge를 하면 이 그래프가 갈라졌다 합쳐집니다.

그럼 diff를 전혀 안 쓰나? (14쪽) — **논리적으로는 Snapshot**, **물리적으로는** 저장 공간을 아끼기 위해 내부(packfile)에서 압축하거나 delta(차이) 형태로 최적화하기도 합니다. "Git은 변경분만 저장한다"는 설명은 불완전합니다.

### 8. ⭐ Git의 3단계 구조 (15쪽) — 가장 중요한 그림

```
Working Directory   ← 지금 내가 보고 수정하는 파일
      │ git add
      ▼
Staging Area (Index) ← 이번 commit에 넣을 변경 목록 (장바구니)
      │ git commit
      ▼
Local Repository    ← commit 이력이 저장되는 곳
```

💡 비유: 온라인 쇼핑에서 **물건 고르기(수정) → 장바구니 담기(add) → 결제(commit)**. 장바구니 덕분에 여러 파일을 고쳤어도 "이번 commit에 넣을 것만" 골라 담을 수 있습니다. 이것이 Staging Area가 필요한 이유입니다.

### 9. 1차시에서 쓰는 명령어 (16쪽)

| 분류 | 명령어 |
|---|---|
| 저장소 | `git init`, `git clone`, `git remote -v` |
| 변경 기록 | `git status`, `git add`, `git commit` |
| 확인·동기화 | `git log`, `git diff`, `git push` |

(branch, merge, conflict, Pull Request는 다음 차시에서)

---

## Part II. 실습 — 순서대로 따라하기

### 실습 전체 상황 한눈에 보기

`git-practice` 라는 폴더를 만들어 Git 저장소로 만들고 → `README.md` 로 첫 commit → 내용 수정 후 두 번째 commit → GitHub에 빈 저장소를 만들어 연결 → push로 업로드 → 다른 폴더에 clone해서 제대로 올라갔는지 확인하는 흐름입니다.

**준비물 (17쪽):** Git 설치, 터미널(또는 Git Bash), GitHub 계정, 실습용 폴더

---

### 실습 1. Git 설치 확인 (18쪽)

```bash
git --version
```
- **하는 일:** 컴퓨터에 Git이 설치되어 있는지, 버전이 몇인지 확인합니다.
- **정상 결과:** `git version 2.xx.x`
- `command not found` 가 나오면 Git이 설치되지 않은 것입니다.

### 실습 2. 사용자 정보 설정 (19쪽)

```bash
git config --global user.name "Student Name"
git config --global user.email "student@example.com"
git config --list
```
- `git config` : Git 설정을 바꾸는 명령
- `--global` : 이 컴퓨터의 **모든 저장소에 공통으로** 적용 (한 번만 하면 됨)
- `user.name` / `user.email` : commit할 때 **작성자로 기록될 이름과 이메일**. 따옴표 안에 본인 정보를 넣으세요.
- `git config --list` : 설정된 값 전체를 보여줘서 제대로 들어갔는지 확인
- 💡 이메일은 GitHub 가입 이메일과 같게 하면 GitHub에서 commit이 내 계정과 연결되어 보입니다.

### 실습 3. Local Repository 만들기 (20쪽)

```bash
mkdir git-practice   # git-practice 폴더 생성
cd git-practice      # 그 폴더 안으로 이동
git init             # 이 폴더를 Git 저장소로 만듦
ls -la               # 숨김 폴더까지 목록 보기
```
- `git init` : 현재 폴더 안에 `.git` 폴더를 만들어 **Git 저장소로 초기화**합니다. init한 폴더가 저장소의 **루트(최상위) 폴더**가 됩니다.
- `ls -la` 결과에 `.git` 이 보이면 성공입니다.
- ⚠ 주의: 이미 저장소인 폴더 안에서 또 `git init` 하지 마세요. 항상 `cd` 로 원하는 폴더에 먼저 들어간 뒤 실행합니다.

### 실습 4. 현재 상태 확인 (21쪽)

```bash
git status
```
- **하는 일:** 지금 어느 branch에 있는지, 어떤 파일이 바뀌었는지, commit할 게 있는지를 알려줍니다. **가장 자주 쓰는 명령**이니 헷갈리면 무조건 이것부터!
- 처음 결과:
  ```
  On branch main
  No commits yet
  nothing to commit
  ```
- 환경에 따라 `main` 대신 `master` 로 나올 수 있는데, 수업에서는 `main` 을 씁니다 (실습 12에서 이름을 바꿉니다).

### 실습 5. 첫 파일 만들기 (22쪽)

```bash
echo "# Git Practice" > README.md
git status
```
- `echo ... > README.md` : `# Git Practice` 라는 내용의 README.md 파일을 만듭니다.
- 이제 `git status` 에 다음이 나옵니다.
  ```
  Untracked files:
    README.md
  ```
- **Untracked** = "파일은 있는데 Git이 아직 관리(추적)하지 않는 상태". 3단계 구조에서 아직 **Working Directory** 에만 있는 것입니다.

### 실습 6. Staging Area에 올리기 (23쪽)

```bash
git add README.md
git status
```
- `git add 파일명` : 그 파일을 **Staging Area(장바구니)에 올립니다.**
- 결과:
  ```
  Changes to be committed:
    new file: README.md
  ```
  → "다음 commit에 들어갈 준비 완료"라는 뜻입니다.
- 💡 `git add .` 은 현재 폴더의 변경된 파일을 전부 올리는 명령입니다.

### 실습 7. 첫 Commit (24쪽)

```bash
git commit -m "Initial commit"
git log --oneline
```
- `git commit` : Staging Area에 올린 내용을 **하나의 기록(snapshot)으로 저장소에 저장**합니다.
- `-m "메시지"` : commit 메시지. "무엇을 했는지"를 적습니다. (`-m` 을 빼면 편집기가 열려서 당황할 수 있으니 꼭 붙이세요.)
- `git log --oneline` : commit 이력을 **한 줄씩 짧게** 보여줍니다.
  ```
  a1b2c3d Initial commit
  ```
  앞의 `a1b2c3d` 는 commit의 고유 ID(해시)입니다. 사람마다 다르게 나옵니다.

### 실습 8. 파일 수정 후 diff 확인 (25쪽)

README.md를 편집기(VS Code, 메모장 등)로 열어 이렇게 바꿉니다.
```
# Git Practice
Name: Student Name
Student ID: 20260000
```
```bash
git status
git diff
```
- `git status` : README.md가 `modified`(수정됨)로 나옵니다.
- `git diff` : **마지막 commit 이후 어떤 줄이 바뀌었는지** 보여줍니다. `+` 로 시작하는 줄이 추가된 줄, `-` 는 삭제된 줄입니다.
- 💡 diff 화면이 길어서 안 끝나면 `q` 를 눌러 빠져나옵니다.

### 실습 9. 두 번째 Commit (26쪽)

```bash
git add README.md
git commit -m "Add student information"
git log --oneline
```
- 방금 수정한 내용을 다시 장바구니에 담고(add) 저장(commit)합니다.
- 결과 (최신이 위):
  ```
  72bc213 Add student information
  113f61c Initial commit
  ```
- 💡 파일을 한 번 add 했어도, **수정할 때마다 다시 add** 해야 합니다.

### 실습 10. GitHub에 Repository 만들기 (27쪽) — 웹에서 진행

1. GitHub 로그인
2. 오른쪽 위 `+` 또는 **New repository** 선택
3. Repository name: `git-practice`
4. README, .gitignore, license **체크하지 않기**
5. **Create repository** 클릭

- 왜 README를 만들지 않나? 이미 내 컴퓨터(로컬)에 README와 commit이 있기 때문입니다. GitHub 쪽에도 README를 만들면 양쪽 이력이 달라져서 push할 때 충돌이 납니다. 그래서 **빈 저장소** 로 만듭니다.

### 실습 11. Remote 등록 (28쪽)

```bash
git remote add origin https://github.com/사용자명/git-practice.git
git remote -v
```
- `git remote add origin 주소` : 내 로컬 저장소에 "원격 저장소 주소"를 등록하는데, 그 주소에 **`origin` 이라는 별명** 을 붙입니다. `사용자명` 자리에 본인 GitHub 아이디를 넣으세요. (주소는 GitHub에서 저장소를 만든 직후 화면에 나옵니다.)
- `git remote -v` : 등록된 원격 저장소 목록과 주소를 보여줍니다 (fetch/push 두 줄이 나오면 정상).
- ⭐ **`origin` 은 GitHub가 아닙니다.** 원격 저장소 주소에 붙인 **별명**일 뿐입니다. 관례상 origin이라고 부릅니다.

### 실습 12. GitHub로 Push (29쪽)

```bash
git branch -M main
git push -u origin main
```
- `git branch -M main` : 현재 branch 이름을 `main` 으로 바꿉니다 (`master` 로 되어 있던 경우 통일용).
- `git push origin main` : 내 로컬 `main` branch의 commit들을 `origin`(GitHub 저장소)으로 **전송**합니다.
- `-u` : "앞으로 이 branch는 origin/main과 짝"이라고 기본 대상을 설정합니다. 한 번 해두면 다음부터는 그냥 `git push`, `git pull` 만 쳐도 됩니다.
- 💡 처음 push할 때 GitHub 로그인 창이 뜨거나 비밀번호를 묻습니다. GitHub는 **계정 비밀번호로 push할 수 없고**, 브라우저 로그인 또는 Personal Access Token(토큰)을 써야 합니다. 막히면 수업 안내대로 쉬는 시간에 해결하세요.
- push 후 GitHub 페이지를 새로고침하면 README.md와 commit 2개가 보입니다.

### 실습 13. Clone으로 확인 (30쪽)

```bash
cd ..                    # git-practice 밖으로 나감
mkdir clone-test         # 확인용 새 폴더
cd clone-test
git clone https://github.com/사용자명/git-practice.git
cd git-practice
git log --oneline
```
- `git clone 주소` : 원격 저장소를 **통째로 복제**해 옵니다. 파일만 받는 단순 다운로드가 아니라 **commit 이력까지 포함한 저장소 전체**를 가져옵니다. (origin 등록도 자동으로 됩니다.)
- 마지막 `git log --oneline` 에서 커밋 2개가 그대로 보이면 push가 제대로 된 것입니다.
- 💡 실습이 끝나면 다시 원래 `git-practice` 폴더로 돌아가세요. 2차시는 **원래 폴더** 에서 이어집니다.

---

### 1차시 전체 흐름 정리 (31쪽)

```
Working Directory
    │ git add
Staging Area
    │ git commit
Local Repository
    │ git push
Remote Repository (GitHub 또는 사설 Git 서버)
```

### 확인 질문 (32쪽) + 모범 답안

| 질문 | 답 |
|---|---|
| Git과 GitHub의 차이는? | Git은 버전 관리 프로그램, GitHub는 Git 저장소를 호스팅하고 협업 기능을 제공하는 서비스 |
| Local과 Remote repository의 차이는? | Local은 내 컴퓨터의 저장소, Remote는 다른 곳(서버, GitHub 등)에 있는 저장소 |
| origin은 무엇인가? | 원격 저장소 주소에 붙인 별명 (GitHub 자체가 아님) |
| Staging area는 왜 필요한가? | 변경 중 이번 commit에 넣을 것만 골라 담기 위해 |

---

# 2차시: Git Branch와 실제 변경 이력 관리

> **한 줄 요약:** 하나의 파일(`calculator.py`)을 직접 고쳐 가며 `diff → commit → branch 분기 → 자동 merge → conflict(충돌) 해결 → pull 전략 → 되돌리기` 를 모두 손으로 해보는 챕터입니다.
>
> **의의:** 1차시가 "혼자 기록하는 법"이었다면, 2차시는 **작업을 갈래로 나누고 다시 합치는 법**을 배웁니다. 여러 사람이 동시에 개발할 수 있게 해주는 핵심 기능이고, 다음 차시의 GitHub Pull Request 협업으로 바로 이어집니다. Git이 "기록 도구"에서 "협업 도구"가 되는 순간입니다.

### 이번 시간의 원칙 (4쪽)

명령을 외우는 것보다 **"지금 어느 branch에 있나? 어떤 파일이 바뀌었나? 어떤 commit을 가리키나?"** 를 계속 확인하는 게 중요합니다. 그래서 거의 매 단계마다 이 세 명령을 씁니다.

```bash
git status                                   # 현재 branch와 파일 상태
git branch                                   # branch 목록 (* 표시가 현재 branch)
git log --graph --oneline --decorate --all   # 전체 commit 그래프
```
- `--graph` : commit 이력을 선(그래프)으로 그려줌
- `--oneline` : commit 하나를 한 줄로
- `--decorate` : 각 commit 옆에 어떤 branch/HEAD가 가리키는지 이름표 표시
- `--all` : 현재 branch뿐 아니라 **모든 branch** 의 commit을 표시

💡 이 긴 명령이 귀찮으면 `git config --global alias.graph "log --graph --oneline --decorate --all"` 로 등록한 뒤 `git graph` 로 쓸 수 있습니다. (선택 사항)

### 2차시 실습 전체 흐름

1. 준비: 1차시 저장소에서 `calculator.py` 기준 상태 commit
2. diff 연습: `multiply` 추가 → diff → stage → commit
3. **자동 merge**: `feature/sub`, `feature/div` 두 branch를 만들어 각각 함수 추가 → main에 둘 다 merge
4. **Conflict**: `feature/add-validation`, `feature/add-message` 가 add() 같은 줄을 다르게 수정 → merge 시 충돌 → 직접 해결
5. **pull 전략**: `--no-rebase` / `--rebase` / `--ff-only` 개념
6. **되돌리기**: `restore` / `reset` / `revert`
7. branch 정리

---

## 단계 1. 준비 (5~7쪽)

### 1-1. 1차시 저장소로 이동 (5쪽)

```bash
cd git-practice
git status
git log --oneline
```
- **새 저장소를 만들지 않고** 1차시의 `git-practice` 를 그대로 씁니다.
- `git log --oneline` 에 1차시 commit 2개가 보이면 맞는 폴더입니다.

### 1-2. calculator.py 만들기 (6쪽)

편집기로 `calculator.py` 를 만들고 다음 내용을 넣습니다.
```python
def add(a, b):
    return a + b

print(add(10, 5))
```
- `add` 함수 하나만 있는 상태가 모든 실습의 **출발점(baseline)** 입니다.

### 1-3. 출발점을 commit으로 고정 (7쪽)

```bash
git add calculator.py
git commit -m "Prepare calculator baseline"
git status
```
- 출발 상태를 commit해 둬야 이후 변경이 깔끔하게 비교됩니다.
- `git status` 결과가 `nothing to commit, working tree clean` 이면 준비 완료.

---

## 단계 2. diff → stage → commit 연습 (8~11쪽)

### 2-1. 코드 수정 (8쪽)

`add` 아래에 추가 (아직 add/commit 하지 않음):
```python
def multiply(a, b):
    return a * b
```

### 2-2. 변경사항 확인 (9쪽)

```bash
git diff
```
- commit하기 전에 **무엇을 바꿨는지 검토** 합니다.
- 읽는 법: `+` 추가된 줄, `-` 삭제된 줄, `@@ -1,4 +1,7 @@` 같은 줄은 **변경 위치**(몇 번째 줄 근처인지).

### 2-3. Stage 하고 한 번 더 확인 (10쪽)

```bash
git add calculator.py
git diff --staged
git status
```
- `git add` 후에는 그냥 `git diff` 를 치면 **아무것도 안 나옵니다!** `git diff` 는 "Working Directory vs Staging Area" 비교이기 때문입니다.
- `git diff --staged` : "Staging Area vs 마지막 commit" 을 비교 → **실제로 commit될 내용** 을 보여줍니다.

| 명령 | 무엇과 무엇을 비교? |
|---|---|
| `git diff` | 작업 중 파일 ↔ Staging Area (아직 add 안 한 변경) |
| `git diff --staged` | Staging Area ↔ 마지막 commit (add 해서 commit 예정인 변경) |

### 2-4. Commit (11쪽)

```bash
git commit -m "Add multiply function"
git log --oneline
```
- commit 메시지는 **"무엇을 했는가"** 가 드러나게 씁니다 (예: "Add multiply function", "Fix division by zero").

💡 이 **수정 → diff → add → diff --staged → commit** 순서가 이후 모든 실습에서 반복되는 기본 루틴입니다.

---

## 단계 3. Branch 개념 (12쪽)

- **branch는 폴더 복사가 아닙니다.** 특정 commit을 가리키는 **이름표(pointer)** 입니다.
- **HEAD** 는 "지금 내가 작업 중인 branch" 를 가리키는 특별한 이름표입니다.
- 새 commit을 만들면 현재 branch의 이름표가 새 commit으로 한 칸 이동합니다.

```
C0 ── C1 ── C2 ── C3
                  ↑
               main ← HEAD
```

💡 비유: 책에 꽂은 **책갈피**. 책갈피를 여러 개 꽂아도 책이 복사되지 않는 것처럼, branch를 만들어도 파일이 복사되지 않습니다.

---

## 단계 4. 자동 merge 실습 (13~26쪽)

**상황:** 두 사람이 각자 다른 기능(sub, div)을 개발한다고 가정합니다. 둘 다 **같은 main commit에서 출발** 해 각자 branch에서 작업한 뒤, main에 합칩니다.

### 4-1. main에서 출발 (13쪽)

```bash
git switch main
git status
git log --graph --oneline --decorate --all
```
- `git switch main` : **main branch로 이동**합니다.
- 💡 옛날 자료에서 보이는 `git checkout main` 도 같은 뜻입니다. `switch` 는 branch 이동 전용으로 새로 나온 더 명확한 명령입니다.

### 4-2. feature/sub branch 만들기 (14쪽)

```bash
git switch -c feature/sub
git branch
```
- `git switch -c 이름` : **새 branch를 만들고(create) 바로 그 branch로 이동**합니다.
- `git branch` : branch 목록을 보여주고, 현재 branch 앞에 `*` 가 붙습니다.
  ```
  * feature/sub
    main
  ```
- 막 만든 직후에는 main과 feature/sub가 **같은 commit** 을 가리킵니다. 새 commit을 만드는 순간부터 갈라집니다.
- 💡 `feature/` 는 "기능 개발용 branch"라는 걸 나타내는 흔한 이름 짓기 관례입니다.

### 4-3. sub 함수 추가 → commit (15~16쪽)

`add` 함수 **바로 아래**에 추가:
```python
def sub(a, b):
    return a - b
```
```bash
git diff                       # 추가한 내용 확인
git add calculator.py          # stage
git diff --staged              # commit될 내용 확인
git commit -m "Add sub function"
```

### 4-4. 상태 확인 (17쪽)

```bash
git status
git log --graph --oneline --decorate --all
```
- 그래프에서 `HEAD -> feature/sub` 가 최신 commit(sub 추가)을 가리키고, `main` 은 한 칸 뒤에 있는지 확인합니다.

### 4-5. 반드시 main으로 돌아가기 (18쪽)

```bash
git switch main
git status
```
- ⚠ **중요:** feature/sub에 있는 상태에서 feature/div를 만들면 div branch에 **sub commit까지 딸려 들어갑니다.** 두 작업을 독립적으로 만들려면 공통 출발점인 main으로 돌아가야 합니다.
- 💡 main으로 돌아오면 편집기의 calculator.py에서 **sub 함수가 사라진 것처럼 보입니다.** 정상입니다! sub는 feature/sub branch에만 있기 때문입니다. `git switch` 는 파일 내용을 그 branch의 상태로 바꿔 줍니다.

### 4-6. feature/div 만들기 (19쪽)

```bash
git switch -c feature/div
git branch
```

### 4-7. div 함수 추가 → commit (20~21쪽)

sub가 들어간 위치(add 바로 아래)와 **충분히 떨어진 파일 아래쪽** 에 추가합니다.
```python
def div(a, b):
    return a / b
```
```bash
git diff
git add calculator.py
git diff --staged
git commit -m "Add div function"
```
- 떨어진 곳에 쓰는 이유: 나중에 Git이 두 변경을 **자동으로 합칠 수 있게** 하기 위해서입니다 (단계 4-11 참고).

### 4-8. 갈라진 그래프 확인 (22쪽)

```bash
git log --graph --oneline --decorate --all
```
```
            S1: sub  ← feature/sub
           /
C1 ── C2 ── C3  ← main
           \
            D1: div  ← feature/div
```
- 같은 main commit(C3)에서 출발했지만 서로 다른 commit을 만들어 **이력이 두 갈래로 갈라진** 상태입니다.

### 4-9. 첫 번째 merge (23쪽)

```bash
git switch main
git merge feature/sub
git status
```
- `git merge 브랜치명` : **지금 있는 branch(main)에** 지정한 branch의 변경을 **합칩니다.** 그래서 먼저 "받는 쪽"인 main으로 이동해야 합니다.
- 💡 이때 main은 feature/sub보다 뒤처져 있기만 하므로 Git은 새 commit 없이 main 이름표만 앞으로 옮깁니다(**Fast-forward**, 단계 6에서 설명). 출력에 `Fast-forward` 라고 나옵니다.

### 4-10. 두 번째 merge (24쪽)

```bash
git merge feature/div
```
- 이번엔 main과 feature/div가 **서로 다른 commit을 가진 상태**라 진짜 합치기가 일어납니다.
- 💡 이때 **편집기(vim 등)가 열리며 merge commit 메시지를 물어볼 수 있습니다.** 기본 메시지 그대로 저장하고 닫으면 됩니다. vim이라면 `:wq` 입력 후 Enter.

### 4-11. 결과 확인 (25~26쪽)

```bash
python calculator.py
git log --graph --oneline --decorate --all
```
- `python calculator.py` : 합쳐진 코드가 실제로 잘 실행되는지 확인 (`15` 출력). Mac/Linux에서 안 되면 `python3` 로.
- calculator.py 안에 add, sub, multiply, div가 모두 들어있어야 합니다.
- 그래프에 두 갈래가 다시 합쳐진 **merge commit(M)** 이 보입니다.

```
     S1 ────┐
    /        \
C3           M  ← main, HEAD
    \        /
     D1 ────┘
```

**핵심 (26쪽): 같은 파일 ≠ 무조건 충돌.** Git은 Python 코드의 의미를 이해하는 게 아니라 **텍스트 줄의 위치**를 비교합니다. 같은 파일이어도 바뀐 위치가 충분히 떨어져 있으면 자동으로 합쳐집니다.

---

## 단계 5. Conflict(충돌) 실습 (27~46쪽)

**상황:** 이번엔 **일부러** 두 branch가 add() 함수의 **같은 줄** 을 서로 다르게 고치게 만듭니다. Git이 "둘 중 뭐가 맞지?"를 결정할 수 없는 상황을 체험하는 실습입니다.

### 5-1. 첫 번째 충돌용 branch (28~30쪽)

```bash
git switch main
git switch -c feature/add-validation
```
add 함수를 이렇게 수정:
```python
def add(a, b):
    print("add called")
    return a + b
```
```bash
git diff
git add calculator.py
git commit -m "Add logging to add"
```

### 5-2. 두 번째 충돌용 branch (31~33쪽)

```bash
git switch main                    # 반드시 main에서 다시 분기!
git switch -c feature/add-message
```
**같은 위치**에 다른 문자열:
```python
def add(a, b):
    print("calculating...")
    return a + b
```
```bash
git diff
git add calculator.py
git commit -m "Add message to add"
git log --graph --oneline --decorate --all
```
- 두 branch가 같은 줄을 서로 다르게 바꾼 상태가 그래프에 보입니다.

### 5-3. 첫 번째 merge — 정상 (34쪽)

```bash
git switch main
git merge feature/add-validation
```
- main에는 아직 상대 변경이 없으므로 문제없이 합쳐집니다.

### 5-4. 두 번째 merge — 충돌 발생! (35~36쪽)

```bash
git merge feature/add-message
```
출력:
```
Auto-merging calculator.py
CONFLICT (content): Merge conflict in calculator.py
Automatic merge failed; fix conflicts and then commit the result.
```
- **당황하지 마세요!** 저장소가 망가진 게 아닙니다. Git이 "자동으로 결정 못 하겠으니 사람이 골라줘" 하고 **멈춘 상태** 입니다.

### 5-5. 상태 확인 (37쪽)

```bash
git status
```
- `Unmerged paths:` 아래에 `both modified: calculator.py` 가 보입니다 → 양쪽 branch가 모두 고친 파일이라는 뜻.

### 5-6. 충돌 표시(Conflict Marker) 읽기 (38쪽)

calculator.py를 열면 Git이 이런 표시를 넣어 놓았습니다.
```
def add(a, b):
<<<<<<< HEAD
    print("add called")
=======
    print("calculating...")
>>>>>>> feature/add-message
    return a + b
```
- `<<<<<<< HEAD` ~ `=======` : **현재 branch(main)** 의 내용 (Current)
- `=======` ~ `>>>>>>> feature/add-message` : **합치려는 branch** 의 내용 (Incoming)

### 5-7. 사람이 최종 코드 결정 + 마커 제거 (39~40쪽)

한쪽만 고르거나, 둘 다 쓰거나, 새로 쓸 수도 있습니다. 여기서는 둘 다 남깁니다.
```python
def add(a, b):
    print("add called")
    print("calculating...")
    return a + b
```
- ⚠ `<<<<<<<`, `=======`, `>>>>>>>` 기호를 **반드시 모두 지우고** 저장하세요. 남아 있으면 해결된 게 아니고, Python 실행 시 문법 오류가 납니다.

### 5-8. 고쳤는데 왜 아직 충돌? → git add (41~42쪽)

```bash
git status          # 아직 both modified 로 나옴
git add calculator.py
git status
```
- 파일을 고친 것과 **Git에게 "해결했어"라고 알려주는 것은 별개** 입니다.
- 충돌 중의 `git add` 는 "이 파일의 최종 결과를 결정했다 = **해결 완료**" 라는 표시입니다.
- 이후 status: `All conflicts fixed but you are still merging.`

### 5-9. merge commit으로 마무리 (43~44쪽)

```bash
git commit -m "Resolve add function conflict"
git status
git log --graph --oneline --decorate --all
```
- commit하면 merge가 끝납니다. 그래프에서 **부모가 두 개인 merge commit** 이 생긴 걸 확인합니다.

### 5-10. (선택) 충돌 해결 포기하기 (45쪽)

```bash
git merge --abort
git status
```
- 잘못된 branch를 합쳤거나 처음부터 다시 하고 싶을 때, **merge 진행 중에** 실행하면 merge 시작 전 상태로 돌아갑니다. (이미 commit으로 끝낸 뒤에는 쓸 수 없습니다.)

### 5-11. VS Code Merge Editor (46쪽)

VS Code에서 충돌 파일을 열면 마커 위에 **Accept Current / Accept Incoming / Accept Both** 버튼이 뜨고, Merge Editor 화면도 제공합니다. 다만 **마커를 직접 읽어 본 뒤** 도구를 쓰는 게 좋습니다.

---

## 단계 6. git pull과 pull 전략 (47~56쪽) — 개념 위주

### 6-1. git pull이란? (47쪽)

```bash
git pull
# 개념적으로 =
git fetch          # 원격의 새 commit을 가져오기만 함
+ merge 또는 rebase  # 가져온 것을 현재 branch에 합침
```
- push의 반대 방향입니다. **원격(GitHub)의 변경을 받아와 내 branch에 합칩니다.**

### 6-2. 이력이 갈라진 경우 (48쪽)

원격(origin/main)에는 다른 사람이 A→B를 올렸고, 내 로컬 main에는 X→Y가 생긴 상황(**divergent history**). 이때 Git은 "어떻게 합칠지" 방법을 알아야 합니다. 방법은 세 가지입니다.

### 6-3. 세 가지 방법

**① `git pull --no-rebase` (merge 방식, 49쪽)**
```
C1 ── A ── B ──┐
  \             M   ← main
   X ── Y ──────┘
```
- 양쪽 이력을 **그대로 보존**하고 merge commit(M)으로 합칩니다. 2차시에서 배운 merge와 같습니다.

**② `git pull --rebase` (rebase 방식, 50~51쪽)**
```
Rebase 전:  C1 ── A ── B        (origin/main)
              \
               X ── Y           (local main)

Rebase 후:  C1 ── A ── B ── X' ── Y'   (main)
```
- X, Y를 그냥 옮기는 게 아니라, X와 Y가 만든 **변경분(ΔX, ΔY)을 뽑아서 B 위에 다시 적용** 해 **새 commit X', Y'** 를 만듭니다.
- 그래서 X'와 X는 **commit ID(해시)가 다릅니다.** 결과는 한 줄로 깔끔한 **선형 이력** 입니다.
- ⚠ **이미 다른 사람과 공유한 commit은 함부로 rebase하지 않는 것**이 기본 원칙입니다 (다른 사람이 가진 X가 갑자기 X'로 바뀌어 꼬이기 때문).

**③ `git pull --ff-only` (fast-forward만 허용, 52~53쪽)**
- **Fast-forward란?** 내 main에 나만의 새 commit이 없고 원격보다 **단순히 뒤처져 있기만** 할 때, merge commit 없이 이름표만 원격 최신 commit으로 **앞으로 쭉 당기는 것**.
```
C0 ── C1 ── A ── B
      ↑          ↑
   main(전)   main, origin/main(후)
```
- `--ff-only` 는 이 경우에만 pull하고, **이력이 갈라져 있으면 아무것도 안 하고 중단** 합니다. 가장 안전한 방식입니다.

### 6-4. 한눈에 비교 (54쪽)

| 명령 | 이력이 갈라졌을 때 | 결과 |
|---|---|---|
| `git pull --no-rebase` | Merge | 이력 보존, 필요 시 merge commit |
| `git pull --rebase` | Rebase | 로컬 commit 재배치, 선형 이력 |
| `git pull --ff-only` | 중단 | Fast-forward 가능할 때만 진행 |

### 6-5. 기본 정책 설정 (55쪽)

매번 옵션을 쓰기 귀찮으면 기본값을 정해둘 수 있습니다 (셋 중 하나만).
```bash
git config pull.rebase false   # 기본을 merge로
git config pull.rebase true    # 기본을 rebase로
git config pull.ff only        # 기본을 ff-only로
```
- `--global` 을 붙이지 않으면 **현재 저장소에만** 적용됩니다.
- 💡 설정이 없는 상태에서 이력이 갈라진 채 `git pull` 을 하면 "어떻게 합칠지 정하라"는 안내(hint)가 나옵니다. 이 설정이 그 답입니다.

### 6-6. 수업에서의 선택 (56쪽)

이번 차시는 merge와 conflict 이해가 핵심이므로 **`--no-rebase` 중심**으로 씁니다. rebase는 그래프 변화 원리만 이해하고, 복잡한 실습은 뒤 차시로 미룹니다.

---

## 단계 7. 되돌리기: restore · reset · revert (57~61쪽)

"reverse", "revoke" 로 헷갈리기 쉽지만 실제 명령은 **restore, reset, revert** 입니다. **무엇을 되돌리느냐**에 따라 다릅니다.

| 명령 | 대상 | 핵심 |
|---|---|---|
| `restore` | 파일 / staging | 파일 변경 또는 stage 상태를 되돌림 |
| `reset` | HEAD / branch | branch 이름표를 과거 commit으로 옮김 |
| `revert` | 공유된 commit | 이력은 남기고, 취소하는 **새 commit** 을 추가 |

### 7-1. 수정한 내용 버리기 — restore (57쪽)

```bash
git diff                    # 무엇이 사라질지 먼저 확인!
git restore calculator.py   # 수정 전으로 되돌림
git status
```
- **아직 add하지 않은** 파일 수정을 마지막 저장 상태로 되돌립니다.
- ⚠ 되돌린 수정 내용은 **복구할 수 없습니다.** 그래서 먼저 `git diff` 로 확인합니다.
- 💡 실습해 보려면 calculator.py에 아무 줄이나 추가한 뒤 해보세요.

### 7-2. add 취소하기 — restore --staged (58쪽)

```bash
git restore --staged calculator.py
git status
```
- 파일 내용은 **그대로 두고** Staging Area(장바구니)에서만 내립니다. `Changes to be committed` → `Changes not staged` 로 바뀝니다.

### 7-3. commit 자체 되돌리기 — reset (59~60쪽)

```bash
git reset --soft HEAD~1
git status
```
- `HEAD~1` : "HEAD에서 한 칸 전 commit". (`HEAD~2` 는 두 칸 전)
- branch 이름표를 한 칸 전 commit으로 옮깁니다. 즉 **마지막 commit을 취소**합니다.
- ⚠ **실습용 branch에서만** 하세요.

| 옵션 | Branch 이름표 | Staging Area | 내 파일(Working Dir) |
|---|---|---|---|
| `--soft` | 이동 | 유지 (변경이 stage에 남음) | 유지 |
| `--mixed` (기본값) | 이동 | 취소 | 유지 |
| `--hard` | 이동 | 취소 | **취소 (파일 수정도 사라짐!)** |

- `--soft` : "commit만 취소, 다시 commit할 준비된 상태로" → commit 메시지를 잘못 썼을 때 유용
- `--hard` 는 실제 파일 변경까지 날아가므로 **특히 주의**!

### 7-4. 공유한 commit 취소 — revert (61쪽)

```bash
git revert <commit-hash>
```
- `<commit-hash>` 자리에 `git log --oneline` 에서 본 commit ID(예: `72bc213`)를 넣습니다. `< >` 기호는 입력하지 않습니다.
- 과거 commit을 지우지 않고, 그 **변경 효과를 반대로 적용하는 새 commit(R)** 을 만듭니다.
```
C0 ── C1 ── C2 ── C3 ── R   (R = C3를 취소하는 commit, C3는 기록에 남음)
```
- 이미 push해서 다른 사람과 공유한 이력은 reset으로 지우면 안 되고 **revert** 를 씁니다.

---

## 단계 8. branch 정리 (62쪽)

```bash
git branch                    # 목록 확인
git branch -d feature/sub     # merge 끝난 branch 삭제
git branch -d feature/div
```
- `-d` : merge가 끝난 branch만 삭제 (안전). merge 안 된 branch면 거부합니다.
- `-D` : merge 여부와 관계없이 **강제 삭제** → 신중하게.
- branch를 지워도 이미 main에 합쳐진 commit은 사라지지 않습니다. 이름표만 떼는 것입니다.
- 💡 같은 방식으로 `feature/add-validation`, `feature/add-message` 도 지울 수 있습니다.

---

## 혼자 연습하기 (63~64쪽)

각 단계 후 `git status` 와 `git log --graph --oneline --decorate --all` 로 확인하세요.

**① 자동 merge**
1. main과 calculator.py baseline 상태 확인
2. main에서 `feature/sub`, `feature/div` 를 **각각** 만들기
3. 각 branch에서 sub, div 작성 후 commit
4. 두 branch를 main에 차례로 merge → 최종 파일과 그래프 확인

**② 충돌과 복구**
1. main에서 두 branch를 만들어 add()의 같은 위치를 서로 다르게 수정
2. Conflict Marker 확인 → 최종 코드 결정 → `git add` + `git commit` 으로 merge 완료
3. `--no-rebase`, `--rebase`, `--ff-only` 결과를 그래프로 설명해 보기
4. `restore`, `reset`, `revert` 가 각각 무엇을 되돌리는지 확인

## 확인 질문 (65쪽) + 모범 답안

| 질문 | 답 |
|---|---|
| 왜 feature/div는 feature/sub가 아니라 main에서 만들어야 하나? | feature/sub에서 만들면 sub commit까지 딸려 들어가서 두 작업이 독립적이지 않게 되기 때문 |
| 같은 파일인데도 자동 merge되는 경우는? | 두 변경의 위치(줄)가 충분히 떨어져 있을 때. Git은 의미가 아니라 텍스트 위치로 비교함 |
| conflict 해결 후 왜 git add가 필요한가? | 파일 편집과 별개로 "이 파일은 해결 완료"라고 Git에 표시해야 하기 때문 |
| --rebase와 --no-rebase의 이력 차이는? | --no-rebase는 양쪽 이력 보존 + merge commit, --rebase는 내 commit을 새로 만들어 뒤에 붙인 한 줄짜리 이력 |
| --ff-only는 언제 중단되나? | 로컬과 원격 이력이 갈라져서 fast-forward가 불가능할 때 |

## 2차시 핵심 요약 (66쪽)

- **branch** 는 작업 흐름을 분리한다.
- **merge** 는 서로 다른 이력을 통합한다.
- **conflict** 는 사람이 의미를 결정해야 하는 지점이다.
- **pull** 은 원격 변경을 가져온 뒤 merge/rebase 등의 정책으로 통합한다.

**다음 차시(3차시) 예고:** 이 로컬 Git 흐름을 GitHub Remote, push, **Pull Request, Review, Merge** 의 실제 협업 절차로 연결합니다.

---

# 3차시: GitHub 협업과 Pull Request

> **한 줄 요약:** 1~2차시에 내 컴퓨터에서 하던 Git 작업(branch, commit, merge)을 GitHub 위로 옮겨서, **Issue → Branch → Push → Pull Request → Code Review → Merge** 라는 실제 팀 협업 절차로 연결하는 챕터입니다.
>
> **의의:** 지금까지는 "나 혼자 내 저장소에서 merge"했다면, 이제는 **"내 변경을 팀에게 제안하고, 검토받고, 규칙에 맞게 합치는"** 방법을 배웁니다. 그리고 누가 무엇을 할 수 있는지(권한), main을 어떤 조건에서 바꿀 수 있는지(Ruleset), 누가 검토하는지(CODEOWNERS)까지 다룹니다. 오픈소스나 회사에서 실제로 일하는 방식 그 자체입니다.

💡 이번 차시는 **명령어보다 GitHub 웹 화면과 개념이 중심**입니다. 실습 명령어는 뒷부분(Part III)에 모여 있습니다.

## Part I. 복습: 핵심 용어와 전체 흐름 (2~3쪽)

| 개념 | 의미 |
|---|---|
| Remote Repository | GitHub에 있는 팀 공유 저장소 |
| Clone | Remote의 파일 + Git 이력 + 저장소 정보를 내 컴퓨터로 복제 |
| origin | clone할 때 자동으로 붙는 원격 저장소 별칭 |
| Working Directory | 지금 편집 중인 실제 파일 |
| Staging Area | 다음 commit에 넣을 변경을 준비하는 곳 |
| Commit | 변경 상태를 로컬 Git 이력에 기록 |
| Feature Branch | main과 분리해서 특정 작업을 하는 작업 갈래 |
| Push | 로컬 branch와 commit을 원격에 올림(게시) |

**전체 흐름:**
```
Working Directory → Staging Area → Commit → Feature Branch → Push
   → Pull Request → Code Review → Merge
```
앞쪽(Push까지)은 1~2차시에 내 컴퓨터에서 배운 것이고, **뒤쪽(Pull Request부터)이 이번 시간에 GitHub에서 새로 배우는 부분**입니다.

---

## Part II. GitHub Repository 화면 둘러보기 (4~14쪽)

GitHub 저장소 페이지 위쪽에는 여러 탭(메뉴)이 있습니다. 저장소는 코드만 두는 곳이 아니라 **할 일 관리 → 개발 → 검토 → 자동화 → 보안 → 분석 → 정책 관리**가 모두 연결된 협업 공간입니다.

| 탭 | 한 줄 설명 | 비유 |
|---|---|---|
| **Code** | 파일, 폴더, branch, commit 이력 보기 | 프로젝트 폴더 |
| **Issues** | 할 일·버그·아이디어 기록 | 할 일 목록 / 게시판 |
| **Pull requests** | 변경을 검토하고 main에 합치는 곳 | 결재 서류함 |
| **Agents** | AI 코딩 에이전트에게 작업 맡기기 | AI 조수 |
| **Actions** | 테스트·빌드·배포 자동 실행 | 자동 검사 로봇 |
| **Projects** | Issue와 PR을 칸반 보드로 관리 | 업무 보드 |
| **Wiki** | 긴 프로젝트 문서 | 프로젝트 위키백과 |
| **Security and quality** | 보안 위험 검사 결과 | 보안 점검표 |
| **Insights** | 활동 통계 | 통계 대시보드 |
| **Settings** | 권한, 규칙 등 저장소 정책 설정 | 관리자 설정 |

### 1. Code (5쪽)
- 파일·폴더 탐색, **branch 선택 및 비교**, commit/파일 이력 확인.
- 왼쪽 위의 branch 선택 버튼(`main ▾`)으로 branch를 바꾸면, **같은 저장소 안에서도 다른 개발 상태**를 볼 수 있습니다. (2차시에서 `git switch` 하면 파일이 바뀌던 것과 같은 원리)
- `Commits` → 특정 commit 클릭 → 그 commit의 diff를 볼 수 있습니다.

### 2. Issues (6쪽)
- 기능, 버그, 개선 요청, 아이디어처럼 **추적해야 할 작업**을 기록하고 토론하는 곳.
- **Assignee**(담당자), **Label**(분류표: bug, enhancement 등), **Milestone**(목표 시점)을 붙일 수 있습니다.
- 예시 흐름:
  ```
  Issue #12 "Add GET /todos endpoint" (담당: 백엔드, Label: enhancement, Open)
    ↓ branch: feature/12-get-todos 에서 작업
    ↓ Pull Request #18 생성
    ↓ Merge → Issue #12 자동으로 Closed
  ```

### 3. Pull requests (7쪽)
- **Pull Request(PR)** = "내 branch의 변경을 main에 합쳐 주세요"라는 **제안서**입니다. 합치기 전에 diff, 리뷰, 자동 검사, merge 가능 여부를 한곳에서 다룹니다.
- PR 화면 안의 탭:
  - **Conversation**: 토론과 리뷰 댓글
  - **Commits**: 이 PR에 포함된 commit 목록
  - **Checks**: 자동 검사(Actions) 결과
  - **Files changed**: 실제로 바뀐 코드(diff)
- `base: main` ← `compare: feature/get-todos` : **compare branch의 변경을 base branch에 합치겠다**는 뜻입니다.
- 리뷰 흐름 예: Files changed 확인 → 리뷰 댓글 → 수정 요청(Request changes) → 추가 commit → 승인(Approve) → Merge
- 💡 이름이 "Pull" Request인 이유: "제 변경을 당겨(pull) 가 주세요"라고 요청하는 것이기 때문입니다. `git pull` 명령과는 다른 것입니다.

### 4. Agents (8쪽)
- AI 코딩 에이전트(예: Copilot)에게 개발 작업을 맡기고 진행 상황을 보는 곳.
- 프롬프트로 작업 요청하거나 Issue를 에이전트에게 할당 → 에이전트가 **branch에서 코드 변경, 테스트, PR 생성** → **사람이 diff를 검토하고 merge**.
- 핵심: AI가 코드를 써도 **최종 결정은 기존 Branch · PR · Review 흐름 안에서 사람이** 합니다.

### 5. Actions (9쪽)
- push나 PR 같은 **이벤트가 생기면 자동으로** 빌드·테스트·배포를 실행하는 기능 (CI/CD라고 부름).
- 예: PR 열림 → Actions가 코드 받아서(checkout) → 라이브러리 설치 → `pytest`로 테스트 → ✓ 통과 → Ruleset 검사 조건 충족 → Merge 가능
- 설정 파일은 `.github/workflows/*.yml` 이며, 뒤의 CI/CD 차시에서 자세히 다룹니다.

### 6. Projects (10쪽)
- Issue와 PR을 **Table, Board(칸반), Roadmap** 형태로 정리해 진행 상태와 우선순위를 관리.
- `Backlog → Todo → In Progress → Done` 같은 칸으로 관리하고, **PR이 merge되면 자동으로 Done으로 옮기는** 것도 가능.
- Notion은 범용 문서·관리에 강하고, GitHub Projects는 **Issue·PR과 직접 연결**되는 게 장점.

### 7. Wiki (11쪽)
- README보다 **자세하고 오래 유지할 문서**(아키텍처, API 규칙, 설치·운영 가이드, 설계 배경)를 두는 곳.
- README = 프로젝트 빠른 소개, Wiki = 상세한 장기 문서.
- Wiki도 내부적으로 Git 저장소라서 수정 이력이 commit으로 남습니다.

### 8. Security and quality (12쪽)
- 코드, 의존 라이브러리, 비밀번호/키 노출 등에 대한 보안·품질 분석 결과를 보는 곳.
  - **Dependabot alerts**: 내가 쓰는 라이브러리에 알려진 취약점이 있으면 알림
  - **Code scanning**: 코드의 보안 취약점 자동 검사
  - **Secret scanning**: 코드에 실수로 올라간 비밀번호·API 키 탐지
- Ruleset과 합치면 **보안 검사를 통과하지 못한 변경은 merge 못 하게** 막을 수 있습니다.

### 9. Insights (13쪽)
- 기여자(Contributors), commit 활동, 방문자(Traffic), Fork 관계(Network) 등 **통계**를 보는 곳.
- 주의: commit 수만으로 개인 기여도를 단순 평가하기보다, **저장소 활동 흐름을 이해하는 자료**로 보는 것이 적절합니다.

### 10. Settings (14쪽)
- 접근 권한, branch 정책, Actions 권한, 보안 설정 등 **저장소 운영 정책**을 정하는 관리 화면.
```
Settings
  ├─ Access   → Role / Permission (누가 무엇을 할 수 있나)
  ├─ Rules    → Ruleset (branch를 어떤 조건에서 바꿀 수 있나)
  ├─ Actions  → Workflow policy
  └─ Security → Analysis settings
```
- 이어지는 Access → Role → Ruleset 설명이 모두 이 Settings 안에서 설정하는 내용입니다.

---

## Part III. 접근 권한(Access)과 역할(Role) (15~19쪽)

### 1. Repository Role 5단계 (15쪽)

조직(Organization) 저장소에서는 사람, 외부 협력자(Outside collaborator), 팀(Team)마다 다른 역할을 줄 수 있습니다. 아래로 갈수록 권한이 커집니다.

| Role | 누구에게? |
|---|---|
| **Read** | 코드를 보고 토론만 하는 사람 (코드 수정 X) |
| **Triage** | 코드는 못 고치지만 Issue·PR을 정리·관리하는 사람 |
| **Write** | 코드를 직접 push하며 적극적으로 기여하는 사람 |
| **Maintain** | 위험한 작업(삭제 등) 없이 저장소를 관리하는 프로젝트 관리자 |
| **Admin** | 보안·삭제 포함 **모든 권한**이 필요한 사람 |

### 2. Write · Maintain · Admin 차이 (16쪽)

| 할 수 있는 일 | Write | Maintain | Admin |
|---|:-:|:-:|:-:|
| Push | ✓ | ✓ | ✓ |
| 리뷰 승인 / 수정 요청 | ✓ | ✓ | ✓ |
| PR Merge | ✓ | ✓ | ✓ |
| PR merge 방식 설정 | — | ✓ | ✓ |
| Ruleset 관리 | — | — | ✓ |
| 사용자·팀 권한 관리 | — | — | ✓ |

- ⭐ Role은 회사 직책(팀장, 사원)이 아니라 **GitHub 기능에 대한 접근 권한**입니다.

### 3. Organization Base Permission (17쪽)
- **Base permission** = 조직 멤버가 조직 저장소에 대해 **기본으로** 갖는 권한 수준.
- 위치: `Organization → Settings → Member privileges → Base permissions`
- 저장소별로 개인이나 팀에게 따로 권한을 더 줄 수 있고, **외부 협력자에게는 Base permission이 적용되지 않습니다.**

### 4. 누가 접근할 수 있는지 확인·관리 (18~19쪽)
- 확인: `Repository → Settings → Collaborators and teams (또는 Access)` 에서 사람·팀·Role을 한눈에 봄.
- 관리: 사용자 선택 → Role 지정·변경·제거. **Admin** 권한이 있어야 합니다.
- 💡 개인 계정 저장소에 친구를 초대할 때는 `Settings → Collaborators → Add people` 로 초대합니다.

---

## Part IV. Ruleset: branch 보호 규칙 (20~24쪽)

### 1. Ruleset이란? (20쪽)
- 특정 branch(또는 tag)에 대해 **사람들이 어떻게 변경할 수 있는지 통제하는 규칙 묶음**.
- 위치: `Repository → Settings → Rules → Rulesets → New branch ruleset`
- 💡 왜 필요할까? 누구나 main에 바로 push하면 검토 안 된 코드가 들어가거나 실수로 이력이 날아갈 수 있습니다. Ruleset으로 "main은 PR과 리뷰를 거쳐야만 바뀐다"를 **강제**할 수 있습니다.

### 2. Ruleset 구성 요소 (21쪽)

| 항목 | 의미 |
|---|---|
| Ruleset name | 규칙 묶음 이름 |
| **Enforcement status** | **Active** 면 실제로 적용됨 (Disabled면 꺼짐) |
| **Bypass list** | 규칙을 무시할 수 있는 예외 사용자·팀·앱 |
| **Target branches** | 적용할 branch (예: `main`, 또는 패턴) |
| Branch rules | 실제 규칙들 (아래 표) |

### 3. branch 보호·이력 관련 규칙 (22쪽)

| Rule | 의미 |
|---|---|
| Restrict creations | 예외 권한자만 해당 branch **생성** 가능 |
| Restrict updates | 예외 권한자만 해당 branch에 **직접 push** 가능 |
| Restrict deletions | 예외 권한자만 해당 branch **삭제** 가능 |
| Require linear history | merge commit 금지 → 이력을 **한 줄**로 유지 (2차시 rebase 개념) |
| Require signed commits | 검증된 **서명**이 있는 commit만 허용 |
| Block force pushes | **force push**(강제로 이력 덮어쓰기) 금지 |

💡 **force push** 란? `git push --force` 로 원격 이력을 내 이력으로 강제로 덮어쓰는 것. 다른 사람 commit이 사라질 수 있어 위험합니다.

### 4. PR·자동 검사 관련 규칙 (23쪽)

| Rule | 의미 |
|---|---|
| **Require a pull request before merging** | main에 직접 push 금지, **다른 branch에서 작업 후 PR로만** 반영 |
| Required approving reviews | merge 전 필요한 **승인(Approve) 개수** |
| Require status checks to pass | 지정한 자동 검사(예: Actions 테스트)를 **통과해야** 반영 |
| Require deployments to succeed | 지정 환경에 배포가 성공해야 반영 |
| Code scanning / quality / coverage | 보안·품질·테스트 커버리지 결과를 merge 조건으로 |

### 5. 예시: PR 기반 main 보호 (24쪽)
```
Target branch:  main
Branch rules:
  Restrict deletions                      ← main 삭제 금지
  Require a pull request before merging   ← PR로만 변경
      Required approvals: 1               ← 최소 1명 승인 필요
  Block force pushes                      ← 강제 덮어쓰기 금지
```
- 이렇게 하면 main의 모든 변경이 **PR과 리뷰 기록과 연결**됩니다. "이 코드는 언제, 누가 검토하고 들어왔나"를 항상 추적할 수 있습니다.

---

## Part V. 실습 흐름: Issue에서 Merge까지 (25~39쪽)

### 실습 전체 상황 한눈에 보기 (25쪽)

```
① Issue 생성 → ② Feature Branch 생성 → ③ 코드 변경·Commit → ④ Push
  → ⑤ Pull Request 생성 → ⑥ Code Review → ⑦ 수정 Commit
  → ⑧ Merge + Issue Close → ⑨ Branch 정리
```
- **Issue** = 무슨 일을 하는지 추적, **Branch** = 독립된 변경 이력, **Pull Request** = 변경 제안과 리뷰 기록. 이 셋이 서로 연결되는 게 핵심입니다.
- 슬라이드 예시는 FastAPI(파이썬 웹 서버) 프로젝트를 초기화하는 작업(`feature/project-init`)입니다.

### ① Issue 생성 (26쪽) — 웹에서

- 저장소 **Issues 탭 → New issue** → 제목 작성 → Submit.
- 예: `Issue #1 Project initialization`, `Issue #3 Implement GET /todos endpoint`
- 생성되면 **번호(#1)** 가 붙습니다. 이 번호를 branch 이름, PR, commit 메시지에 써서 작업끼리 연결합니다.

### ② Feature Branch 생성 (27~29쪽)

```bash
git switch main                      # main으로 이동
git pull                             # GitHub의 최신 main을 받아옴
git switch -c feature/project-init   # 새 작업 branch 만들고 이동
```
- `git pull` 을 먼저 하는 이유: 다른 팀원이 그사이 main에 합친 내용이 있을 수 있어서, **최신 main에서 출발**해야 나중에 충돌이 줄어듭니다.
- 이후 기능 구현 때는 `feature/get-todos` 같은 이름을 씁니다.

**Branch 이름 짓기 관례 (28쪽):** `<종류>/<짧은-설명>`

| 접두어 | 의미 | 예 |
|---|---|---|
| `feature/` | 새 기능 | `feature/get-todos` |
| `fix/` | 버그 수정 | `fix/divide-by-zero` |
| `docs/` | 문서 변경 | `docs/update-readme` |
| `test/` | 테스트 추가·수정 | `test/add-api-test` |
| `refactor/` | 기능 변화 없이 구조 개선 | `refactor/todo-model` |

- 이건 GitHub가 강제하는 게 아니라 **팀이 합의하는 약속**입니다.

**쓸 수 있는 문자 (29쪽):** 영문 대소문자, 숫자, `.` `-` `_` `/` 정도만 쓰는 게 안전합니다. 특수문자는 터미널에서 다른 의미가 될 수 있고, **문자로 시작하는 이름**을 권장합니다. (💡 띄어쓰기와 한글은 피하세요.)

### ③ 코드 변경과 Commit (30쪽)

```bash
git status                                   # 무엇이 바뀌었나 확인
git diff                                     # 바뀐 내용 자세히
git add .                                    # 바뀐 파일 전부 stage
git diff --staged                            # commit될 내용 최종 확인
git commit -m "Initialize FastAPI project"   # commit
```
- 2차시에서 반복한 **수정 → diff → add → diff --staged → commit** 루틴 그대로입니다.
- `git add .` : 현재 폴더 아래 바뀐 파일 **전부**를 stage. (`.` 은 "현재 폴더"라는 뜻)

### ④ Feature Branch Push (31쪽)

```bash
git push -u origin feature/project-init
```
- 내 **feature branch** 와 commit을 GitHub에 올립니다. (1차시에는 main을 push했지만 이번엔 작업 branch를 push)
- `-u` : 이 branch의 기본 원격 짝을 설정 → 다음부터는 `git push` 만 쳐도 됨.
- ⭐ **이 시점까지 main은 전혀 바뀌지 않습니다.** GitHub에서 main과 feature branch를 비교할 수 있게 된 것뿐입니다.
- 💡 push 직후 GitHub 저장소 페이지에 노란 배너로 **"Compare & pull request"** 버튼이 뜹니다. 그걸 누르면 바로 ⑤로 넘어갈 수 있어요.

### ⑤ Pull Request 생성 (32~34쪽) — 웹에서

**Pull requests 탭 → New pull request** (또는 위 배너 버튼)
```
base:    main                      ← 합쳐질 곳 (받는 쪽)
compare: feature/project-init      ← 내 변경 (보내는 쪽)

Title:  Initialize FastAPI project
Body:   Closes #1
```
- ⚠ base와 compare 방향을 헷갈리지 마세요. **compare → base** 로 합쳐집니다.
- **`Closes #1`** : 이 PR이 merge되면 **Issue #1이 자동으로 닫힙니다.** (closing keyword)

**Issue · Branch · PR 연결 (33쪽):**
```
Issue #12 → feature/12-get-todos → PR #18 → main에 Merge → Issue #12 자동 Closed
```
- 자동 종료 키워드: `Closes #12`, `Fixes #12`, `Resolves #12` (셋 다 같은 효과)
- PR이 **기본 branch(main)를 대상**으로 할 때만 자동 종료됩니다.
- 다른 저장소의 Issue는 `Fixes owner/repository#100` 처럼 저장소까지 적습니다.

**좋은 PR 본문 예시 (34쪽):**
```markdown
## Summary
- GET /todos endpoint 구현

## Changes
- Todo response model 정의
- GET /todos 구현

## Test
- pytest PASS

## Related Issue
Closes #3
```
| 섹션 | 쓰는 내용 |
|---|---|
| Summary | 변경 목적과 핵심 결과 |
| Changes | 주요 변경 파일·기능 |
| Test | 어떻게 확인했고 결과는 어땠는지 |
| Related Issue | 관련 Issue (+ 자동 종료 키워드) |

- PR 본문은 **diff만 봐서는 알기 어려운 "왜, 어떻게 확인했는지"** 를 리뷰어에게 알려주는 역할입니다.
- 💡 `##` 은 마크다운 제목 문법입니다. GitHub에서 굵은 소제목으로 보입니다.

### ⑥ Files changed와 Code Review (35쪽) — 웹에서

- PR의 **Files changed** 탭에서 base와 compare 사이 실제 diff를 보고, **특정 코드 줄에 댓글**을 남길 수 있습니다 (줄 번호 옆 `+` 버튼).
- 리뷰 제출 시 셋 중 하나를 고릅니다.
  - **Comment**: 의견만 남김
  - **Approve**: 승인 (merge해도 좋다)
  - **Request changes**: 수정 요청 (고치기 전엔 안 됨)
- 리뷰 결과와 이후 수정 commit은 **같은 PR 안에서** 이어서 기록됩니다.

### ⑦ 리뷰 반영과 추가 Commit (36~37쪽)

```bash
# 같은 feature branch에서 그대로 수정
git diff
git add .
git commit -m "Add API metadata"
git push
```
- ⭐ PR을 새로 만들 필요가 없습니다! **같은 branch에 push하면 기존 PR이 자동으로 최신 상태로 업데이트**됩니다.
- 이미 ④에서 `-u` 로 설정했으므로 그냥 `git push` 만 쓰면 됩니다.

**새 commit과 기존 승인 (37쪽):**
- Ruleset에서 **"Dismiss stale pull request approvals when new commits are pushed"** 를 켜면, 승인 후 새 commit이 push되어 diff가 바뀌면 **기존 승인이 취소(stale)** 되고 다시 승인받아야 합니다.
- 의미: 리뷰어가 승인한 건 "PR이라는 이름"이 아니라 **그 시점의 변경 내용(diff)** 이기 때문입니다. 승인 후 몰래 코드를 바꾸는 걸 막아줍니다.

### ⑧ Merge와 Issue Close (38쪽) — 웹에서

PR 아래쪽 **Merge pull request** 버튼 옆 ▾ 에서 방식을 고릅니다.

| Merge 방식 | Git 이력 결과 |
|---|---|
| **Create a merge commit** | feature commit들을 그대로 두고 별도 merge commit 생성 (2차시의 `--no-rebase` 와 비슷) |
| **Squash and merge** | feature의 여러 commit을 **하나의 commit으로 합쳐서** 반영 |
| **Rebase and merge** | feature commit들을 main 위에 다시 붙여 한 줄 이력 (2차시의 `--rebase` 와 비슷) |

- `Closes #1` 이 들어간 PR이 main에 merge되면 Issue #1도 자동으로 닫힙니다.

### ⑨ Merge 이후 정리 (39쪽)

```bash
git switch main                              # main으로 돌아옴
git pull                                     # GitHub에서 merge된 최신 main을 받아옴
git branch -d feature/project-init           # 다 쓴 로컬 작업 branch 삭제
git log --oneline --graph --decorate --all   # 이력 확인
```
- ⭐ merge는 **GitHub(원격)에서** 일어났기 때문에, 내 컴퓨터의 main은 아직 옛날 상태입니다. 그래서 `git pull` 로 받아와야 합니다.
- branch를 지워도 이미 merge된 commit과 이력은 남습니다 (이름표만 떼는 것).
- 💡 GitHub에 남은 원격 branch는 PR 화면의 **Delete branch** 버튼으로 지울 수 있습니다.

---

## Part VI. CODEOWNERS: 리뷰어 자동 지정 (40~44쪽)

### 1. CODEOWNERS란? (40쪽)
- 저장소의 **특정 파일·폴더에 책임이 있는 사람이나 팀**을 적어두는 파일.
- 동작: PR에서 파일이 바뀜 → CODEOWNERS 패턴 확인 → 해당 담당자를 **리뷰어로 자동 요청**

| 항목 | 내용 |
|---|---|
| 파일 위치 | `.github/CODEOWNERS`, 저장소 최상위, 또는 `docs/CODEOWNERS` |
| Owner | 사용자(`@아이디`) 또는 팀(`@조직/팀이름`) |
| 권한 | Code Owner는 저장소에 **Write 권한**이 있어야 함 |
| PR | 담당 파일이 바뀌면 그 Owner에게 리뷰 요청 |

- ⚠ CODEOWNERS만으로는 **리뷰 요청이 자동화될 뿐, 승인이 강제되지는 않습니다.** (강제하려면 Ruleset과 결합 → 3번)

### 2. 파일 작성법 (41쪽)
```
# .github/CODEOWNERS
# 기본 소유자 (모든 파일)
*              @org/project-leads

# 영역별 소유자
/backend/      @org/backend-team      ← backend 폴더
/frontend/     @org/frontend-team     ← frontend 폴더
/.github/      @org/devops-team       ← .github 폴더
docs/          @org/docs-team         ← 어디든 docs 폴더
*.py           @org/python-reviewers  ← 모든 .py 파일
```
- 한 줄 = **파일 패턴 + 담당자(1명 이상)**. `#` 으로 시작하는 줄은 주석.
- ⭐ 여러 패턴이 동시에 맞으면 **파일 아래쪽에 있는 패턴이 우선**합니다. 그래서 넓은 규칙(`*`)을 위에, 구체적인 규칙을 아래에 씁니다.
- 팀을 Owner로 쓰려면 그 팀이 공개(visible) 상태이고 저장소에 명시적인 Write 권한이 있어야 합니다.

### 3. PR에서의 동작 (42쪽)
```
바뀐 파일: backend/todo.py, backend/model.py
CODEOWNERS: /backend/  @org/backend-team
→ PR 생성 시 @org/backend-team 에게 자동 리뷰 요청
```
- 리뷰 요청에는 **PR의 base branch(main)에 있는 CODEOWNERS 파일**이 사용됩니다.
- **Draft PR**(초안 PR)에서는 자동 요청이 안 되고, **Ready for review** 로 바꾸면 그때 요청됩니다.

### 4. Ruleset과 결합: Code Owner 승인을 merge 조건으로 (43쪽)
```
Require a pull request before merging
  ✓ Required approvals: 1
  ✓ Require review from Code Owners
```
- 이렇게 설정하면 Code Owner가 지정된 파일을 바꾸는 PR은 **그 Owner의 승인 없이는 merge 불가**.
- 한 패턴에 Owner가 여러 명이면 **그중 한 명만 승인**해도 충족됩니다.

### 5. CODEOWNERS 파일 자체 보호 (44쪽)
- 누구나 CODEOWNERS를 고칠 수 있다면, 자기 마음대로 리뷰어를 바꿔 규칙을 우회할 수 있습니다.
- 그래서 **CODEOWNERS 파일과 `.github/` 폴더에도 Owner를 지정**합니다.
```
/.github/            @org/project-leads
/.github/CODEOWNERS  @org/project-leads
```
- 정리: CODEOWNERS는 "누가 이 영역을 검토하는가"를 **코드와 함께 버전 관리**하는 장치이고, Ruleset과 합치면 리뷰어 지정부터 merge 조건까지 이어집니다.

---

## Part VII. 계산기 예시로 보는 PR과 Conflict (45~48쪽)

### 1. 예시 저장소 (45~46쪽)

교수님 예시 저장소 `DBChoi85/git-practice2` 의 출발 상태:
```python
def add(a, b):
    return a + b

print(add(4, 3))
```
- 2차시처럼 `feature/sub`(sub 함수), `feature/div`(div 함수) branch를 따로 만들면, 이번엔 **각각 독립된 PR**로 올려서 리뷰·merge할 수 있습니다.
- 서로 다른 부분을 고쳤으니 두 PR 모두 충돌 없이 merge 가능.

### 2. 같은 영역을 고치면 Conflict (47쪽)

```python
# Branch A                     # Branch B
def add(a, b):                 def add(a, b):
    return a + b + 0               result = a + b
                                   return result
```
- 한쪽 PR이 먼저 main에 merge된 뒤, 다른 쪽이 최신 main을 합치려고 하면 **같은 부분(hunk)을 다르게 고쳤기 때문에 conflict**가 납니다.
- GitHub PR 화면에 "This branch has conflicts that must be resolved" 같은 메시지가 뜹니다.

### 3. 해결: 최신 main을 내 feature branch에 합치기 (48쪽)

**상황:** 내 PR(`feature/div`)에 conflict가 났습니다. 내 컴퓨터에서 최신 main을 내 branch에 합쳐서 충돌을 해결하고 다시 올립니다.

```bash
git fetch origin              # GitHub의 최신 내용을 받기만 함 (합치지는 않음)
git switch feature/div        # 내 작업 branch로 이동
git merge origin/main         # GitHub의 최신 main을 내 branch에 합침 → conflict 발생
# (calculator.py를 열어 <<<<<<< ======= >>>>>>> 마커 정리, 2차시 방법 그대로)
git add calculator.py         # 해결 완료 표시
git commit                    # merge commit 생성
git push                      # 해결된 branch를 다시 올림
```
- `git fetch origin` : 원격 변경을 **가져오기만** 하고 합치지 않습니다 (2차시: `pull = fetch + merge`).
- `origin/main` : "GitHub에 있는 main"을 내 컴퓨터에서 가리키는 이름. fetch로 최신화됩니다.
- `git merge origin/main` : 방향 주의! main에 내 branch를 합치는 게 아니라 **내 branch에 최신 main을 합치는** 것입니다.
- `git commit` 을 `-m` 없이 치면 편집기가 열리는데, 기본 merge 메시지 그대로 저장하고 닫으면 됩니다 (vim이면 `:wq`).
- push하면 **기존 PR에 해결 commit이 자동 반영**되어 conflict 표시가 사라지고 merge할 수 있게 됩니다.

---

## 3차시 전체 요약 (49쪽)

```
Repository Access → Ruleset → Feature Branch → Pull Request → Files changed
  → Code Review → Additional Commit → Merge → Issue Close → Git History
```
- **접근 권한(Access/Role)**: "누가 무엇을 할 수 있는가"
- **Ruleset**: "어떤 조건에서 branch가 바뀔 수 있는가"
- **Pull Request**: "어떤 변경을 어떻게 검토했는가"를 기록

## 스스로 점검 질문 (슬라이드에는 없는 연습용)

| 질문 | 답 |
|---|---|
| PR의 base와 compare는 각각 무엇? | base = 합쳐질 곳(보통 main), compare = 내 변경이 있는 branch |
| feature branch를 push하면 main이 바뀌나? | 아니요. PR이 merge되어야 main이 바뀜 |
| 리뷰 반영할 때 PR을 새로 만들어야 하나? | 아니요. 같은 branch에 push하면 기존 PR이 업데이트됨 |
| `Closes #3` 은 무슨 역할? | PR이 main에 merge될 때 Issue #3을 자동으로 닫음 |
| Write와 Admin의 가장 큰 차이는? | Admin만 Ruleset과 사용자 권한을 관리할 수 있음 |
| CODEOWNERS만 있으면 승인이 강제되나? | 아니요. 리뷰 요청만 자동. 강제하려면 Ruleset의 "Require review from Code Owners" 필요 |
| GitHub에서 merge 후 내 컴퓨터에서 할 일은? | `git switch main` → `git pull` 로 최신화, 다 쓴 branch 삭제 |
| PR에 conflict가 나면? | `git fetch origin` → 내 branch에서 `git merge origin/main` → 해결 → add, commit, push |

---

# 소프트웨어공학 10장: 테스팅

> 원본: `소프트웨어공학_10.pdf` (47쪽). 표지에는 "Architecture and Design Pattern / 아키텍처 설계와 패턴"이라고 적혀 있지만, 본문 전체는 **테스팅**을 다룹니다. 표지는 이전 장 템플릿이 남은 것으로 보입니다.

> **한 줄 요약:** 소프트웨어의 결함을 **체계적으로 찾아내는 방법**을 배우는 챕터입니다. 용어(오류·결함·장애, 검증·확인)부터 시작해 테스트 수준(단위·통합·시스템·인수), 테스트 케이스를 고르는 기법(동등 분할, 경계값, 결정 테이블, 조합, 커버리지, 상태 기반), 통합 순서 전략까지 다룹니다.
>
> **의의:** 1~3차시에서 Git과 GitHub로 "변경을 기록하고 함께 합치는 법"을 배웠다면, 이번 장은 **합치기 전에 그 변경이 맞는지 확인하는 법**입니다. 3차시에 나온 GitHub Actions의 자동 테스트나 PR의 "Require status checks to pass" 규칙이 바로 이 테스트를 자동으로 돌려 merge를 막는 장치입니다. 좋은 테스트를 설계할 줄 알아야 그 자동화가 의미가 있습니다.

💡 이 장은 **명령어 실습이 없는 이론 장**입니다. 대신 은행 출금, 회원가입 나이 검사 같은 예제로 "테스트 케이스를 어떻게 뽑는지"를 연습합니다. 아래에서는 각 예제를 **문제 → 푸는 방법 → 결과** 순서로 풀어 썼습니다.

## 학습 목표 (2쪽)
- 오류, 결함, 장애와 검증·확인을 구분한다.
- 단위·통합·시스템·인수 테스트의 역할을 설명한다.
- 동등 분할, 경계값, 결정 테이블로 테스트 케이스를 도출한다.
- 코드 커버리지와 테스트 자동화의 한계를 설명한다.

---

## Part 1. 테스팅 기초 (3~17쪽)

### 1. 왜 테스트하나? (3쪽)
소프트웨어는 **사람이** 요구사항을 해석하고 설계·구현하기 때문에 실수가 생깁니다.
- 요구사항을 잘못 이해함
- 로직이나 **경계 조건**(예: `<` 와 `<=`)이 틀림
- 기능끼리 예상 못 한 상호작용
- 고치다가 **다시 생긴 결함**

⭐ **테스트의 목적:** 품질을 "무조건 증명"하는 게 아니라, **위험과 결함을 발견하고 정보를 제공**하는 것.

### 2. 오류 · 결함 · 장애 (4~5쪽) — 시험 단골

| 용어 | 뜻 | 어디에 있나 | 예 |
|---|---|---|---|
| **오류 (Error)** | 사람이 저지른 잘못된 판단·행위 | 사람의 머리 | "18세 이상"을 "18세 초과"로 잘못 이해 |
| **결함 (Defect / Fault)** | 산출물(코드·설계·문서)에 남은 문제 | 코드·문서 | `if age > 18` 로 코딩됨 |
| **장애 (Failure)** | 실행 중 기대한 서비스를 못 하는 **눈에 보이는** 현상 | 실행 결과 | 18세가 가입을 거부당함 |

- 흐름: **오류 → 결함 → (특정 조건에서) 장애**
- ⭐ 결함이 있어도 그 조건이 실행되지 않으면 장애는 **안 보일 수 있습니다** (위 예에서 18세가 가입하기 전까지는 아무도 모름).
- **테스트**는 장애를 단서로 결함을 찾고, **디버깅**은 그 원인을 분석합니다.

### 3. 검증(Verification) vs 확인(Validation) (6쪽) — 시험 단골

| | 검증 Verification | 확인 Validation |
|---|---|---|
| 질문 | **제품을 올바르게** 만들었나? | **올바른 제품을** 만들었나? |
| 기준 | 명세·설계·규칙 | 실제 사용자의 목적·요구 |
| 예 | 출금 한도 규칙이 코드에 정확히 들어갔나? | 사용자에게 이 출금 절차가 편하고 믿을 만한가? |

- 슬라이드 질문: **"요구사항 자체가 틀렸는데 코드는 요구사항대로 동작한다면?"** → 검증은 통과하지만 확인은 실패합니다. 그래서 둘 다 필요합니다.

### 4. 테스팅 vs 디버깅 (7쪽)
- **테스트**: 실제 결과와 기대 결과의 **차이를 드러내는** 활동
- **디버깅**: 그 차이의 **원인을 찾아 고치는** 활동
- ⭐ "테스트 통과"는 **테스트한 조건에서만** 성공했다는 뜻입니다.

### 5. 테스트 원칙 6가지 (8쪽)

| 원칙 | 설명 |
|---|---|
| 완전성의 한계 | 모든 입력·상태·경로를 다 시험할 수는 없다 |
| 위험 기반 선택 | 결함 영향이 크고 발생 가능성이 높은 곳에 집중 |
| 빠른 피드백 | 결함은 일찍 발견할수록 유리 (고치는 비용이 적음) |
| 독립적인 관점 | 개발자가 놓친 가정을 다른 사람이 검토 |
| 회귀 검증 | 수정 후에도 **이전 기능이 그대로 동작**하는지 확인 |
| 자동화의 한계 | 자동으로 돌려도 **테스트 자체가 잘못 설계됐으면** 소용없다 |

💡 **회귀(regression)** 테스트는 2차시에서 merge 후 `python calculator.py` 로 기존 add가 여전히 되는지 확인한 것과 같은 개념입니다.

### 6. 테스트 설계와 테스트 케이스 (9~11쪽)
테스트는 **실행하기 전에 설계**합니다.
1. 목표와 검증할 요구사항을 정한다
2. 테스트 조건·데이터와 **예상 결과를 실행 전에** 적는다
3. 실행 후 실제 결과와 비교하고 실패를 분석한다

**좋은 테스트 케이스 예 (10쪽):**

| ID | 사전조건 | 입력/행동 | 기대 결과 | 결과 |
|---|---|---|---|---|
| WD-01 | 잔액 1,000원 | 500원 출금 | 성공 / 잔액 500원 | 미실행 |
| WD-02 | 잔액 1,000원 | 1,000원 출금 | 성공 / 잔액 0원 | 미실행 |
| WD-03 | 잔액 1,000원 | 1,001원 출금 | 거부 / 잔액 불변 | 미실행 |

**테스트 케이스 명세서의 조건 (11쪽):**
- 식별자, 시험 조건, 입력 데이터, 기대 결과를 구분해서 적는다
- **누가 실행해도 같은 절차로 반복**할 수 있어야 한다
- 실행 전에 적은 예상 결과가 판정 기준이 된다 → 이것을 **오라클(Oracle)** 이라고 부름

### 7. 요구사항에서 테스트 케이스 뽑기 (12~13쪽) — 예제

**문제:** 은행 출금 기능 요구사항
- R1. 출금액은 양의 정수다.
- R2. 출금액은 잔액을 초과할 수 없다.
- R3. 출금 성공 시 잔액이 감소한다.
- R4. 실패 시 잔액이 유지된다.

**푸는 방법:** 요구사항 → **정상 시나리오**(잔액 안에서 출금) + **예외 시나리오**(0, 음수, 잔액 초과)를 만들고, 각 시나리오에서 케이스를 뽑습니다.

| ID | 초기 잔액 | 출금액 | 기대 결과 | 검증하는 요구사항 |
|---|---|---|---|---|
| TC-01 | 1,000 | 500 | 성공, 잔액 500 | R2, R3 |
| TC-02 | 1,000 | 1,000 | 성공, 잔액 0 | R2, R3 |
| TC-03 | 1,000 | 1,001 | 거부, 잔액 1,000 | R2, R4 |
| TC-04 | 1,000 | 0 | 거부, 잔액 1,000 | R1, R4 |
| TC-05 | 1,000 | -100 | 거부, 잔액 1,000 | R1, R4 |

- 마지막 열처럼 **어떤 요구사항을 검증하는지** 적어 두면, 빠진 요구사항이 없는지 확인할 수 있습니다.

**Test Suite (13쪽):** 목적에 따라 묶은 테스트 케이스 모음.
```
withdraw-success (정상 출금 스위트)
├─ TC-01 일부 금액 출금
└─ TC-02 잔액 전액 출금

withdraw-rejection (출금 거부 스위트)
├─ TC-03 잔액 초과
├─ TC-04 금액 0
└─ TC-05 음수 금액
```

### 8. 테스트 분류: 수준 vs 설계 기법 (14쪽)
헷갈리기 쉬운 두 축입니다.
- **테스트 수준**: 검증할 **범위** (단위 / 통합 / 시스템 / 인수)
- **설계 기법**: 테스트 **데이터를 고르는 방법** (동등 분할, 경계값, 커버리지 등)
- 둘은 독립적이라서, 예를 들어 단위 테스트에서도 동등 분할·경계값을 쓸 수 있습니다.

### 9. 테스트 수준 4단계 (15~17쪽)

| 수준 | 무엇을 | 어떤 설계 단계에서 나오나 | 질문 | 은행 예시 |
|---|---|---|---|---|
| **단위** | 함수·클래스 같은 작은 단위 | 모듈 상세 설계 | 한 함수의 정상·예외 동작이 맞나? | `withdraw(500)` 이 잔액을 정확히 바꾸나? |
| **통합** | 모듈 사이 호출·데이터 교환 | 아키텍처·인터페이스 설계 | 모듈 사이 데이터·호출 약속이 맞나? | 계좌 서비스가 저장소에 바뀐 잔액을 제대로 기록하나? |
| **시스템** | 전체 시스템의 요구사항 | 시스템 요구사항 | 전체 시스템이 요구 기능을 제공하나? | 로그인 → 계좌 선택 → 출금 전체 흐름이 되나? |
| **인수** | 사용자·발주자의 수용 기준 | 사용자 요구사항 | 업무 시나리오와 수용 기준을 충족하나? | 고객의 출금 요구를 서비스 정책에 맞게 충족하나? |

- ⭐ 테스트를 **설계하는 시점**과 **실행하는 시점**은 다릅니다. 예를 들어 인수 테스트는 요구사항을 정할 때 설계하지만, 실행은 맨 마지막에 합니다. (V 모델이라고 부르는 구조)

---

## Part 2. 블랙박스 테스트 (18~26쪽)

**블랙박스 테스트** = 코드 내부를 보지 않고, **밖에서 보이는 입력과 출력**만으로 테스트. 요구사항을 기준으로 정상·비정상 입력을 고릅니다.

| 장점 | 단점 |
|---|---|
| 프로그래밍 지식이 없어도 가능 | 가능한 조건을 놓칠 수 있음 |
| 크고 복잡한 시스템에 효과적 | 큰 시스템은 경우의 수가 너무 많아 다 못 할 수 있음 |
| 초기 단계에서 요구사항과의 불일치 발견 | |

### 1. 동등 분할 (Equivalence Partitioning) (19~20쪽)

**아이디어:** 시스템이 **똑같이 처리할 것으로 예상되는 입력끼리 묶고(동등 클래스)**, 각 묶음에서 **대표값 하나만** 테스트한다.

**예제:** 회원가입 나이는 **18~60세, 정수만** 허용.

| 분할 | 대표 입력 | 기대 결과 |
|---|---|---|
| 17세 이하 (Invalid) | 15 | 거부 |
| 18~60세 (Valid) | 30 | 허용 |
| 61세 이상 (Invalid) | 70 (교재 그림은 65) | 거부 |
| 자료형 오류 | 문자열 `"20"` | 형식 오류 |

- 1~100세를 다 넣어볼 필요 없이 **4개로 줄어듭니다.**
- 문자열, 소수, 빈 값 같은 **잘못된 타입**도 별도 클래스로 생각할 수 있습니다.

### 2. 경계값 분석 (Boundary Value Analysis) (21쪽)

**아이디어:** 버그는 **경계 근처**에 몰려 있다 (`<` 를 `<=` 로 잘못 쓰는 실수 등). 그래서 경계 **바로 앞 · 경계 · 바로 뒤**를 테스트한다.

**예제:** 18세 이상 60세 이하 가입 가능.

| 최솟값 주변 | 기대 | 최댓값 주변 | 기대 |
|---|---|---|---|
| 17 | 거부 | 59 | 허용 |
| 18 | 허용 | 60 | 허용 |
| 19 | 허용 | 61 | 거부 |

- 동등 분할의 대표값(15, 30, 70)만으로는 `age > 18` 같은 **비교 연산자 실수**를 못 잡지만, 경계값 18을 넣으면 바로 잡힙니다.
- 💡 시험 팁: 동등 분할과 경계값은 보통 **함께** 씁니다.

### 3. 원인-결과 그래프 (Cause-Effect Graph) (22~23쪽)

**아이디어:** 규칙을 **논리식(AND, OR, NOT)** 으로 바꾼다. 원인 = 입력 조건, 결과 = 시스템 반응.

**예제 1 (22쪽):** 이체 성공 조건
```
C1: 잔액 충분   C2: 계좌 활성   C3: 이체 한도 이하
성공 = C1 AND C2 AND C3
실패 = NOT 성공
```
- 슬라이드 질문: **참/거짓 조건 3개의 가능한 조합은?** → 2 × 2 × 2 = **8개**.

**예제 2 (23쪽):** 은행 거래 처리
- 원인: C1 명령어가 입금, C2 명령어가 출금, C3 계정 번호 정상, C4 거래 금액 정상
- 결과: E1 '명령어 오류' 출력, E2 '계정 번호 오류' 출력, E3 '출금액 오류' 출력, E4 출금 수행, E5 입금 수행

### 4. 결정 테이블 (Decision Table) (24쪽)

**아이디어:** 원인-결과 그래프를 **표로** 정리해서, 결과마다 필요한 조건 조합을 나열한다. 표의 각 열이 곧 테스트 케이스 하나입니다.

표기: `1` = 참, `0` = 거짓, `x` = 상관없음(don't care)

| No. | 1 | 2 | 3 | 4 | 5 |
|---|:-:|:-:|:-:|:-:|:-:|
| C1 입금 | 0 | 1 | x | x | 1 |
| C2 출금 | 0 | x | 1 | 1 | x |
| C3 계정 정상 | x | 0 | 1 | 1 | 1 |
| C4 금액 정상 | x | x | 0 | 1 | 1 |
| **결과** | E1 명령어 오류 | E2 계정 오류 | E3 출금액 오류 | E4 출금 | E5 입금 |

**표 읽는 법:**
- 열 1: 입금도 출금도 아님 → 계정·금액은 볼 필요 없이(x) **명령어 오류**
- 열 2: 입금인데 계정이 틀림 → **계정 번호 오류**
- 열 3: 출금, 계정 정상인데 금액이 틀림 → **출금액 오류**
- 열 4: 출금, 계정·금액 모두 정상 → **출금 수행**
- 열 5: 입금, 계정·금액 정상 → **입금 수행**

💡 원래 4개 조건이면 2⁴ = 16가지지만, `x`(상관없음) 덕분에 **5개 케이스**로 줄었습니다.

### 5. 조합 테스팅 / Pairwise (25~26쪽)

- **요인(Factor)**: 바뀔 수 있는 조건 (브라우저, 인증 방식 등)
- **수준(Level)**: 각 요인이 가질 수 있는 값 (Chrome / Firefox 등)
- **Pairwise(2-way)**: **모든 두 요인의 값 쌍**이 최소 한 번씩 나오도록 테스트를 고르는 방법.

**예제:** 브라우저(Chrome/Firefox) × 인증(로그인/비로그인) × 테마(밝게/어둡게) → 전부 하면 2×2×2 = **8개**, Pairwise로는 **4개**.

| 케이스 | 브라우저 | 인증 | 테마 |
|---|---|---|---|
| P1 | Chrome | 로그인 | 밝게 |
| P2 | Chrome | 비로그인 | 어둡게 |
| P3 | Firefox | 로그인 | 어둡게 |
| P4 | Firefox | 비로그인 | 밝게 |

- 확인해 보기: 브라우저×인증 4쌍, 브라우저×테마 4쌍, 인증×테마 4쌍이 모두 한 번씩 나옵니다.
- ⚠ 한계: **세 요인이 동시에** 얽혀서 생기는 결함(예: Firefox + 비로그인 + 어둡게에서만 생기는 버그)은 2-way로 못 잡을 수 있습니다.
- 이 방법은 **어떤 조합을 테스트할지**만 정해 줍니다. 각 조합의 기대 결과는 기능 명세에서 따로 정해야 합니다.

---

## Part 3. 화이트박스 테스트 (27~30쪽)

**화이트박스 테스트** = 코드 **내부 구조**를 보고 체계적으로 점검하는 테스트 (구조적 테스트).

**과정:**
1. 소스 코드를 읽고 구조를 이해한다 (**논리 흐름도** 그리기)
2. 검증 기준(**커버리지**)을 정한다
3. 각 경로를 실행시키는 테스트 데이터를 준비한다

**검증 대상 (28쪽):** 실행 문장, 분기 조건의 참/거짓, 실행 경로, 반복문·예외 처리
- ⚠ 화이트박스는 "코드가 무엇을 했는가"는 잘 보지만, **코드에 아예 없는(빠진) 요구사항은 찾지 못합니다.** 그래서 블랙박스와 함께 씁니다.

### 커버리지 (Coverage) (29~30쪽)

커버리지 = 테스트가 코드를 **얼마나 실행해 봤는지**의 기준.

| 기준 | 검증 목표 | 대표적인 한계 |
|---|---|---|
| **문장 커버리지** | 모든 문장이 한 번 이상 실행됐나? | 거짓 분기를 충분히 시험하지 않을 수 있음 |
| **분기 커버리지** | 각 조건의 참/거짓 결과를 모두 시험했나? | 복합 조건(`A and B`)의 모든 조합까지는 보장 안 함 |
| **경로 커버리지** | 가능한 모든 실행 흐름을 시험했나? | 반복문 등으로 경로 수가 폭증함 |

⭐ **100% 커버리지 ≠ 결함 없음.**

**예제:**
```
if (amount <= 0) reject();
else if (amount > balance) reject();
else withdraw();
```
| 잔액 | 출금액 | 실행되는 분기 |
|---|---|---|
| 1,000 | 0 | 첫 번째 조건 참 → reject |
| 1,000 | 1,001 | 두 번째 조건 참 → reject |
| 1,000 | 500 | 정상 처리 → withdraw |

- 이 세 입력으로 주요 분기를 다 실행할 수 있습니다. 하지만 경계 근처의 모든 오류(예: 1,000원 전액 출금)나 **누락된 요구사항**까지 보장하지는 않습니다.

💡 파이썬에서는 `pytest` 와 `coverage` 도구로 커버리지를 자동 측정할 수 있고, 3차시에서 나온 Ruleset의 "coverage" 조건이 이 수치를 merge 조건으로 쓰는 것입니다.

---

## Part 4. 상태 기반 테스팅 (31~33쪽)

**배경:**
- 지금까지의 기법은 주로 **같은 입력엔 항상 같은 결과**를 내는 시스템(state-less: 배치 처리, 계산 위주, 하드웨어 회로)에 맞습니다.
- 하지만 많은 시스템은 **현재 상태에 따라** 같은 입력에도 반응이 다릅니다. 예: **동결된 계좌**와 **활성 계좌**에서 출금 요청의 결과가 다름.

**상태 모델의 4요소:**

| 요소 | 뜻 | 계좌 예 |
|---|---|---|
| 상태 (State) | 과거 입력의 영향이 남은 현재 모습 | 활성, 동결, 폐쇄 |
| 트랜지션 (Transition) | 한 상태에서 다른 상태로의 변화 | 활성 → 동결 |
| 이벤트 (Event) | 시스템에 들어오는 입력 | "동결" 요청 |
| 액션 (Action) | 이벤트에 대한 출력 | "계좌가 동결되었습니다" 안내 |

**검증 기준 (33쪽):**
- **모든 트랜지션**: 모든 화살표를 최소 한 번씩
- **모든 트랜지션 쌍**: 들어오는 화살표와 나가는 화살표의 쌍을 모두
- **트랜지션 트리**: 시작 상태에서 다른 모든 상태까지 가는 단순 경로 집합

**예제 (표 10.5, 은행 계좌):** 상태 번호(1~5)는 교재의 계좌 상태 다이어그램 번호입니다. 슬라이드에는 그 그림이 없으니, 이벤트 이름(동결, 동결 해지, 5년 미사용, 폐쇄)을 보고 3 = 동결, 4 = 휴면, 5 = 폐쇄 정도로 짐작할 수 있고 정확한 의미는 교재 그림으로 확인하세요.

| No. | 트랜지션 | 테스트 케이스(이벤트) |
|---|---|---|
| 1 | start → 1 | 입금 |
| 2 | 1 → 1 | 출금 |
| 3 | 1 → 1 | 입금 |
| 4 | 1 → 2 | 입금(잔고 > 0) |
| 5 | 2 → 2 | 입금 |
| 6 | 2 → 1 | 출금(잔고 < 0) |
| 7 | 1 → 3 | 동결 |
| 8 | 3 → 1 | 동결 해지 |
| 9 | 1 → 4 | (현재 − 마지막 사용일) > 5년 |
| 10 | 1 → 5 | 폐쇄(잔고 = 0) |
| 11 | 4 → 5 | 폐쇄 |

- 이 11개 케이스로 모든 트랜지션을 한 번씩 지나가므로 **"모든 트랜지션" 기준**을 만족합니다.

---

## Part 5. 통합 테스트 (34~39쪽)

**통합 테스트** = 따로 만든 모듈들을 **연결했을 때 인터페이스(호출·데이터 주고받기)가 맞는지** 테스트. 여러 팀이 만든 모듈을 합칠 때 특히 중요합니다.

### 용어: 테스트 더블 (34쪽)
아직 없는 모듈을 대신하는 가짜 코드들입니다.

| 용어 | 역할 | 비유 |
|---|---|---|
| **드라이버 (Driver)** | 시험 대상 모듈을 **호출하는** 임시 프로그램 (상위 대신) | 운전자 대역 |
| **스텁 (Stub)** | 시험 대상 모듈이 **호출하는** 임시 모듈 (하위 대신, 정해진 값만 돌려줌) | 마네킹 |
| **목 (Mock)** | 호출 횟수·전달된 인자 등 **상호작용 자체를 검증**하도록 만든 테스트 더블 | 감시 카메라 달린 마네킹 |

### 통합 전략 4가지 (35~39쪽)

| 방식 | 접근 | 특징 |
|---|---|---|
| **빅뱅** | 모든 모듈을 한 번에 결합 | 문제 생기면 원인 찾기 어려움 |
| **하향식** | 상위 모듈부터 결합 | 아직 없는 하위는 **스텁**으로 대체 |
| **상향식** | 하위 모듈부터 결합 | 아직 없는 상위는 **드라이버**로 대체 |
| **연쇄식 (기능 흐름 중심)** | 사용자 기능 하나의 수직 흐름부터 결합 | 완성된 기능 단위로 일찍 검증 가능 |

**각 방식의 장단점:**

| 방식 | 장점 | 단점 |
|---|---|---|
| 빅뱅 (36쪽) | 일정 관리가 편함, 통합용 스텁이 필요 없음 | 오류 위치·원인 찾기 어려움, 단위 테스트에 많은 시간, 준비할 드라이버/스텁이 많음, 진도 예측 어려움 |
| 하향식 (37쪽) | 중요한 상위 인터페이스를 일찍 테스트, 스텁으로 시스템 모습을 일찍 보여줌, 개발자 입장에서 쉬움 | 입출력 모듈이 하위에 있어 늦게 붙음, 테스트 케이스 작성·실행이 어려움, 중요 기능이 마지막에 구현됨 |
| 상향식 (38쪽) | 점진적이라 오류 발견이 쉬움, 하위 모듈을 더 많이 테스트 | 초기에 시스템 뼈대가 없음, 중요한 상위 인터페이스를 마지막에야 확인, 의뢰자가 일찍 시험해 볼 기회가 적음 |
| 연쇄식 (39쪽) | 초기에 골격이 생김, 사용자 의견을 빨리 확인, 나눠서 개발하기 쉬움 | 모듈 간 상호작용 검증 부족, 테스트 환경 구성이 복잡, 전체 검증이 늦어짐 |

💡 외우는 요령: **하향식 ↔ 스텁, 상향식 ↔ 드라이버.** "위에서 내려오니 아래가 비어 있어서 스텁", "아래에서 올라가니 위가 비어 있어서 드라이버".

---

## Part 6. 시스템 테스트와 인수 테스트 (40~47쪽)

모든 컴포넌트를 통합한 뒤 수행합니다.

| 종류 | 무엇을 |
|---|---|
| 기능 테스트 | 기능 요구사항을 시스템 수준에서 |
| 성능 테스트 | 비기능 요구사항 중 성능 |
| 보안 테스트 | 보안 취약점 찾기 |
| 사용성(UI) 테스트 | 화면 요소, 상호작용, 오류 메시지 등의 결함 |
| 인수 테스트 | 의뢰자가 계약서에 적힌 기준대로 |
| 설치 테스트 | 실제 사용할 환경에서 사용성·기능·성능 |

### 1. 기능 테스트 (41~42쪽)
- 기능 요구사항과 실제 시스템의 차이를 찾는 테스트. 사용자와 관련 있고 오류가 날 가능성이 큰 것을 고릅니다.
- **유스케이스**를 보고 오류를 일으킬 만한 경우를 찾아 테스트 케이스로 만듭니다. 일반적인 경우와 예외적인 경우를 모두.

**예제 (티켓 판매기):**
- 유스케이스 "티켓 구입": 시작 조건(승객이 판매기 앞, 충분한 돈 있음) → 사건 흐름(구간 선택 → 금액 표시 → 돈 투입 → 거스름돈과 표 발행) → 종료 조건(승객이 표를 받음). 예외 흐름으로 "돈을 넣기 전에 구간을 바꾸면 넣은 돈을 돌려준다", "초과 금액은 돌려준다"가 있습니다.
- 이것을 **구체적인 값이 들어간 테스트 케이스**로 바꿉니다. 예: 승객이 1000원을 가지고 구간 2, 3, 1, 2를 차례로 누름 → 800, 1000, 600, 800원 표시 확인 → 1000원 넣고 2구간 표와 거스름돈 200원(100원 2개) 받는지 확인 등.
- ⭐ 핵심: 유스케이스(일반적인 서술) → 테스트 케이스(구체적인 입력값과 기대 결과).

### 2. 성능 테스트 (43~44쪽)

| 측정 항목 | 뜻 |
|---|---|
| 작업부하 (workload) | 시스템이 처리·생성하는 작업의 양 |
| 처리량 (throughput) | 단위 시간당 처리한 트랜잭션 수 (예: 시간당 메일 수) |
| 반응 시간 (response time) | 요청 하나를 처리하는 데 걸린 총 시간 |
| 효율성 | 작업 처리에 쓴 CPU 시간·메모리 같은 자원의 비율 |

- **스트레스 테스트**: 처리 능력의 **몇 배** 부하를 견디는지 측정
- **시뮬레이션**: 사용자 모델을 만들고, 트랜잭션 종류별 프로토타입을 만든 뒤, 난수로 실제 사용 비율에 맞는 부하를 생성

### 3. 보안 테스트 (45쪽)
의도하지 않은 기능·동작(**취약점**)을 찾는 테스트.
- **정적/동적 분석**: 도구가 코드를 분석해 취약한 패턴을 찾음 (3차시의 Code scanning이 이것)
- **침입 테스트**: 공격 시나리오를 테스트 케이스로 만들어 실제로 실행
- **랜덤 테스트**: 무작위 입력값
- **입력 퍼징(fuzzing)**: 이상한 입력을 대량으로 넣어 보기 (유전자 알고리즘 기반 포함)

### 4. UI 테스트 (46쪽)
기능·성능·보안과 달리 **인간 공학적인 목적**(쓰기 편한가)을 봅니다. 찾는 결함:
- 보고 느끼는 UI 결함: 일관성 없음, 빠짐, 부정확, 복잡, 엉성한 화면 구성
- 입력·출력 데이터 결함: 올바른 데이터 타입·형식을 쓰는지
- 사용자-시스템 상호작용 결함: 설계대로 동작하는지
- 오류 처리 결함: 오류를 처리 안 함, 부정확, 부적절
- 문서·도움말 결함

### 5. 인수 테스트 (47쪽)
- **목적:** 시스템을 **바로 사용할 준비가 다 되었는지** 확인
- **방법:** 개발자가 아닌 **의뢰자(또는 대리인)** 가, 요구 분석서를 기반으로, 실제 업무 절차대로 수행
- **유형:**

| | 누가 | 어디서 |
|---|---|---|
| **알파 테스트** | 선택된 사용자 | **개발 환경**에서 (개발자 옆에서) |
| **베타 테스트** | 선택된 사용자 | **실제 외부 환경**에서 (필드 테스트) |

- 정해진 방식의 테스트로 못 찾은 오류를 실제 사용자가 발견할 수 있다는 게 장점입니다.
- 💡 게임의 "오픈 베타"가 바로 베타 테스트입니다.

---

## 10장 스스로 점검 질문 (슬라이드에 없는 연습용)

| 질문 | 답 |
|---|---|
| 오류, 결함, 장애의 차이는? | 오류 = 사람의 실수, 결함 = 코드·문서에 남은 문제, 장애 = 실행 중 보이는 잘못된 동작 |
| 결함이 있는데 장애가 안 나타날 수 있나? | 있다. 그 결함이 있는 조건이 실행되지 않으면 안 보임 |
| 검증과 확인의 차이는? | 검증 = 명세대로 만들었나, 확인 = 사용자가 원하는 걸 만들었나 |
| 나이 18~60 허용일 때 경계값 테스트 입력은? | 17, 18, 19, 59, 60, 61 |
| 참/거짓 조건 3개의 조합 수는? | 2³ = 8 |
| 결정 테이블의 x는? | don't care (그 조건은 결과에 영향 없음) |
| Pairwise의 한계는? | 3개 이상 요인이 동시에 얽힌 결함은 놓칠 수 있음 |
| 커버리지 100%면 결함이 없나? | 아니다. 빠진 요구사항이나 경계 오류는 못 잡을 수 있음 |
| 하향식 통합에서 쓰는 임시 모듈은? | 스텁 (상향식은 드라이버) |
| 알파 테스트와 베타 테스트의 차이는? | 알파 = 개발 환경에서, 베타 = 실제 사용자 환경에서 |

---

# GitHub Actions (워크플로 자동화)

> 원본 자료: `github_action.pdf` (25쪽)
>
> **한 줄 요약:** GitHub Actions는 "언제(이벤트), 어디서(러너), 어떻게(스텝)" 할지를 YAML 파일에 적어 두면 GitHub가 알아서 빌드·테스트·배포 같은 작업을 자동으로 실행해 주는 기능입니다.
>
> **의의:** 3차시에서 이름만 나온 Actions의 실제 작성법입니다. 10장 테스팅에서 배운 테스트를 push나 PR 때마다 자동으로 돌리고, Ruleset의 "Require status checks to pass"와 묶으면 검사를 통과 못 한 코드는 merge를 막을 수 있습니다.

## 1. Actions란? (2쪽)
- GitHub가 제공하는 **범용 워크플로 엔진**. **workflow 단위로 작업(task)을 자동화**합니다.
  - PR이 작성되면 빌드와 테스트 실행
  - 릴리스 태그가 작성되면 컨테이너 이미지 배포
  - Issue가 작성되면 무작위로 멤버 할당
- Workflow에는 **언제(on), 어디서(runs-on), 어떻게(steps)** 처리할지 정의합니다.

## 2. Workflow 파일 위치 (3쪽)
- 저장소 루트 기준 `.github/workflows/*.yml` (확장자 `.yml` 또는 `.yaml`)
- 한 저장소에 워크플로 파일을 **여러 개** 둘 수 있습니다.
```bash
mkdir -p .github/workflows            # 폴더를 한 번에 (상위 폴더까지) 만들기
touch .github/workflows/hello.yml     # 빈 파일 만들기 (PowerShell에서는 VS Code로 새 파일 만들기)
```
```
.
└── .github
    └── workflows
        └── hello.yml
```

## 3. YAML 작성 시 주의 (4쪽)
- 들여쓰기는 **공백 2칸. 탭 사용 금지**
- 콜론(`:`) 뒤에는 공백, 목록은 하이픈(`-`)
- 같은 계층의 키는 같은 깊이로 정렬
- 문자열·특수문자·표현식의 따옴표 처리 주의
- ※ **YAML 문법**과 **GitHub Actions 전용 키워드**는 다릅니다.
- 💡 이 저장소의 `calculator.py` 는 탭으로 들여쓰기했지만, **YAML 파일은 절대 탭을 쓰면 안 됩니다.**

## 4. Workflow 기본 구조 (5~6쪽)
```yaml
name: Hello                       # 워크플로우명
on: push                          # 이벤트
jobs:                             # 잡 정의
  hello:                          # Job ID
    runs-on: ubuntu-latest        # Runner
    steps:                        # Steps def
      - run: echo "Hello, world"  # Shell command
      - uses: actions/checkout@v4 # action call
```
- `name`: 생략 가능하지만 생략하면 로그 분석이 어려우니 지정 권장. 프로젝트 안에서 규칙을 통일 (예: 모두 소문자, 빈칸은 `-`).

## 5. 이벤트 `on` (7~8쪽)
- `on: push` 처럼 한 개, `on: [push, pull_request]` 처럼 배열로 여러 개 지정.

| 이벤트 | 발생 조건 | 주요 활용 |
|---|---|---|
| `push` | Commit/Tag가 원격에 push될 때 | 빌드, 자동 테스트 |
| `pull_request` | PR 생성, 재개방, 새 commit 반영 | 코드 검증, CI |
| `pull_request_target` | PR 이벤트를 **기본 branch 컨텍스트**에서 처리 | PR 라벨링, 관리 자동화 |
| `workflow_dispatch` | 사용자가 **수동 실행** | 수동 테스트, 배포 |
| `schedule` | 지정한 시간 | 정기 테스트·점검 |
| `workflow_run` | 다른 워크플로 상태가 바뀔 때 | 후속 워크플로 |
| `workflow_call` | 다른 워크플로에서 호출 | 재사용 가능한 워크플로 |
| `issues` | Issue 생성·수정·종료 | 이슈 관리 자동화 |
| `issue_comment` | Issue/PR 댓글 작성·수정 | 댓글 기반 자동화 |
| `pull_request_review` | PR 리뷰 제출·수정·취소 | 리뷰 상태 확인 |
| `release` | Release 생성·게시 | 패키지 배포 |
| `create` / `delete` | branch·tag 생성 / 삭제 | 생성 처리 / 정리 작업 |
| `fork` | 저장소가 Fork될 때 | Fork 현황 기록 |
| `repository_dispatch` | 외부 시스템이 API로 전달 | 외부 서비스 연동 |

- 전체 목록: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## 6. Job과 Runner (9~10쪽)
- **Job** = 워크플로의 실행 단위. `jobs:` 아래에 쓰고, 여러 개 가능. **Job ID는 자유롭게** 짓습니다 (예시에서는 `hello`).
- Job ID 단위로 **러너(실행 환경)** 를 지정하고, 그 안의 `steps` 에 할 일을 적습니다.

| Runner | `runs-on` | 주요 용도 |
|---|---|---|
| Ubuntu | `ubuntu-latest` | Python, Java, 일반적인 CI |
| Windows | `windows-latest` | Windows 프로그램 테스트 |
| macOS | `macos-latest` | macOS 앱 테스트 |
| 특정 버전 | `ubuntu-24.04`, `windows-2022`, `macos-15` | 실행 환경 버전 고정 |

## 7. Step (11~16쪽)
- **Step** = 워크플로의 **최소 처리 단위**. `steps:` 아래에 여러 개, **위에서 아래 순서대로** 실행.
- 스텝이 하는 일은 두 가지: **셸 명령(`run`)** 또는 **액션(`uses`)**.

**셸 명령 (ubuntu 러너 기준, 13쪽)**

| 명령어 | 기능 | 예시 |
|---|---|---|
| `echo` | 문자열 출력 | `echo "Hello GitHub"` |
| `pwd` | 현재 디렉터리 | `pwd` |
| `ls` | 파일 목록 | `ls -la` |
| `cd` | 디렉터리 이동 | `cd src` |
| `mkdir` | 디렉터리 생성 | `mkdir build` |
| `cat` | 파일 내용 출력 | `cat README.md` |
| `cp` / `mv` / `rm` | 복사 / 이동·이름 변경 / 삭제 | `cp a.txt b.txt` |
| `which` | 실행 파일 경로 | `which python` |

```yaml
steps:
  - name: Check environment      # 스텝에도 name 지정 가능
    run: |                       # | : 여러 줄 셸 명령을 쓸 때
      echo "Current directory:"
      pwd
      ls -la
```
- 셸 명령이므로 **조건문(`if`), 반복문(`for`), 환경변수 사용**도 가능 (15쪽).
```yaml
  - name: Check file
    run: |
      if [ -f "README.md" ]; then
        echo "File exists"
      else
        echo "File not found"
      fi
  - name: Repeat commands
    run: |
      for i in 1 2 3
      do
        echo "Test $i"
      done
  - name: Use environment variable
    env:
      MESSAGE: Hello
    run: echo "$MESSAGE"
```
**액션 `uses` (16쪽)**
- **Action = 재사용 가능한 구성 요소.** 남이 만든 것도 쓸 수 있습니다. 예: `actions/checkout@v4` (저장소 코드를 러너로 내려받기).
- GitHub Marketplace(https://github.com/marketplace)에 많이 공개되어 있습니다.
- 💡 러너는 매번 **빈 컴퓨터**에서 시작해서, 내 코드가 필요하면 `checkout` 이 먼저 있어야 합니다.

## 8. 오류의 종류 (17쪽)
| 종류 | 설명 |
|---|---|
| **Syntax Error** | 러너가 코드를 해석하지 못할 때. Workflow 문법 오류, YAML 문법 오류 (YAML에는 있지만 Actions에서 못 쓰는 구문, 예: anchor, alias) |
| **Run-time Error** | 실행 중 오류. **종료 상태(Termination status)** 가 0이면 성공, 그 외 값이면 실패 |

- ⚠ **의도한 결과가 아니어도 0이 반환되면 "정상 종료"로 인식**됩니다. 그래서 테스트는 실패할 때 0이 아닌 값으로 끝나도록 작성해야 합니다.

## 9. Context (18~20쪽)
- **Context** = 실행 정보나 job 결과 등을 담은 객체. 값은 `${{ github.actor }}` 처럼 꺼냅니다.

**github context**

| 속성 | 개요 |
|---|---|
| `github.run_id` | 워크플로 실행 ID |
| `github.head_ref` | PR의 source branch |
| `github.workspace` | 스텝의 작업 디렉터리 |
| `github.repository` | Repo 이름 |
| `github.repository_owner` | Repo 소유자 |
| `github.event` | 출발점이 된 이벤트(객체) |
| `github.actor` | 실행을 일으킨 사용자 |

**runner context:** `runner.name`(이름), `runner.os`(OS), `runner.arch`(CPU 구조), `runner.temp`(임시 폴더), `runner.tool_cache`(설치된 도구 폴더), `runner.debug`(디버그 로그)

## 10. 환경 변수 `env` (21~23쪽)
- `env` 키로 정의. **워크플로 / 잡 / 스텝 중 어디에 쓰느냐에 따라 유효 범위**가 달라집니다.
- 값은 문자열이나 context 모두 가능. 참조는 셸에서 `$이름`, 셸이 아닌 곳에서는 `${{ env.이름 }}`.
- 기본 환경 변수가 자동 제공됩니다: `CI`, `GITHUB_ACTOR`, `GITHUB_REPOSITORY`, `GITHUB_SHA`, `GITHUB_WORKSPACE`, `RUNNER_OS` 등.
- **중간 환경 변수(intermediate environment variable):** context 값을 `run:` 안에 `${{ }}` 로 **직접 넣으면 여러 문제**가 생길 수 있어서, 먼저 `env` 에 담고 셸에서 `$변수`로 쓰는 방식이 안전합니다.
```yaml
env:
  ACTOR: ${{ github.actor }}     # context → 환경 변수에 담고
steps:
  - run: echo "$ACTOR"           # 셸에서는 변수로 사용
```
- 💡 보충: PR 제목처럼 **사용자가 입력한 값**을 `${{ }}` 로 `run` 에 직접 넣으면 악의적인 문자열이 명령으로 실행될 위험이 있습니다. 이 때문에 중간 환경 변수를 권장합니다.

## 11. Variables와 Secrets (24~26쪽)
| | 환경 변수 `env` | 변수 Variables | 비밀 Secrets |
|---|---|---|---|
| 범위 | 단일 워크플로 안 | **여러 워크플로에서 공유** | 여러 워크플로에서 공유 |
| 등록 | 워크플로 파일에 직접 | Settings > Secrets and variables > Actions > **Variables** > New repository variable | 같은 위치의 **Secrets** 탭 |
| 참조 | `${{ env.NAME }}` / `$NAME` | `${{ vars.NAME }}` | `${{ secrets.NAME }}` |
| 특징 | 파일에 평문으로 보임 | 평문(민감하지 않은 값용) | 암호화 저장, 로그에서 자동 마스킹, **등록 후 값 확인 불가** |

```yaml
name: Variables
on: workflow_dispatch
jobs:
  print:
    runs-on: ubuntu-latest
    env:
      USERNAME: ${{ vars.USERNAME }}
    steps:
      - run: echo "$USERNAME"
```
- Secrets는 자동 마스킹되지만 **너무 의존하지 말고**, 로그 출력은 **최대한 하지 않는 것**이 좋습니다.
- ⚠ 비밀번호·토큰은 절대 코드나 워크플로 파일에 직접 쓰지 말고 Secrets에 등록합니다.

## Actions 스스로 점검 질문 (슬라이드에 없는 연습용)
| 질문 | 답 |
|---|---|
| 워크플로 파일은 어디에 두나? | `.github/workflows/*.yml` |
| 워크플로의 세 요소 "언제/어디서/어떻게"는 각각 어떤 키? | `on` / `runs-on` / `steps` |
| `run` 과 `uses` 의 차이는? | run = 셸 명령 실행, uses = 만들어진 액션 호출 |
| YAML에서 들여쓰기에 탭을 쓰면? | 안 된다. 공백 2칸 |
| 수동으로 실행하고 싶으면 어떤 이벤트? | `workflow_dispatch` |
| 테스트가 실패했는데 워크플로가 성공으로 나오는 이유는? | 종료 코드가 0이면 정상 종료로 보기 때문 |
| 환경 변수와 변수(Variables)의 차이는? | env는 한 워크플로 안에서만, Variables는 여러 워크플로에서 공유 |
| 비밀번호는 어디에 저장? | Secrets (`${{ secrets.NAME }}`) |

## Actions 실습 기록 (2026-11-06, Claude가 적용)
슬라이드 예제를 `.github/workflows/` 에 파일로 만들어 push했습니다.

| 파일 | 이벤트 | 내용 |
|---|---|---|
| `hello.yml` | `push` | 5쪽 Hello 예제 (echo + checkout) |
| `shell-command.yml` | `workflow_dispatch` | 13~15쪽 셸 명령, 조건문, 반복문, env |
| `env-vars.yml` | `workflow_dispatch` | 21~23쪽 환경 변수, setup-python, `python calculator.py` 실행 |
| `variables.yml` | `workflow_dispatch` | 24~25쪽 Variables 참조 (`USERNAME` 변수 등록) |

확인 방법: GitHub 저장소 > **Actions** 탭에서 실행 결과를 보고, 수동 워크플로는 **Run workflow** 버튼으로 실행합니다.

---

# 부록: 명령어 치트시트

| 명령어 | 하는 일 |
|---|---|
| `git --version` | Git 설치/버전 확인 |
| `git config --global user.name "이름"` | commit 작성자 이름 설정 |
| `git config --global user.email "메일"` | commit 작성자 이메일 설정 |
| `git config --list` | 설정 전체 보기 |
| `git init` | 현재 폴더를 Git 저장소로 만들기 |
| `git status` | 현재 branch와 파일 상태 확인 |
| `git add 파일` | 변경을 Staging Area에 올리기 |
| `git commit -m "메시지"` | stage된 내용을 commit으로 저장 |
| `git log --oneline` | commit 이력 한 줄씩 보기 |
| `git log --graph --oneline --decorate --all` | 모든 branch의 commit 그래프 보기 |
| `git diff` | add 전 변경 내용 보기 |
| `git diff --staged` | add 된(commit 예정) 변경 내용 보기 |
| `git remote add origin 주소` | 원격 저장소를 origin이라는 이름으로 등록 |
| `git remote -v` | 등록된 원격 저장소 보기 |
| `git branch -M main` | 현재 branch 이름을 main으로 변경 |
| `git push -u origin main` | main을 원격에 올리고 기본 대상으로 설정 |
| `git clone 주소` | 원격 저장소를 이력까지 통째로 복제 |
| `git branch` | branch 목록 보기 |
| `git switch 브랜치` | 그 branch로 이동 |
| `git switch -c 브랜치` | 새 branch 만들고 이동 |
| `git merge 브랜치` | 현재 branch에 그 branch를 합치기 |
| `git merge --abort` | 진행 중인 merge 취소 |
| `git pull` (`--no-rebase` / `--rebase` / `--ff-only`) | 원격 변경 가져와 합치기 |
| `git restore 파일` | add 전 파일 수정 버리기 |
| `git restore --staged 파일` | add 취소 (파일 내용은 유지) |
| `git reset --soft HEAD~1` | 마지막 commit 취소 (변경은 stage에 남김) |
| `git revert 커밋ID` | 해당 commit을 취소하는 새 commit 만들기 |
| `git branch -d 브랜치` | merge된 branch 삭제 |
| `git add .` | 현재 폴더의 바뀐 파일 전부 stage |
| `git push -u origin 브랜치` | 작업 branch를 GitHub에 올리기 (PR 만들기 전 단계) |
| `git fetch origin` | GitHub의 최신 내용을 받기만 함 (합치지 않음) |
| `git merge origin/main` | GitHub의 최신 main을 현재 branch에 합치기 (PR 충돌 해결용) |

## 초보자가 자주 막히는 곳

- **`not a git repository` 오류** → Git 저장소가 아닌 폴더에 있는 것. `cd git-practice` 로 이동했는지 확인.
- **commit 할 때 이상한 편집기 화면(vim)이 열림** → `-m "메시지"` 를 빠뜨린 경우. `Esc` 누르고 `:q!` 로 나온 뒤 `-m` 을 붙여 다시 실행. merge 메시지 화면이면 `:wq` 로 저장하고 닫기.
- **`git diff` 가 아무것도 안 보임** → 이미 add 했기 때문. `git diff --staged` 로 확인.
- **push 시 비밀번호 오류** → GitHub는 계정 비밀번호로 push 불가. 브라우저 로그인이나 Personal Access Token 사용.
- **push 거부(rejected)** → GitHub 저장소를 만들 때 README를 같이 만들어 이력이 갈라진 경우가 많음. 실습 10처럼 빈 저장소로 만드는 게 안전.
- **branch를 바꿨더니 코드가 사라짐** → 정상. 그 코드는 다른 branch에 있음. `git switch` 로 돌아가면 다시 보임.
- **PR에 conflict 표시가 뜸** → 내 branch에서 `git fetch origin` 후 `git merge origin/main`, 충돌 해결 후 add, commit, push (3차시 Part VII).
- **GitHub에서 merge했는데 내 컴퓨터 main이 그대로임** → 정상. `git switch main` 후 `git pull` 로 받아와야 함.
