# 트랜스포머
### 참고 서적 : [트랜스 포머를 활용한 자연어 처리](https://books.google.co.kr/books?id=BUihEAAAQBAJ&pg=PP1&dq=%ED%8A%B8%EB%9E%9C%EC%8A%A4%ED%8F%AC%EB%A8%B8%EB%A5%BC+%ED%99%9C%EC%9A%A9%ED%95%9C&hl=ko&newbks=1&newbks_redir=1&sa=X&ved=2ahUKEwj5yorIucmJAxUEh68BHfouDkEQ6AF6BAgJEAI)

- 구글 연구팀이 발표한 논문 ([Attention is all you need](https://arxiv.org/abs/1706.03762))
- 대형 언어 모델(LLM)을 뛰어 넘어 이미지 처리에도 사용된다.
- 사전 훈련 모델(및 데이터)을 이용해 개인에 맞춰 **파인튜닝(ULMFiT)**.

>[ULMFiT : Uniiversal Language Model Fine-tuning](https://arxiv.org/abs/1801.06146)
>1. **계층별 고정 (Layer-wise Freezing)**: 
>상위 계층부터 순차적으로 학습하여, 특정 작업에 필요한 정보는 조정하면서도 언어의 일반적인 패턴은 보존함.
>2. **차별적 미세 조정 (Discriminative Fine-tuning)**:
>계층마다 다른 학습률을 적용해, 상위 계층은 더 적극적으로 학습하고, 하위 계층은 덜 변화시킴.
>3. **기울어진 삼각 학습률 (Slanted Triangular Learning Rates)**:
>초기 학습률을 높게 시작해 빠르게 적응하고, 후반에는 낮춰 안정적으로 수렴하도록 함. <br><br>

### 목차

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
- [03_Transformer.ipynb](03_Transformer.ipynb)
  - **어텐션 가중치(attention weights)**
  - seq2seq 의 attention 매커니즘(인코더 디코더 어텐션)
  - 기존 seq2seq 및 + attention 이용의 단점
  - [트랜스 포머](https://arxiv.org/pdf/1706.03762)
  - 다양한 트랜스 포머 모델들
  - **셀프 어텐션**
  - 어텐션 시각화
  - 밀집 임베딩 만들기
  - 셀프 어텐션 구하기(임베딩 된 벡터들을 이용하여 유사도 계산)
  - bert-base-uncased의 어텐션 헤드 출력 확인
  - Position Wise Feed Forward Layer
  - 층 정규화 및 스킵 커넥션
  - 인코더 구현
  - 위치 임베딩 추가하기
  - 상대적 위치 표현을 포함한 트랜스 포머의 인코더
  - 분류 헤드 추가하기
  - 디코더 의 어텐션
  - 평가 방법, 및 데이터셋
  - 다양한 트랜스포머 모델들



<details>
<summary>🤗 다양한 Transformer 모델들🤗</summary>

### 다양한 트랜스 포머 기반의 모델들
| 연도  | 설명                                                               |
|-------|--------------------------------------------------------------------|
| 2017  | **Transformer**: "Attention is all you need" 논문에서 소개된 모델로, 순차적인 데이터 처리 없이 병렬 처리가 가능.<br>**ULMFiT**: 전이 학습을 활용한 언어 모델로, NLP 태스크에서 높은 성능을 발휘. |
| 2018  | **BERT**: Bidirectional Encoder Representations from Transformers의 약자로, 문맥을 양방향으로 이해하므로 다양한 NLP 태스크에서 성능이 우수.<br>**GPT-1**: Generative Pre-trained Transformer 1으로, 텍스트 생성에 강점을 보임. |
| 2019  | **T5**: 모든 NLP 태스크를 텍스트 변환 문제로 간주하여 훈련.<br>**BART**: 텍스트 요약 및 생성에 특화된 모델.<br>**XLNet**: BERT의 개선 모델로, 순열 기반의 훈련 방식 사용.<br>**ERNIE**: 지식 주입을 통한 언어 모델 개선.<br>**GPT-2**: GPT의 후속 모델로, 더 큰 데이터와 매개변수를 활용.<br>**ELECTRA**: 효율적인 훈련 방식을 통한 성능 개선.<br>**GPT-3**: 1750억 개의 매개변수를 가진 매우 대규모 모델. |
| 2020  | **Chinchilla**: 효율적인 훈련을 위해 데이터를 최적화한 모델.<br>**InstructGPT**: 사용자의 지시를 이해하고 따르는 텍스트 생성 모델.<br>**CodeGen**: 코드 생성 및 완성을 위한 모델.<br>**WebGPT**: 웹에서 정보를 검색하고 요약하는 기능에 중점.<br>**ERNIE 3.0 TITAN**: 더욱 강화된 지식 주입 기능.<br>**GLaM**: 더 적은 매개변수로 높은 성능을 발휘.<br>**Gopher**: 자연어 처리에서 강한 성능을 가진 모델.<br>**Cohere**: 비즈니스에 최적화된 언어 모델.<br>**MT-NLG**: 초대형 NLG 모델.<br>**T0**: 사전 훈련된 변환기 기반의 모델.<br>**Yuan 1.0**: 중국어 중심의 언어 모델. |
| 2021  | **GPT-Neo**: 오픈 소스 GPT 대안.<br>**Switch**: 다양한 태스크에 적응할 수 있는 모델.<br>**GLM**: Generalized Language Model, 다양한 언어 처리에 최적화.<br>**GPT-J**: 오픈 소스 GPT-3 대안.<br>**Pangu-α**: 대규모 비즈니스 언어 모델.<br>**PLUG**: 텍스트와 행동의 연계를 중점.<br>**FLAN-PaLM**: 다중 태스크 성능 향상.<br>**FLAN-T5**: 다양한 NLP 태스크에 활용.<br>**BioGPT**: 생물학적 텍스트 처리를 위한 모델. |
| 2022  | **BLIP**: 비주얼-언어 모델.<br>**LaMDA**: 대화형 AI 모델, 자연스러운 대화 처리.<br>**GPT-NeoX-10B**: 10억 개의 매개변수를 가진 고성능 모델.<br>**AlphaCode**: 프로그래밍 코드 생성.<br>**GLM-130B**: 저비용 고성능 모델.<br>**BLOOM**: 오픈 소스 멀티언어 모델.<br>**Sparrow**: 안전한 대화형 AI.<br>**Galactica**: 과학적 텍스트 이해에 중점.<br>**BLOOMZ**: 다국어 지원 모델.<br>**FLAN**: 다양하고 유연한 특성.<br>**ChatGPT**: 다양한 대화형 태스크에 적합. |
| 2023  | **Claude 2**: 대화형 AI 발전.<br>**Bard**: 창의적인 텍스트 생성.<br>**Alpaca**: 소규모 파라미터 모델.<br>**ChatGLM**: 대화형 생성 모델.<br>**GPT-4**: GPT 시리즈의 최신 모델.<br>**MiniGPT-4**: 소형 버전의 GPT-4.<br>**LLaVA**: 시각-언어 모델.<br>**mPLUG-owl**: 멀티모달 처리.<br>**YuLan-Chat**: 대화적 AI.<br>**Baichuan**: 중국어 중심의 언어 모델.<br>**VPGTrans**: 비전-언어 모델.<br>**OpenLLaMA**: 오픈 소스 변환 모델.<br>**Otter**: 자연어 처리 기능 강화.<br>**Falcon LLM**: 빠르고 효율적인 모델.<br>**WizardLM**: 다양한 태스크에 적합.<br>**RedPajama-INCITE**: 데이터 처리 최적화.<br>**UltraLM**: 고성능 언어 모델.<br>**Ziya**: 다양한 언어 지원.<br>**InternLM**: 내부 태스크 지원.<br>**MPT-7B**: 7억 개의 파라미터를 가진 모델.<br>**Koala**: 우호적인 대화형 모델.<br>**Baize**: 다양한 주제 처리.<br>**CodeGeeX**: 코드 처리 최적화.<br>**MultimodalGPT**: 멀티모달 정보 처리. |

</details>