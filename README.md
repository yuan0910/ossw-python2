# 강의 관리 프로그램

+ 클래스 Lecture로 한 강의의 설정 및 성적을 관리할 수 있습니다.
+ 이용자의 요구에 따라 내부적으로 다른 함수를 호출하는 manageLecture() 함수 하나로 강의를 관리할 수 있습니다.

---


> 클래스 변수


| 변수 | 설명 | 예시 | default | 
| --- | --- | --- | --- |
| name | 강의명 | 자료구조, 수치해석 | 설정되지 않음 |
| category | 강의 구분 | 자유선택, 전공 | 설정되지 않음 |
| size | 강의 수강 인원 | 24, 50 | -1 |

각각의 변수는 private 변수로 설정되어 클래스 외부에서 접근할 수 없으며, 클래스 내의 manageLecture() 함수를 통해서 참조 및 변경이 가능합니다.  
Lecture 클래스에서는 오직 manageLecture() 함수를 통해서만 강의를 관리합니다. 

---
> ManageLecture() 기능

| 옵션 | 기능 | 설명 | 
| --- | --- | --- |
| 0 | 과목 설정 (name, category, size)를 출력 | 클래스 내부의 showInfo() 함수 호출 |
| 1 | 과목 설정 (name, category, size)를 변경 | 클래스 내부의 setInitSettings() 함수 호출 |
| 2 | 성적 입력 | 클래스 내부의 settingScore() 함수 호출 |
| 3 | 성적 조회 | 클래스 내부의 viewScore() 함수 호출 |
| 그외 | 프로그램 종료 | 내부 반복문 break |

한가지 옵션을 선택하여 작업을 수행한 후에는 '[NOTICE] 계속 관리하시겠습니까? (0. No, Otherwise. YES)'라는 문구가 출력됩니다.  
이때 사용자가 0 입력시 manageLecture() 함수가 종료되고, 이외의 키를 입력시 다시 옵션 선택 문구가 출력됩니다.

---
> option 0. showInfo()

```
print('')
print('>> 과목 설정 조회')
print(f'과목 이름: {self.getName()}, 과목 구분: {self.getCategory()}, 과목 수강 인원: {self.getSize()}')
print('-------------------------------------------------------------------')

```
위의 출력 형식대로 과목 설정을 출력합니다

+ 예시  
![image](https://github.com/user-attachments/assets/ecde5b1c-21c9-4041-aadc-752595772097)

---
> option 1. setInitSettings()

option 1 선택시 현재의 과목 설정 (과목 이름/과목 구분/수강 인원) 출력 후 옵션 선택 문구가 출력됩니다.

| 옵션 | 기능 | 설명 | 비고 |
| --- | --- | --- | --- |
| 0 | 취소 | 내부 반복문 break > manageLecture() '계속 관리하시겠습니까?'로 연결 | X |
| 1 | 과목 이름 변경 | 클래스 내부의 getName() 호출 | '0' 입력시 취소 |
| 2 | 과목 구분 변경 | 클래스 내부의 getCategory() 호출 | '0' 입력시 취소 |
| 3 | 수강 인원 변경 | 클래스 내부의 getSize() 호출 | '-1' 입력시 취소, 숫자 이외 입력시 Error 처리 |

0 이외의 옵션 동작 후에는 '[NOTICE] 수정이 추가로 필요할시 1, 수정 종료시 이외의 키 입력' 문구가 출력됩니다.  
1을 선택시 setInitSettings()의 옵션 선택 문구가 출력되며, 이외의 키 입력시 manageLecture() '계속 관리하겠습니까?'로 연결됩니다.

+ 예시
>  
  ![image](https://github.com/user-attachments/assets/bd9afe3f-89d0-44ac-bf1f-74f9d5b0aa8c)

---
> option 2. settingScore()

option 2 선택시 '[NOTICE] 학번-성적 입력 // ex: 20250000-96 // (0 입력시 종료): ' 문구가 출력됩니다.  
입력값에 따른 동작은 다음과 같습니다.

| 입력 | 동작 | 설명 |
| --- | --- | --- |
| 0 | 성적 입력 종료 | 내부 반복문 break > manageLecture() '계속 관리하겠습니까?'로 연결 |
| 학번-성적 | 성적 등록 | 내부 딕셔너리에 key=학번, value=int(학번)으로 저장 후 option 2 [NOTICE] 문구 출력 |
| 잘못된 형식 | 오류 발생 | - 기준으로 문자열이 2개가 아닐시 '잘못된 형식' 오류 문구 출력, 성적에 대응되는 문자열이 정수로 변환이 불가능할시 '성적은 숫자여야 합니다' 문구 출력 |

0 이외의 값 입력시 [NOTICE] 문구를 반복하여 출력하며 0을 입력할 때까지 성적을 입력받습니다.
0 입력시 현재까지 입력된 학생수를 출력하고, 옵션 2 종료 후 manageLecture() '계속 관리하시겠습니까?'로 연결됩니다.

+ 예시
>  
![image](https://github.com/user-attachments/assets/412975d7-ca3d-4fe8-a75e-d81e70749d30)

---
> option 3. viewScore()

option 3 선택시 '[NOTICE] 1 성적 입력 현황 / 2 학번으로 검색 / 3 순위 조회 / 그외 입력시 종료' 문구가 출력됩니다.
옵션에 따른 동작은 다음과 같습니다.  

1. 성적 입력 현황  
![image](https://github.com/user-attachments/assets/b34e81db-d639-40d5-8726-2289591d9c66)

위와 같이 수강 인원과 성적 입력된 학생 수를 출력합니다.  

2. 학번으로 검색  
![image](https://github.com/user-attachments/assets/b9fd2381-5187-4208-a126-35871fdf948b)

위와 같이 학번을 입력시 해당 학생의 점수와 등수를 출력합니다.
유효하지 않은 학번 입력시 에러 메시지가 출력됩니다.  

3. 순위 조회  
![image](https://github.com/user-attachments/assets/8ed7fd32-dceb-4fd5-9d13-ca888ba021a6)

위와 같이 [등수. 학번 - 점수] 형식으로 전체 학생의 등수를 출력합니다.

