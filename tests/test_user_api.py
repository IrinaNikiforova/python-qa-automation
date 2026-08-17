from api.user_api import UserApi
from config.users import USER1

def test_users_me_api(user_api, auth_token):
    
    user_me = user_api.users_me(token=auth_token)
    assert user_me.email == USER1["email"]
    
def test_users(user_api, auth_admin_token, auth_token):

    users = user_api.users(token=auth_admin_token)
    user = user_api.users_me(token=auth_token)

    assert len(users.data) > 0
    user_email = user.email

    user_from_users = next((u for u in users.data if u.email == user_email ), None)
    user_from_users = user_from_users.model_dump(exclude={"enabled", "role", "failed_login_attempts"})
    user = user.model_dump()
    print(f"---------//---------------------")
    print(f" User from Users {user_from_users}")
    print(f"---------//---------------------")
    print(f" User : {user}")
    
    assert user_from_users == user, "Again "
    
    

