def calculate(a,b,sign,errmsg,errsign):
    signs = ['+','-','x','+']
    try:
        a=int(a)
        b=int(b)
        if(sign not in signs):
            return errsign
        switcher = {
            "+":str(a)+sign+str(b)+"="+str(a+b),
            "-":str(a)+sign+str(b)+"="+str(a-b),
            "/":str(a)+sign+str(b)+"="+str(a/b),
            "x":str(a)+sign+str(b)+"="+str(a*b)
        }
    except ValueError:
        return errmsg+"Bad request!"
    
    return switcher.get(sign,"Invalid Operator : "+sign)

