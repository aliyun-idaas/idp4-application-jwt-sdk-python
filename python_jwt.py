import jwt
import json
from jwt.algorithms import RSAAlgorithm
from jwt.utils import force_bytes
from utils import key_path

my_idtoken = ""


## 1.接收token
def get_idToken(token):
    if not token.strip():
        print('token信息不能为空')
    else:
        get_user_info(token)


## 2.解析令牌
# 通过JWT解密库，使用公钥对传入的 id_token 进行解密。将公钥以字符串的形式从文件中读取出来，并作为key进行解密：
def get_user_info(id_token):
    try:
        algo = RSAAlgorithm(RSAAlgorithm.SHA256)
        # 请在keys文件夹中放入publicKey，
        # 开发前需要在IT管理员权限下前往应用->详细->导出 PKCS8 公钥来获取解密 `JWT`用的公钥，并安全地放置在能访问到的目录内
        # 这里指放到keys文件夹内
        pem_key = open(key_path('jwt_public_key_pkc8.pem'), 'r')
        public_key = algo.prepare_key(pem_key.read())
        token_info = jwt.decode(force_bytes(id_token), key=public_key, algorithms="RS256",
                                options={"verify_aud": False})
        # algorithms 签名算法，默认RS256
        # aud : audience 受众，在JWT应用详情中获取，这里指定不校验aud，如需校验，请传入audience,如下
        # token_info = jwt.decode(force_bytes(id_token), key=public_key, algorithms="RS256", audience='testplugin_jwt')
        # 注意防重放攻击，需要判断id_token是否已经使用过了，可以存放jti来达到该效果
        user_info = json.loads(json.dumps(token_info))
        username = user_info['sub']
        print(username)
        # 3.判断用户名是否在自己系统存在
        # 4.如果存在, 登录成功，返回登录成功后的页面
        # 5.如果注册时添加redirect_url，那么返回此自定义url页面
        # 6.否则返回系统默认操作页面
        # 7.如果不存在, 返回登录失败页面, 提示用户不存在
    except Exception as e:
        print(e)


get_idToken(my_idtoken)
