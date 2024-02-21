from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextSaver(BasePasswordHasher):
    #평문 그대로 저장
    algorithm='PlainTextSaver'

    def encode(self,password):
        return password
    

    def verify(self, password, encoded):
        return True