- [00_Attention.ipynb](00_Attention.ipynb)
  1. RNN 구조의 인코더 디코더의 문제점
  2. 인코더 디코더에서의 어텐션 매커니즘
  3. ULMFiT(Universal Language Model Fine-tuning)
  4. 셀프 어텐션과 전이학습을 이용한 모델들
- [01_huggingface_간단구현.ipynb](01_huggingface_간단구현.ipynb)
  - 허깅페이스
  - transformer pipeline - 텍스트 분류
  - transformer pipeline - 개체명 인식(Ner)
  - transformer pipeline - 질의 응답
  - transformer pipeline - 요약
  - transformer pipeline - 번역
  - transformer pipeline - 텍스트 생성
- [02_text_classification.ipynb](02_text_classification.ipynb)
  - 진행 순서
  - 데이터셋
  - 데이터 셋 to Dataframe
  - **데이터 클래스 분포 확인**
  - 문장 길이 확인(최대 토큰 길이 측정)
  - 문장 토큰화 하기
  - 부분 단어 토큰화
  - 전체 데이터 셋 토큰화
  - DistilBERT 훈련하기
  - DistilBERT 예측 분류(machine learning head)
  - distilBERT(End to End finetuning)
  - cf) keras로 훈련 시키기(예시)
  - 직접 훈련한 모델 불러와서 사용 해보기(pipeline)
- [99_to_study.ipynb](99_to_study.ipynb)
  - python : mapping with dict
