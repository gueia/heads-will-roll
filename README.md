# Heads Will Roll: 디시인사이드 말머리 이동 자동화 프로그램
![greetings](https://github.com/github/docs/actions/workflows/greetings.yml/badge.svg)

Heads Will Roll은 디시인사이드 말머리 이동을 자동적으로 수행하는 프로그램입니다.

## 시작하기
### 설치
> __Note__
> 
> 운영체제가 macOS 또는 Linux인 경우 pip 대신 pip3를 실행하세요.

```
~$ git clone https://github.com/gueia/heads-will-roll.git
~$ cd heads-will-roll
~/heads-will-roll$ pip install -r requirements.txt
```

터미널에 상단의 명령어를 순서대로 입력합니다.

### 업데이트
```
~/heads-will-roll$ git pull origin main 
```

## 사용 방법
> __Warning__
> 
> 사용한 계정에서 간혹 영원히 PC 환경에서 직접 로그인할 수 없는 오류(ERR_300016)가 발생하므로, 반드시 부계정으로 로그인하길 바랍니다.
> 
> 이 오류는 계정에 귀속되는 것으로 보아 일종의 차단에 해당하는 것으로 추측됩니다.
> 
> 계정에서 이미 ERR_300016가 발생하는 경우에는 모바일 환경(m.dcinside.com)에서 로그인한 뒤 PC 버전으로 전환하는 방법으로 우회해서 로그인 가능합니다.

> __Note__
> 
> 운영체제가 macOS 또는 Linux인 경우 python 대신 python3를 실행하세요.
***
### 말머리 이동
```
~/heads-will-roll$ python main.py -m
```

처음 실행하는 경우 ChromeDriver를 설치하는 과정이 필요하기 때문에 시간이 소요될 수 있습니다.

main.py 실행 후 마이너 갤러리 아이디를 입력하고 말머리를 목록에서 선택한 뒤 로그인하면 됩니다.

작업을 중단하고 싶은 경우 <kbd>Ctrl</kbd>+<kbd>C</kbd>를 입력하세요.

> 입력 예시
```
GALLERYID: postrockgallery
다음 중 현재 이동할 글이 존재하는 말머리의 번호를 선택하세요.
(0, '전체')
(1, '💬')
(2, '🔔소식')
(3, '💡정보')
(4, '💿인증')
(5, '🎵음추')
(6, '🌐번역')
(7, '📖후기')
(8, '🍀탑스터')
(9, '🎸자작')
(10, '📢공지')
입력: 6
다음 중 글을 이동할 목표 말머리의 번호를 선택하세요.
(0, '전체')
(1, '💬')
(2, '🔔소식')
(3, '💡정보')
(4, '💿인증')
(5, '🎵음추')
(6, '🌐번역')
(7, '📖후기')
(8, '🍀탑스터')
(9, '🎸자작')
(10, '📢공지')
입력: 6
USERID: gueia
PASSWORD: 
```
***
### 포스트락 마이너 갤러리 말머리 복구
```
~/heads-will-roll$ python main.py -r
```

포스트락 마이너 갤러리 말머리 복구 기능을 실행하려면 파라미터 값에 -r을 입력하세요.

> 입력 예시
```
다음 중 복구할 말머리의 번호를 선택하세요.
(0, 'NaN')
(1, 'NaN')
(2, '소식')
(3, 'NaN')
(4, '인증')
(5, '음추')
(6, '번역')
(7, '후기')
(8, '탑스터')
(9, '자작')
(10, 'NaN')
입력: 6
USERID: gueia
PASSWORD: 
```

## 수정&개발 예정 목록
* [ ] CLI 환경 구현
* [ ] 말머리 id 직접입력 (삭제된 말머리 복구에 필요)
* [ ] 예외 처리 개선
  * [ ] 로그인 실패 시 재시도
  * [ ] 입력란 공백 무시하기
* [ ] 속도 향상
  * [ ] 로그인 정보 입력을 로그인 페이지에서 기다리기
* [ ] <s>multiprocessing 병렬 처리</s> (무기한 연기)
### 버그
* [ ] 입력 과정에서 나타나는 UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 0-1: invalid continuation byte

