def get():
  return {"test": "읽기"}
def post():
  return {"test": "수정"}
def put():
  return {"test": "입력"}
def delete():
  return {"test": "삭제"}

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
      "path":"/", "summary":"데이터 수정", "description":"기능1 데이터를 수정합니다.",
      "endpoint": post,
    },
    {
      "methods":["PUT"],
      "path":"/", "summary":"데이터 입력", "description":"기능1 새로운 데이터를 입력합니다.",
      "endpoint": put,
    },
    {
      "methods":["DELETE"],
      "path":"/", "summary":"데이터 삭제", "description":"기능1 데이터를 삭제합니다.",
      "endpoint": delete,
    }
  ]
}
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
      "endpoint": put
    },
    {
      "methods":["DELETE"],
      "path":"/", 
      "summary":"데이터 삭제", 
      "description":"기능1 데이터를 삭제합니다.",
      "endpoint": delete
    }
    
  ]
}

urls = [ctr1, ctr2]
