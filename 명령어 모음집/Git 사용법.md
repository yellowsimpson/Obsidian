
git 시뮬레이션 사이트

```
https://learngitbranching.js.org/?locale=ko
```



git bash 처음 로그인

## 초기 설정

$git config —global [user.name](http://user.name) “이름”

$git config —global [user.email](http://user.email) “메일 주소” $git config --global --list

→설정 확인

$git config ([user.name](http://user.name))

→() 안에 확인해보고 싶은 설정 넣으면되

<파일 처음 만들었을 때 같이 만들면 편한것>

$git init

→ 파일을 처음 만들었을 때 깃을 사용할 수 있게 초기화 해주는것(처음 1번만 해주면됨)

→ 이 작업을 해주면 .git이라는 파일 생성

$git remote add origin [](https://github.com/yellowsimpson/aa.git)[https://github.com/yellowsimpson/파일이름.git](https://github.com/yellowsimpson/%ED%8C%8C%EC%9D%BC%EC%9D%B4%EB%A6%84.git)

→만들어진 파일에 원격 저장소를 연결해주는 작업

echo "# 파일이름" >> [README.md](http://readme.md/)

git add [README.md](http://readme.md/) git commit -m "first commit" git branch -M main git push -u origin main

파일 github에 넣을 때

git remote add origin [https://github.com/yellowsimpson/aa.git](https://github.com/yellowsimpson/aa.git) git branch -M main git push -u origin main

## 프로젝트 생성

처음 repoistory를 만들때 같이 만들어야하는 파일

1. [README.md](http://README.md)
2. .gitignore → 추적 무시
3. requirements.txt. →종속성 파일 list 사용(다운로드 하는 파일 설정해두는 파일)

- **파일 넣는 방법**
    
    내컴퓨터에서 깃에 파일 올리는 방법 아무것도 없는 상태에서
    
    add → commit → push
    
    $git init
    
    →현재 디렉토리에서 내가 git을 사용할 수 있게 초기화시켜주는 명령어
    
    (초기에 1번만 하면되)
    
    #git 원격 저장소 설정 $git remote add origin <원격 저장소 URL>
    
    →원격으로 조작하고
    
    $git clone <원격 저장소 URL>
    
    → 파일 올릴려면 먼저 git에 있는 정보를 받아와야되
    
    젤 처음에만 사용
    
    $git checkout -b 브랜치 이름
    
    → git에서 받아오고 싶은 branch를 내 컴퓨터에 만들어야되
    
    (이름 github에 있는 branch와 같아야됨)
    
    $git pull origin 브랜치 이름
    
    →그럼 git에 있는 파일이 내 컴퓨터에 받아져
    
    $git add .
    
    $git add 추가하고 싶은 파일이름
    
    →git에 내 파일을 추가명령어
    
    $git commit -m “메모 내용”
    
    $git push origin simpson
    
    $git remote -v
    
    → 지금 터미널이 어디를 바라보고 있는지 확인하는 명령어
    

$echo ‘My Project’ > README

→ a new file created

- Viewing commit history(%git log)
    
    $git log
    
    → 지금까지 commit 했던 내용 확인 할 수 있어
    
    $git log -stat
    
    → 변경된 내용이 몇개 있는지, 변경 내용이 뭔지 까지 확인
    
    $git log —pretty=fromat: “%h - %an, %ar : %s”
    
    → 상황에 따라 필요한 명령어를 붙이면되
    
    - **`%h`**: 커밋 해시의 짧은 형식 (짧은 SHA-1 해시 값).
    - **`%an`**: 커밋 작성자의 이름 (author name).
    - **`%ar`**: 커밋이 작성된 시점으로부터의 상대적 시간 (예: "2 days ago").
    - **`%s`**: 커밋 메시지 (commit message).
    
    $git log -p -2
    
    → 상황에 따라 비교해보고 싶은 commit이 있다면 숫자 바꿔주면되
    
    - **`p`**: 각 커밋의 변경 사항을 보여줍니다. 이 옵션을 사용하면 커밋마다 어떤 파일이 어떻게 변경되었는지에 대한 diff(차이)를 출력합니다.
    - **`2`**: 최근 두 개의 커밋만 출력합니다. 숫자를 변경하면 출력되는 커밋의 수를 조정할 수 있습니다.

$git branch -M “브랜치 이름”

→main 에서 branch에 저장

$git clone -b <branch_name> <repository_url>

→ 특정 브랜치에 있는 파일들 받아올 때

$git status

→현재 상태 확인

$git init

→현재 디렉터리에서 깃을 사용할 수 있게 초기화


$git branch

→지금 어느 branch를 보고 있는지 확인하는 명령어

$git fetch

→원격 저장소에 있는 정보를 최신화하는 명령어

$git branch -M “”

$git pull orgin 브랜치이름

$git commit -amend

→ 젤 마지막 commit 덮어쓰기

$git reset HEAD <file>

→ un

$git checkout —<file>

→파일의 변경 사항을 마지막 커밋 상태로 되돌리기 위해 사용

$git status
→ 현재 상태 알려줘
