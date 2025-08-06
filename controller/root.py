# #apirouter 의 속성값인 prefix 를 사용하면 주소를 묶음으로 만들수 있다.

# from fastapi import APIRouter
# from config.urls import urls
# ctr1 = APIRouter()
# for index in range(len(urls[0])):
#     ctr1.add_api_route(**urls[0][index])
# # @ctr1.get(**urls[0]["get"])#읽기
# # def root():
# #     return {"test": "읽기"}
# # @ctr1.post(**urls[0]["post"])#수정
# # def root():
# #     return {"test": "수정"}
# # @ctr1.put(**urls[0]["put"])#생성
# # def root():
# #     return {"test": "생성"}
# # @ctr1.delete(**urls[0]["delete"])#삭제
# # def root():
# #     return {"test": "삭제"} 


# ctr2=APIRouter()
# for index in range(len(urls[1])):
#     ctr1.add_api_route(**urls[1][index])
# # @ctr2.get(**urls[1]["get"])
# # def root():
# #     return {"test": 2}
# # @ctr2.post(**urls[1]["post"])
# # def root():
# #     return {"test": "ctr2"}
# # @ctr2.put(**urls[1]["put"])
# # def root():
# #     return {"test": "ctr2"}
# # @ctr2.delete(**urls[1]["delete"])
# # def root():
# #     return {"test": "ctr2"}

# #ctr1을 사용해서 다 사용할 수 있다. 주소만 다르면 다른 결과가 나오니까.