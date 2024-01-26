# super-octo-doodle
def ecdsa_siggen(msg,d):
    #1메시지 해시한걸 e에대입
    encode_msg=msg.encode()
    msgdigest=hashlib.sha256(encode_msg).hexdigest()
    e=int(msgdigest,16)
    e=e%p

    flag=0
    while flag==0:
        #2
        k=random.randrange(1,n)
        #3 [k]G연산
        X,Y,Z =kmul(k,gx,gy,1)
        zinv=mod_inv(Z,p)
        x1=(X*zinv)%p
        y1=(X*zinv)%p

        #4
        r=x1%n
        #5
        kinv=mod_inv(k,n)
        s=kinv*(e+r+d)%n
        
        if r==0:
            flag=0
        elif s==0:
            flag=0
        else:
            flag=1

    return r,s



def ecdsa_sigver(msg,r,s,Qx,Qy):
    ret=0
    #1
    if not (1<=r<n-1 or 1<=s<=n-1):
        ret =0
        return ret

    else:
        #2
         encode_msg=msg.encode()
         msgdigest=hashlib.sha256(encode_msg).hexdigest()
         e=int(msgdigest,16)
         z=e%p

         #3
         sinv=mod_inv(s,n)
         u1=(z*sinv)%n
         u2=(r*sinv)%n

        #4
        u1x,u1y,u1z = kmul(u1,gx,gy,1)
        u2x,u2y,u2z = kmul(u2,Qx,Qy,1)    

        X,Y,Z=pt_add_proj(u1x,u1y,u1, u2x,u2y,u2z)
        sinv=mod_inv(Z,p)
        x1=(X*zinv)%p
        

        #5
        chk=x1%n
        if chk==r:
            ret=1
        else:
            ret=0


        return ret

#키 생성
d,Qx,Qy=ecdsa_keygen()

r,s=ecdsa_siggen("abc",d)
ret=ecdsa_sigver("abc",r,s,Qx,Qy)
print("verification: ", ret)
