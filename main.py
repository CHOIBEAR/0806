#fastapi 메인파일
#라우터와 인클루드 사용.
#분리
 

from fastapi import FastAPI
from config import routers
app = FastAPI(**routers.api_config)
for ctr in routers.ctrs:
  app.include_router(**ctr)

    

#반복되는 패턴은 for를 이용해여 배열에 넣고 하나씩 꺼내쓰는게 가능하다.
