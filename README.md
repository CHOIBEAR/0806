# 0806
routers
# 📘 FastAPI 라우터 구성 - routers.py 노트 요약 🛠️
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 목적:
- 여러 API 경로(prefix)와 메서드(GET, POST 등)를 자동으로 등록하고 관리하기 위한 구조화된 설정

🧩 주요 구성 요소:
──────────────────────────────────────────────
1️⃣ from fastapi import APIRouter
🔹 FastAPI의 모듈형 라우터 생성 도구

2️⃣ from config.urls import urls
🔹 urls.py에서 정의한 API 경로 세트 불러오기

3️⃣ api_config = {...}
🔹 FastAPI 앱에 적용될 설정 딕셔너리
   - title: API 문서 제목
   - version: API 버전
   - docs_url: Swagger 문서 경로
   - redoc_url: ReDoc 비활성화 설정

4️⃣ ctrs = []
🔹 완성된 라우터 딕셔너리를 담는 리스트

5️⃣ for link in urls:
🔹 urls.py 내 기능별 API 세트 순회

   ┗ ctr = APIRouter()
   🔸 각 기능마다 새로운 라우터 인스턴스 생성

   ┗ router = {
        "prefix": link["prefix"],
        "tags": link["tags"],
     }

   ┗ for item in link["urls"]:
        ctr.add_api_route(**item)
   🔸 각 엔드포인트를 라우터에 등록
   🔸 item 딕셔너리는 methods, path, endpoint 등을 포함

   ┗ router["router"] = ctr
   🔸 라우터 인스턴스를 딕셔너리에 추가

   ┗ ctrs.append(router)
   🔸 완성된 라우터를 목록에 저장

🔁 이 구조는 main.py에서 다음처럼 활용됨:
    for ctr in routers.ctrs:
        app.include_router(**ctr)

🧠 요약 키워드:
- 모듈화된 라우팅
- 자동 등록
- prefix/tag 기반 그룹화
- 확장성 높은 구조

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ 전체 흐름: urls.py → routers.py → main.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


3천자 풀이.
📄 routers.py – 전체 코드 분해 및 설명
python
복사
편집
from fastapi import APIRouter
from config.urls import urls
✅ 설명:
fastapi 패키지에서 APIRouter를 임포트합니다.

APIRouter는 FastAPI에서 라우팅 기능을 모듈화할 수 있게 도와주는 클래스입니다.

하나의 파일에서 여러 기능을 담당하지 않도록 하기 위해 각 기능별로 나눌 때 유용합니다.

config.urls에서 urls 객체를 임포트합니다.

이 객체는 urls.py 파일에 정의되어 있으며, 여러 API 경로(prefix), 태그(tags), 각 엔드포인트 설정들을 포함하는 리스트입니다.

이 파일이 핵심적으로 라우터 자동 생성에 사용됩니다.

python
복사
편집
api_config = {
  "title": "UV API",
  "version": "0.0.1",
  "docs_url": "/api_docs",
  "redoc_url": None
}
✅ 설명:
FastAPI 인스턴스를 초기화할 때 전달할 API 설정 정보를 저장한 딕셔너리입니다.

각 항목 의미는 다음과 같습니다:

"title": API 문서의 제목.

"version": API 버전 정보.

"docs_url": Swagger UI 문서가 열리는 경로 (기본: /docs → 커스터마이징: /api_docs).

"redoc_url": ReDoc 문서 URL (기본 /redoc) → None이면 비활성화됨.

👉 이 설정은 main.py에서 FastAPI(**routers.api_config) 식으로 사용됩니다.

python
복사
편집
ctrs = []
✅ 설명:
ctrs는 라우터 정보들을 담을 리스트입니다.

이 리스트에는 prefix, tags, router로 구성된 딕셔너리가 들어가며, 이 딕셔너리들은 main.py에서 app.include_router(**ctr)로 등록됩니다.

python
복사
편집
for link in urls:
✅ 설명:
urls는 urls.py에서 정의된 리스트이며, 각 요소는 다음과 같은 구조입니다:

python
복사
편집
{
  "prefix": "/docs",
  "tags": ["기능1"],
  "urls": [ ... API 설정들 ... ]
}
이 루프는 각 라우터 세트에 대해 반복 작업을 수행합니다.

python
복사
편집
  ctr = APIRouter()
✅ 설명:
새로운 APIRouter 인스턴스를 생성합니다.

이 인스턴스는 해당 기능의 URL과 엔드포인트들을 등록할 공간입니다.

python
복사
편집
  router = {
    "prefix": link["prefix"],
    "tags": link["tags"],
  }
✅ 설명:
현재 라우터의 경로(prefix)와 태그(tags) 정보를 가져와 router라는 딕셔너리에 저장합니다.

prefix: /docs, /ctr2 등과 같은 기본 경로.

tags: Swagger 문서에 표시될 분류용 카테고리 이름.

python
복사
편집
  for item in link["urls"]:
    ctr.add_api_route(**item)
✅ 설명:
link["urls"]는 각각의 HTTP 메서드(GET, POST 등), 경로, 요약, 설명, 실제 endpoint 함수 등을 담고 있는 딕셔너리들의 리스트입니다.

add_api_route(**item)는 unpacking을 통해 다음과 같이 동작합니다:

python
복사
편집
ctr.add_api_route(
  methods=["GET"],
  path="/",
  summary="기본 조회",
  description="기능1 기본 정보를 조회합니다.",
  endpoint=get
)
이 코드는 결국 APIRouter 인스턴스에 실제로 API 경로를 등록합니다.

👉 하나의 라우터(ctr) 안에 여러 메서드(GET, POST 등)를 같은 path에 다르게 연결할 수 있습니다.

python
복사
편집
  router["router"] = ctr
✅ 설명:
위에서 생성한 ctr (APIRouter 인스턴스)을 router 딕셔너리에 "router" 키로 추가합니다.

이 딕셔너리는 최종적으로 main.py에서 FastAPI 앱에 등록될 준비가 됩니다.

python
복사
편집
  ctrs.append(router)
✅ 설명:
완성된 router 객체를 전체 리스트인 ctrs에 추가합니다.

이 리스트는 여러 개의 모듈별 API를 구성하는 데 사용됩니다.

🧠 전체 흐름 정리 (그림 없이 텍스트로)
urls.py로부터 기능별 API 정보 목록(urls)을 불러옴.

각 기능(ctr1, ctr2 등)에 대해:

APIRouter 인스턴스를 새로 생성.

해당 기능의 메서드(GET, POST...)를 라우터에 .add_api_route로 등록.

prefix, tags, router 키로 구성된 딕셔너리를 만들어 ctrs에 저장.

최종적으로 ctrs 리스트는 main.py에서 사용되어 FastAPI 앱에 등록됨.

🔍 추가 기술 포인트
📌 **item과 **ctr의 의미
**item: 딕셔너리를 키워드 인자로 풀어서 전달 (add_api_route(**item)).

**ctr: main.py에서 app.include_router(**ctr) → prefix, tags, router 키를 가진 딕셔너리여야 함.

🧩 향후 확장 팁
확장 방식	설명
🔌 기능별 urls 분리	urls_docs.py, urls_ctr2.py 등으로 분리해 urls 리스트를 조합하면 유지보수 쉬움
🧪 Pydantic 모델 사용	response_model, request_model 등을 활용해 타입 검증 및 문서 자동화 가능
⚙️ 동적 import	config 파일에서 엔드포인트 경로만 지정하고 importlib으로 불러오기 가능
📁 디렉토리 기반 구성	/routes, /schemas, /controllers 등으로 파일 구조 개선