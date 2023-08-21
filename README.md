# Toy_Project5
Toy_Project5는 비동기 처리를 위한 Celery 토이 프로젝트입니다.
## 1. Click 사용 이유
- 프로젝트 실행 및 수행 명령어 main.py에서 모든 cli 관리 목적  
- main.py 경로에 import 기준 설정  

## 2. 프로젝트 구조  

```
src/
 ┗━ app/
     ┣━ batch/
     ┃   ┃ ┗━ celery/
     ┃   ┃      ┗━ tasks/  (수행 함수 모음)
     ┃   ┃           ┗━ calculator.py
     ┃   ┗━ cli/ (개별 cli 관리)
     ┃        ┗━ calculator.py
     ┃
     ┣━ cli.py (Nesting Commands tutorial)
     ┣━ group.py (Command and Group)
     ┣━ hello.py (Quick Start)
     ┗━ main.py (main.py에서 cli 통합관리 )
 
README
```