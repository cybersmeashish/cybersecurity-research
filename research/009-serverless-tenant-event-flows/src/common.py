import base64,hashlib,hmac,json
# Public synthetic key exclusively for local fixtures; never a real credential.
KEY=b'synthetic-lab-key-not-for-production'
def sign(claims):
    body=base64.urlsafe_b64encode(json.dumps(claims,sort_keys=True,separators=(',',':')).encode()).decode().rstrip('=')
    return body+'.'+hmac.new(KEY,body.encode(),hashlib.sha256).hexdigest()
def verify(token):
    try:
        body,signature=token.split('.')
        if not hmac.compare_digest(signature,hmac.new(KEY,body.encode(),hashlib.sha256).hexdigest()):return None
        return json.loads(base64.urlsafe_b64decode(body+'='*(-len(body)%4)))
    except (ValueError,TypeError):return None
