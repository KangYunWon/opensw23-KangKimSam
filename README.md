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
  |male(20) original |<img width="312" alt="jonghyuck1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/d66de645-1bea-4fb9-9acf-671a72971934">|<img width="312" alt="jonghyuck1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/a451eda9-9313-4f7e-a148-48d22b5ec638">|
  |분홍배경-outff00ff|<img width="312" alt="outff00ff" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/c9039770-8c9f-4768-a291-cfbd57fee730">|<img width="312" alt="outff00ff" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/4d5c8088-182a-4b98-adb8-af178ff4f900">|
  |female(22)-마스크 착용|<img width="312" alt="KSH4" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/708faf3f-ae1c-454f-a34c-ef0ed925218b">|<img width="312" alt="KSH4output" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/c685f8d7-fac5-4ba2-bf65-09aacf2cc2c7">|
  
|||
|:---|:---:|
|webcam|![webcam 2023-06-08 16-57-08](https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/87fa05cf-5cfa-4258-bee0-a7636ad3f9ee)
|
 

# Analysis & Visualization

- Analysis & Visualization 1

![graph1](https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/1b663223-e92a-4216-a477-7a7f028139f8)

(data 개수: 6개)

얼굴의 일부가 가려질 수록 오차율은 커졌고 가장 많이 가려진 KSH4.jpg(마스크 착용)의 경우 얼굴 자체를 감지하지 못하는 결과가 나타난 것으로 보아 얼굴의 일부가 가려질 수록 얼굴을 감지하는 능력이 떨어진다고 판단됨. 



- Analysis & Visualization 2

||||
|---|---|---|
|<img width="250" alt="graph1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/ad429da4-4539-4fc0-8fc5-951300a0cc74">|<img width="250" alt="graph2" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/9ceb1d2b-7f47-4b35-bcfe-c05ff3b29f4b">|<img width="250" alt="graph3" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/60549bba-04ce-4aba-9fff-9aced5355ec2">|
|<img width="250" alt="graph4" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/ce036858-6b0e-4d11-a671-504df06837c2">|<img width="250" alt="graph5" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/4e9ba784-ee84-44aa-af33-6c9a050c99ca">|<img width="250" alt="graph6" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127182199/2eb1dd14-fd61-4734-90f0-90ef336e35f5">|

(data 개수: 86개)

가설대로 좌우각도, 상하각도 모두에서 정면각도에 가까울 수록 실제 인물의 성별과 나이인 Male, 22years와 유사한 결과가 나옴.

상대적으로 좌우각도에 비해 상하각도에 따라서 성별과 나이 분석의 정확도가 많이 떨어짐을 알 수 있음.

눈을 감는 것과 뜨는 것은 성별과 나이 분석에 큰 영향을 주지 않는다는 것을 알 수 있음.

머리를 내려 얼굴이 가려질 때 좌우각도에 따라 성별과 나이 분석 결과의 정확도가 굉장히 떨어지는 것을 확인할 수 있었음.

좌우각도가 변할 때  성별에 대한 분석 정확도가 많이 떨어짐을 알 수 있음.



- Analysis & Visualization3

| | | | |
|---|---|---|---|
|<img width="200" alt="blue" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/603cf50b-8d5e-46fb-8d58-0f4c6e9c6a50"> | <img width="200" alt="green" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9dc24a5a-6bfc-4283-9a44-21f180976b43"> | <img width="200" alt="pink" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/d4080d07-1eeb-4662-9c02-036fb778e343"> | <img width="200" alt="red" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9420b484-ddaa-465d-9148-d6dad8f2727f"> |
| <img width="200" alt="sky" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/b03ed8c2-7793-4d9c-b476-304bbdb29446"> | <img width="200" alt="white" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/4c9891de-7102-48c0-a9aa-dbab1bda6c78">  | <img width="200" alt="yellow" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/604859af-ff29-4115-961d-f088b9b181e5"> |  |

| 강도＼색|	흰색-회색|	빨강|	초록|	파랑|	하늘-청록|	분홍-보라	|노랑| |  |
|---|---|---|---|---|---|---|---|---|:---:|
|0~255 |xxxxxx|	xx0000|	00xx00	|0000xx|	00xxxx|	xx00xx	|xxxx00| | 000000 |
|32 |	male 38-43	|-|	male 38-43|	-|	-	|male 8-12	|-|    | 검정|
|64	| male 38-43	|-|	male 38-43	|male 38-43|	male 38-43	|male 4-6 |	-|  | - |
|128|	male 38-43|	male 4-6|	male 8-12|	male 38-44|	male 38-43|	female 4-6	|male 38-43| | |
|192|	male 38-43	|male 4-6	|male 8-12	|male 4-6|	male 38-43	|female 4-6	|male 38-43|   | 원본|
|224|	male 38-43	|male 4-6	|male 8-12	|male 4-6|	male 38-43	|female 4-6	|male 8-12|  |male 15-20 |
|256|	-|	female 4-6	|male 8-12	|male 4-6	|male 8-12|	female 4-6	|male 8-12|  |"-"로 표기  |

예시) 초록 64 = "#004000"

(data 개수: 44개)

채도가 낮을수록 나이를 많게 측정하는 경향을 보임. 

배경색이 검정색에 가까워질수록 검정 채도가 강해서 나이를 정확히 측정하는 것을 관찰할 수 있음.

붉은 계통의 색에서 상대적으로 성별을 여성으로 판단할 가능성이 높다는 것을 관찰할 수 있었음



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
  
      - 사진 파일을 이용해 성별, 나이 분석 시(image파일은 detect.py랑 같은 디렉토리에 위치해야 함)

        `python detect.py --image <image_name>`
      
        example1
      
          `python detect.py --image girl1.jpg`
          
        example2(이미지 파일 이름에 띄어쓰기가 들어가는 경우)
        
          `python detect.py --image "girl 1.jpg"`
          
      - 웹캠을 이용해 성별, 나이 분석 시

        `python detect.py`
    
# Presentation
https://www.youtube.com/watch?v=L_osJHiKF6Y&ab_channel=%EA%B9%80%EC%A2%85%ED%98%81
