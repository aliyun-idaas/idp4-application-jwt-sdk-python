# idp4-application-jwt-sdk-python
jwt应用插件客户端python集成sdk

## 目录说明
- python_jwt.py  示例程序
- utils.py  工具类


## 使用前提

本Python JWT 示例使用PyJWT 库来进行 JWT 的解密
官方文档请参考：https://pyjwt.readthedocs.io/en/stable/
请先安装PyJWT环境

```shell
// 库的 github 链接 https://github.com/jpadilla/pyJWT
pip install PyJWT

// 注：CentOS系统如果使用时无法导入算法 RSAAlgorthm时需要下载pyJWT的2个依赖包
yum install ibffi-devel
pip install cryptography
```
