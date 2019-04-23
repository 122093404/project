from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generate_token(key, data, expiration=60 * 60 * 2):
    """获取token"""
    s = Serializer(key, expires_in=expiration)
    return s.dumps(data).decode('utf-8')

def token_decode(key,token):
    """解码"""
    s = Serializer(key)
    try:
        data = s.loads(token.encode('utf-8'))
    except:
        return None
    return data