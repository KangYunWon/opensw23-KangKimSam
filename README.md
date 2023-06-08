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
<img width="497" alt="outff00ff" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/4d5c8088-182a-4b98-adb8-af178ff4f900">

![outff00ff](https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/c9039770-8c9f-4768-a291-cfbd57fee730)

# Analysis

| 강도＼색|	흰색-회색|	빨강|	초록|	파랑|	하늘-청록|	분홍-보라	|노랑| |  |
|---|---|---|---|---|---|---|---|---|:---:|
|0~255 |xxxxxx|	xx0000|	00xx00	|0000xx|	00xxxx|	xx00xx	|xxxx00| | 000000 |
|32 |	male 38-43	|-|	male 38-43|	-|	-	|male 8-12	|-|    | 검정|
|64	| male 38-43	|-|	male 38-43	|male 38-43|	male 38-43	|male 4-6 |	-|  | - |
|128|	male 38-43|	male 4-6|	male 8-12|	male 38-44|	male 38-43|	female 4-6	|male 38-43| | |
|192|	male 38-43	|male 4-6	|male 8-12	|male 4-6|	male 38-43	|female 4-6	|male 38-43|   | 원본|
|224|	male 38-43	|male 4-6	|male 8-12	|male 4-6|	male 38-43	|female 4-6	|male 8-12|  |male 15-20 |
|256|	-|	female 4-6	|male 8-12	|male 4-6	|male 8-12|	female 4-6	|male 8-12|  |"-"로 표기  |

data 개수 : 색 변경 43개 + 원본 1개 = 총 44개

에시 ) 초록 64 = "#004000"

# Visualization

| | | | |
|---|---|---|---|
|<img width="129" alt="blue" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/603cf50b-8d5e-46fb-8d58-0f4c6e9c6a50"> | <img width="128" alt="green" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9dc24a5a-6bfc-4283-9a44-21f180976b43"> | <img width="128" alt="pink" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/d4080d07-1eeb-4662-9c02-036fb778e343"> | <img width="129" alt="red" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/9420b484-ddaa-465d-9148-d6dad8f2727f"> |
| <img width="129" alt="sky" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/b03ed8c2-7793-4d9c-b476-304bbdb29446"> | <img width="129" alt="white" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/4c9891de-7102-48c0-a9aa-dbab1bda6c78">  | <img width="126" alt="yellow" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/129364199/604859af-ff29-4115-961d-f088b9b181e5"> |  |












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
