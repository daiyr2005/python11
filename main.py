
from fastapi import FastAPI
from mysite.admin.setup import  setup_admin
from  mysite.api import user,auth
import  uvicorn


user_app = FastAPI(title='User')
user_app.include_router(user.user_router)
user_app.include_router(auth.auth_router)
setup_admin(user_app)



if __name__ == '__main__':
    uvicorn.run(user_app , host='127.0.0.1', port=8000)