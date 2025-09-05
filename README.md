✨ Korean Typo & Grammar Corrector

## 🔎 프로젝트 배경

맞춤법 교정기는 오래전부터 연구·개발되어 왔으며 hanspell, spacing 등 다양한 오픈소스가 존재합니다.
그러나 메신저 대화 기반 데이터에서는 기존 교정기가 잘 대응하지 못했습니다.

우리의 목표는 정밀한 맞춤법 교정이 아니라,
👉 사람과 모델(tokenizer)이 이해하기 쉬운 형태로 변형하여

NLU 정확도 향상

챗봇 답변의 품질 개선

DB 정제

을 실현하는 것입니다.

따라서 이 프로젝트는 완벽한 맞춤법 교정기가 아닌,
👉 현실적인 대화 데이터용 오탈자·띄어쓰기 교정기를 지향합니다.

## ✅ 주요 기능

입력 문장을 문장 단위 분리 후 교정

맞춤법, 띄어쓰기, 문장 부호, 음성인식 오류 등 교정

REST API 형태의 문장 교정 서비스 제공

## 📊 학습 데이터

**총 290,500문장**

### 포함 오류 유형
- 오탈자  
- 맞춤법 오류  
- 음성 인식기 오류  
- 자동 생성 오류  
- 띄어쓰기·문장부호 오류  
- 자주 틀리는 맞춤법 패턴  

### 전처리 과정
- 특수문자 제거  
- null 값 제거  
- name 태그 제거  
- 짧은 문장 제거  


## 🤖 사용 모델

HuggingFace T5ForConditionalGeneration

ETRI-ET5 한국어 모델 기반 커스텀 학습

## 🖥️ 학습 환경

Google Colab, VSCode

라이브러리: transformers, sentencepiece, torch

학습 결과 저장 구조:

checkpoint/        # config.json, pytorch_model.bin, generation_config.json
et5_model/         # tokenizer_config.json, spiece.model, config.json

## 📁 프로젝트 구조
```
.
├─ checkpoint/                  # 학습된 가중치 및 설정
│   ├─ config.json
│   ├─ generation_config.json
│   └─ pytorch_model.bin
│
├─ et5_model/                   # 토크나이저 및 설정
│   ├─ config.json
│   ├─ spiece.model
│   └─ tokenizer_config.json
│
├─ .dockerignore
├─ .gitattributes
├─ Dockerfile                   # API 서버 Docker 배포 환경
├─ README.md
├─ app.py                       # FastAPI inference 서버
├─ requirements.txt             # 의존성 패키지
```
## 🚀 기술 시연

요청 (POST)
```
{
  "text": " 협업을 통해 아이디어를 직접 구현해볼수있다는점에서 매력을 느끼썼습니다. 팀워크와 전공실력을 동시에 기르며 다양한○ 프로젝트를 함께 진행해나가고싶습니다. "
}
```
응답
```
{
  "corrected_text": "협업을 통해 아이디어를 직접 구현해 볼 수 있다는 점에서 매력을 느꼈습니다. 서로의 팀워크와 전공 실력을 동시에 기르며 다양한 프로그램을 함께 진행해 나가고 싶습니다."
}
```
➡️ 입력 문장에서 띄어쓰기, 오탈자, 맞춤법 오류를 자동으로 교정하여 보다 자연스러운 한국어 문장으로 변환합니다.

