📄 urls.py – 전체 코드 분해 및 상세 설명
python
복사
편집
def get():
  return {"test": "읽기"}
def post():
  return {"test": "수정"}
def put():
  return {"test": "입력"}
def delete():
  return {"test": "삭제"}
✅ 설명:
API 요청에 응답할 기본 테스트용 함수들입니다.

각각 GET, POST, PUT, DELETE 요청에 대응되며 단순한 JSON 응답을 반환합니다.

FastAPI의 endpoint는 일반적인 Python 함수로 작성되며, 이러한 함수들을 add_api_route()나 include_router()에서 사용합니다.

python
복사
편집
ctr1 = {
  "prefix":"/docs", 
  "tags":["기능1"],
  "urls" : [ 
    {
      "methods":["GET"], 
      "path":"/", 
      "summary":"기본 조회", 
      "description":"기능1 기본 정보를 조회합니다.",
      "endpoint": get,
    },
    {
      "methods":["POST"],
      "path":"/", 
      "summary":"데이터 수정", 
      "description":"기능1 데이터를 수정합니다.",
      "endpoint": post,
    },
    {
      "methods":["PUT"],
      "path":"/", 
      "summary":"데이터 입력", 
      "description":"기능1 새로운 데이터를 입력합니다.",
      "endpoint": put,
    },
    {
      "methods":["DELETE"],
      "path":"/", 
      "summary":"데이터 삭제", 
      "description":"기능1 데이터를 삭제합니다.",
      "endpoint": delete,
    }
  ]
}
✅ 설명:
ctr1은 하나의 라우터 그룹 정의입니다.
prefix: /docs
→ 이 라우터에 등록되는 모든 경로 앞에는 /docs가 붙습니다.
예: /docs/

tags: ["기능1"]
→ Swagger UI 문서에서 해당 API들을 "기능1"이라는 그룹명 아래 묶어 표시합니다.

urls:
→ add_api_route()에 넘길 수 있는 딕셔너리들이 리스트로 들어 있습니다.
→ 각 딕셔너리의 구성은 다음과 같습니다:

항목	설명
methods	허용할 HTTP 메서드 (["GET"], ["POST"] 등)
path	해당 메서드가 적용될 URL 경로 (여기선 전부 /)
summary	Swagger 문서 요약
description	Swagger 문서 상세 설명
endpoint	호출될 실제 함수 (앞서 정의한 get, post 등)

👉 하나의 경로(/docs/)에 대해 다양한 HTTP 메서드를 설정해 RESTful API 설계가 가능하도록 구성되어 있음.

python
복사
편집
ctr2 = {
  "prefix":"/ctr2", 
  "tags":["기능2"],
  "urls" : [ 
    {
      "methods":["GET"], 
      "path":"/", 
      "summary":"기본 조회", 
      "description":"기능1 기본 정보를 조회합니다.",
      "endpoint": get,
    },
  ]
}
✅ 설명:
ctr2는 두 번째 라우터 그룹입니다.

기본 경로는 /ctr2, 태그는 "기능2".

단일 메서드(GET)만 등록되어 있으며, endpoint는 동일한 get() 함수를 재사용합니다.

실전에서는 ctr2에 별도의 get2(), post2() 같은 함수들을 분리해주는 게 바람직합니다.

python
복사
편집
urls = [ctr1, ctr2]
✅ 설명:
이 리스트는 routers.py에서 루프를 돌며 각각을 APIRouter로 변환하고 등록하게 됩니다.

routers.py의 핵심 역할은 이 urls 리스트를 순회하여 자동으로 API를 생성하는 것입니다.

🔁 전체 흐름 요약
arduino
복사
편집
get/post/put/delete 함수 정의
↓
ctr1, ctr2 같은 dict 형태로 라우터 구조 정의
↓
urls 리스트에 담음
↓
routers.py에서 urls 리스트를 순회하며
  → APIRouter 객체 생성
  → .add_api_route()로 각 url 등록
↓
main.py에서 FastAPI 앱에 라우터 등록
✅ 실행 결과 예시
전체 URL	메서드	응답 JSON
/docs/	GET	{"test": "읽기"}
/docs/	POST	{"test": "수정"}
/docs/	PUT	{"test": "입력"}
/docs/	DELETE	{"test": "삭제"}
/ctr2/	GET	{"test": "읽기"}

# 📘 FastAPI 라우터 정의 - urls.py 노트 요약 📂
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 목적:
- 라우터 그룹별 경로, 메서드, 설명 및 핸들러 함수들을 정의하는 설정 파일

🧩 구성 요소:
──────────────────────────────────────────────
1️⃣ 기본 endpoint 함수 정의
🔹 테스트용 함수이며 JSON 응답 반환
def get(): return {"test": "읽기"}
def post(): return {"test": "수정"}
def put(): return {"test": "입력"}
def delete(): return {"test": "삭제"}

2️⃣ ctr1: 기능1 라우터 설정
───────────────────────────────
ctr1 = {
  "prefix": "/docs",           # URL 접두어
  "tags": ["기능1"],           # Swagger 그룹명
  "urls": [                    # 각 HTTP 메서드별 설정
    {
      "methods": ["GET"],      # 허용 메서드
      "path": "/",             # 상대 경로
      "summary": "기본 조회",  # 문서 요약
      "description": "기능1 기본 정보를 조회합니다.",
      "endpoint": get          # 연결 함수
    },
    ... POST, PUT, DELETE 도 동일 구조
  ]
}

3️⃣ ctr2: 기능2 라우터 설정
───────────────────────────────
ctr2 = {
  "prefix": "/ctr2",
  "tags": ["기능2"],
  "urls": [
    {
      "methods": ["GET"],
      "path": "/",
      "summary": "기본 조회",
      "description": "기능1 기본 정보를 조회합니다.",
      "endpoint": get
    }
  ]
}

4️⃣ 전체 라우터 리스트로 묶기
───────────────────────────────
urls = [ctr1, ctr2]

🧠 요약 키워드:
- prefix: 경로 접두어 설정
- tags: Swagger 문서 분류
- methods: 허용 HTTP 메서드
- endpoint: 실제 실행할 함수
- summary/description: API 문서 정보

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ 이 파일은 routers.py에서 순회되어 자동 등록됨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
