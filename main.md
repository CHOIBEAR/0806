📄 main.py – 전체 코드 분해 및 상세 설명
python
복사
편집
from fastapi import FastAPI
from config import routers
✅ 설명:
FastAPI 클래스를 가져와 앱 인스턴스를 만들 준비를 합니다.

routers 모듈은 config/routers.py를 의미하며, 이 파일 안에는:

api_config: FastAPI 앱 설정 정보

ctrs: urls.py 기반으로 생성된 라우터 목록 리스트

즉, 이 파일은 FastAPI 프로젝트의 진입점(entry point) 이며, 모든 라우터 등록과 앱 실행의 출발점입니다.

python
복사
편집
app = FastAPI(**routers.api_config)
✅ 설명:
FastAPI 앱 인스턴스를 생성합니다.

**routers.api_config는 routers.py에 정의된 api_config 딕셔너리를 unpack 해서 전달합니다.
예:

python
복사
편집
app = FastAPI(
  title="UV API",
  version="0.0.1",
  docs_url="/api_docs",
  redoc_url=None
)
📌 주요 설정 항목:
항목	설명
title	Swagger 문서 상단에 표시될 API 이름
version	API 버전 (버전 관리 또는 문서 구분 시 유용)
docs_url	Swagger UI 경로 (기본: /docs, 여기선 /api_docs로 변경됨)
redoc_url	ReDoc 문서 사용 여부 (None이면 비활성화됨)

👉 문서 접근은 기본 /docs가 아니라 /api_docs로 바뀌며, redoc은 제공되지 않습니다.

python
복사
편집
for ctr in routers.ctrs:
    app.include_router(**ctr)
✅ 설명:
🔁 동작 방식:
routers.ctrs는 routers.py에서 만들어진 라우터 정보 목록입니다.

각 ctr는 다음 형태의 딕셔너리입니다:

python
복사
편집
{
  "prefix": "/docs",
  "tags": ["기능1"],
  "router": <APIRouter 객체>
}
app.include_router(**ctr)는 이 딕셔너리를 unpack 하여 FastAPI 앱에 포함시킵니다:

python
복사
편집
app.include_router(
  prefix="/docs",
  tags=["기능1"],
  router=ctr_obj
)
📌 include_router의 역할:
각 라우터 모듈을 FastAPI 앱에 연결하여 경로 등록, 문서 분류, URL 구조화를 도와줍니다.

prefix는 모든 하위 URL에 공통 접두어로 적용됩니다.

tags는 Swagger 문서에서 분리된 그룹으로 표시됩니다.

🔁 전체 구조 흐름 요약
css
복사
편집
main.py
 └── FastAPI 인스턴스 생성 (api_config 적용)
 └── routers.ctrs 순회하여
     └── 각 router를 FastAPI 앱에 등록
     └── 결과적으로 모든 기능 경로가 app에 자동 포함됨
✅ 실제 라우팅 구성 예시
python
복사
편집
# app.include_router(...) 수행 결과
/docs/ [GET, POST, PUT, DELETE]
/ctr2/ [GET]
/docs/ → 기능1 관련 API (다중 메서드 지원)

/ctr2/ → 기능2 관련 API (GET만 지원)

Swagger 문서는 /api_docs 경로에서 확인 가능하며, ReDoc은 제공되지 않음.

📌 보완 및 확장 아이디어
개선 방향	설명
✅ 에러 핸들러 추가	FastAPI 앱에 공통 예외 처리 핸들러 등록
🧪 미들웨어 사용	CORS, 로깅, 인증용 미들웨어 적용 가능
🔒 보안 기능	OAuth2, JWT 인증 등을 main.py에서 초기화 가능
🌐 커스텀 이벤트	@app.on_event("startup") 등으로 DB 연결 등 설정 가능

# 📘 FastAPI 앱 실행 - main.py 노트 요약 🚀
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 목적:
- FastAPI 애플리케이션을 생성하고,
- 라우터들을 앱에 포함시켜 실행 가능하게 구성

🧩 구성 요소:
──────────────────────────────────────────────
1️⃣ from fastapi import FastAPI
🔹 FastAPI 앱을 만들기 위한 클래스 import

2️⃣ from config import routers
🔹 라우터 설정 모듈 import
   - routers.api_config: 앱 설정 정보
   - routers.ctrs: 생성된 APIRouter 리스트

3️⃣ app = FastAPI(**routers.api_config)
🔹 FastAPI 인스턴스를 설정과 함께 초기화
   - title: "UV API"
   - version: "0.0.1"
   - docs_url: "/api_docs" → Swagger UI 경로 변경
   - redoc_url: None → ReDoc 비활성화

4️⃣ for ctr in routers.ctrs:
       app.include_router(**ctr)
🔹 각 라우터 그룹을 FastAPI 앱에 등록
   - prefix: ex) "/docs"
   - tags: ex) ["기능1"]
   - router: APIRouter 인스턴스

🧠 요약 키워드:
- FastAPI 초기화
- API 문서 경로 지정
- 라우터 자동 등록
- 확장 가능한 구조

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ 전체 구조 흐름: urls.py → routers.py → main.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
