# opensw23-강김삼

# Team Introduction
  강윤원 202211249 리더
  
  김소희 202210728 코더
  
  김종혁 202211282 서포터
  
  김민형 202211270 서포터
# Topic Introduction
  - 원본 프로젝트 레포지토리 주소 : https://github.com/smahesh29/Gender-and-Age-Detection.git

  - 주제 : 이미지 및 웹캠 영상으로 부터 성별 및 연령 감지

  - 내용 :
  
    - 딥러닝을 이용한 얼굴 인식 및 이를 이용한 성별, 나이 추정 프로그램이다.
  
    - Tal Hassner과 Gil Levi가 pretrained한 모델을 사용해 성별, 나이를 추정한다.
  
    - 입력받은 이미지 혹은 웹캠의 데이터에서 사람의 얼굴을 감지해 성별, 나이를 추정한다.
  
    - 성별은 male 혹은 female 둘 중 하나로 판단한다.
  
    - 연령은 (0 – 2), (4 – 6), (8 – 12), (15 – 20), (25 – 32), (38 – 43), (48 – 53), (60 – 100) 8개의 구간 중 하나로 판단한다.
    
    - python detect.py --image <파일명> 의 <파일명>에 jpg혹은 png형식의 사진 파일 이름 입력 시 일정 시간 후 입력한 사진에서 사람 얼굴을 인식해 성별, 나이를 추정한 내용을 사진에 추가해서 자동으로 팝업한다.(Results 항목의 output처럼 나온다.)
    
    - python detect.py로 실행 시 일정 시간 후 웹캠이 구동되어 웹캠에서 촬영된 영상에서 사람 얼굴을 인식해 성별, 나이를 추정한 내용을 영상에 추가해서 팝업한다. 카메라 현황에 실시간으로 성별과 나이가 출력되고 콘솔창에 추정 내용이 실시간으로 출력된다.
# Results
  |input data|input|output|
  |:---|:---:|:---:|
  |sample data|<img width="362" alt="sample1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/f9516e0e-e243-4891-a9e8-10e6ead64501">|<img width="362" alt="sample1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/58feb0e0-b17d-44fe-9e7a-484f48e9e581">|
  |male(20) original |<img width="312" alt="jonghyuck1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/d66de645-1bea-4fb9-9acf-671a72971934">|<img width="312" alt="jonghyuck1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/a451eda9-9313-4f7e-a148-48d22b5ec638">|
|       |          |        |
|    배경-검정   |      ![outblack](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/98dd011c-30f5-457c-90cb-7ab044022071)     |     ![Screenshot 2023-06-07 at 20 22 30](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/49b17f2b-9516-4614-a727-45a1dc54077e)    |
| 배경-흰색32#202020  |       ![out202020](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/8e6b957b-87bb-44eb-8a19-606dfd23ee15)  |     ![Screenshot 26](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/26ec42b4-ac12-42a0-893d-c105477b785a)   |
| 배경-빨강64#400000       |   ![out400000](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9bf0f99b-dd30-4648-ba74-99e33629a003)        |      ![out400000](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/e4e1a0be-3c53-4864-bb45-c806cecd584d)  |
|   배경-초록128#008000    |       ![out008000](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/f3d03f2d-b06f-4117-97ee-decc366eedfe)   |   ![Screenshot 24](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/6c3ff0c5-a516-43b5-bc84-5992ed32afb5)     |
|   배경-파랑128#000080    |  ![out000080](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/79c88caf-9d9c-4d27-95d2-047a2eaed4b6)        |   ![Screenshot 23](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/5305cc7e-5541-413d-a5f0-093aaac136cd)  |
|  배경-파랑192#0000c0     |       ![out0000c0](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/393659fb-ab44-4942-9d20-387aba08ed8c)  |   ![out0000c0](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/b99981be-165d-48f9-92bd-97939d652a6f)     |
|  배경-하늘224#00e0e0      |   ![out00e0e0](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9fbcbb4d-5198-4b2b-a1f1-fc06b2a84cee)       |     ![Screenshot 31](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/40042c7f-a3eb-4a19-8a09-6d4b6c89e94e)   |
|   배경-노랑256#ffff00    |      ![outffff00](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/2d289e10-fe78-4582-8b6f-04356db994ab)    |   ![Screenshot 13](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/c15343fa-a41e-46cc-a428-a1d1ce1b4d77)     |



# Analysis

| 강도＼색|	흰색-회색|	빨강|	초록|	파랑|	하늘-청록|	분홍-보라	|노랑| |  |
|---|---|---|---|---|---|---|---|---|:---:|
|0~255 |xxxxxx|	xx0000|	00xx00	|0000xx|	00xxxx|	xx00xx	|xxxx00| | 000000 |
|32 |	m 38-43	|-|	m 38-43|	-|	-	|m 8-12	|-|    | 검정|
|64	|m 38-43	|-|	m 38-43	|m 38-43|	m 38-43	|m 4-6 |	-|  | - |
|128|	m 38-43|	m 4-6|	m 8-12|	m 38-44|	m 38-43|	f 4-6	|m 38-43| | |
|192|	m 38-43	|m 4-6	|m 8-12	|m 4-6|	m 38-43	|f 4-6	|m 38-43|   | 원본|
|224|	m 38-43	|m 4-6	|m 8-12	|m 4-6|	m 38-43	|f 4-6	|m 8-12|  |m 15-20 |
|256|	-|	f 4-6	|m 8-12	|m 4-6	|m 8-12|	f 4-6	|m 8-12|  |"-"로 표기  |

data 개수 : 색 변경 43개 + 원본 1개 = 총 44개

# Visualization

| | | | |
|---|---|---|---|
|![blue](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/51ad9ff4-6ae7-4165-9e8b-5ba1fc397b56) |![green](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/81533437-65e5-42e8-9c2c-66cdb8873707) | ![pink](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/d188b165-a02a-4958-a681-cbd9ffb436f0) | ![red](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/88ab9c85-df8f-4342-8b41-6111e51b57f0) |
|  ![sky](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/386fd885-21eb-4f27-aee7-7390fbb1a5b4) | ![white](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/306c2f5f-1219-4dd3-9fb3-51f1b73fda99) | ![yellow](https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/0a89a269-155a-4cb8-8b43-e77342201d2b) ||











# Installation
- 모든 구동은 cmd창에서 진행한다.

- 구동 환경
  - os : window 10, window 11
  - 파이썬 3.9.13
  - lg gram 2021 ver.
  - cpu: 11th Gen Intel(R) Core(TM) i7-1165G7
  - RAM: 16.00GB
  - GPU: intel IRIS xe
 
- 추가 라이브러리 요구사항
  - opencv
  
    `pip install opencv-python`
  - argparse
  
    `pip install argparse`
    
- 구동 방법    
 
  1. repository 복사(cmd의 default path에서 실행함) 

      `git clone https://github.com/KangYunWon/opensw23-KangKimSam.git`
    
  2. repository를 복사하면 cmd의 default path 밑에 opensw23-KangKimSam 디렉터리가 생성됨.
  
  3. 생성된 opensw23-KangKimSam 디렉터리로 이동 후 detect.py파일 실행
  
      - 사진 파일을 이용해 성별, 나이 분석 시

        `python detect.py --image <image_name>`
      
        example
      
          `python detect.py --image girl1.jpg`
          
      - 웹캠을 이용해 성별, 나이 분석 시

        `python detect.py`
    
# Presentation
