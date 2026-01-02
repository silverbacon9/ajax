from flask_restful import Resource

class Users(Resource):
    def get(self):
        # 讀取所有資料
    
        return {"users": "所有使用者"}, 200 #狀態碼, 200代表正常


    def post(self):
        return {"users": "新增使用者"}, 200



# GET https://127.0.0.1/api.users/8
class User(Resource):
    def get(self, user_id):
        #根據UserID讀取資料
        return {"users": user_id}, 200
        

    def put(self, user_id):
        return {"users修改": user_id}, 200

    def delete(self, user_id):
        return {"users刪除": user_id}, 200