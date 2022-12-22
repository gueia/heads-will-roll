# Heads Will Roll: 디시인사이드 말머리 이동 자동화 프로그램
Heads Will Roll은 디시인사이드 말머리 이동을 자동화해주는 프로그램입니다. 현재 포스트락 마이너 갤러리에서만 작동합니다.

## 주의 사항
> __Warning__

## 설치
```
~$ git clone https://github.com/gueia/heads-will-roll.git
~$ cd heads-will-roll
~/heads-will-roll$ pip install -r requirements.txt
```

## 사용 방법
```
~/heads-will-roll$ ./main.py
```

## 프로젝트 역사
#### v0.0.1 (2022-12-21)
* 프로젝트 시작
#### v0.0.2 (2022-12-22)
* 말머리 목록 자동으로 가져오는 기능 추가
* 처리 속도 개선
* 예외 처리 개선
* 로그 저장 기능 추가

#### 수정&개발 예정 목록
* CLI 환경 구현
* 말머리 id 직접입력 (삭제된 말머리 복구에 필요)
* <s>multiprocessing 병렬 처리</s> (무기한 연기)
