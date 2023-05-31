# opensw23-강김삼

# Team Introduction
  강윤원 202211249 리더
  
  김소희 202210728 코더
  
  김종혁 202211282 서포터
  
  김민형 202211270 서포터
# Topic Introduction
  - 레포지토리 주소 : https://github.com/smahesh29/Gender-and-Age-Detection.git

  - 주제 : 성별 및 연령 감지
  
  성별은 male 혹은 female 둘중 하나로 감지한다.
  
  연령은 (0 – 2), (4 – 6), (8 – 12), (15 – 20), (25 – 32), (38 – 43), (48 – 53), (60 – 100) 8개의 구간 중 하나로 감지한다.
# Results
example

<img width="312" alt="jonghyuck1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/a451eda9-9313-4f7e-a148-48d22b5ec638">
<img width="362" alt="sample1" src="https://github.com/KangYunWon/opensw23-KangKimSam/assets/127183027/58feb0e0-b17d-44fe-9e7a-484f48e9e581">

# Analysis/Visualization

# Installation
- 모든 구동은 cmd창에서 진행함.

- 구동 환경
  - os : window 10, window 11
  - 파이썬 3.9.13
 
- 추가 라이브러리 요구사항
  - opencv
  
    `pip install opencv-python`
  - argparse
  
    `pip install argparse`
    
- 구동 방법    
 
  1. repository 복사(cmd의 default path에서 실행함) 

      `git clone https://github.com/smahesh29/Gender-and-Age-Detection.git`
    
  2. repository를 복사하면 cmd의 default path 밑에 Gender-and-Age-Detection 디렉터리가 생성됨.
  
  3. 생성된 Gender-and-Age-Detection 디렉터리로 이동 후 detect.py파일 실행
  
    + 사진 파일을 이용해 성별, 나이 분석 시

      `python detect.py --image <image_name>`

    + 웹캠을 이용해 성별, 나이 분석 시

      `python detect.py`
    
# Presentation
