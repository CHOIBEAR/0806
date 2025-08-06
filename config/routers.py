# from controller import root

# api_config={
#     "title":"UV API",
#     "version":"0.0.1",
#     "docs_url":"/api_docs",
#     "redoc_url":None
    
# }
# ctr1_config={
#     "router":root.ctr1,
#     "prefix":"/docs",
#     "tags":["기능"]
# }
# ctr2_config={
#     "router":root.ctr2,
#     "prefix":"/docs",
#     "tags":["기능2"]
# }

# ctrs = [ctr1_config, ctr2_config] 
# #이 방식이 아니라면 직접 라우터에 속성값을 찾아 "router" : root.ctr1 이런식으로 지정가능.

from fastapi import APIRouter
from config.urls import urls
api_config = {
  "title":"UV API", 
  "version":"0.0.1", 
  "docs_url":"/api_docs", 
  "redoc_url": None
}

ctrs = []
for link in urls:
  ctr = APIRouter()
  router = {
    "prefix": link["prefix"],
    "tags": link["tags"],
  }
  for item in link["urls"]:
    ctr.add_api_route(**item)
    
  router["router"] = ctr
  ctrs.append(router)
#반복되는 패턴은 for를 이용해여 배열에 넣고 하나씩 꺼내쓰는게 가능하다.