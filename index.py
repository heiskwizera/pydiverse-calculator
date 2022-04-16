import helpers._appMessage as msg
import helpers.ops as calc
import helpers.appHandler as app

print(msg.startMessage)

read = str(input("Do you want to read instructions Y | n :  "))
app.toRead(read,msg.instructions)

res = []

a = input(msg.promptA)
sign = input(msg.promptSign)
b = input(msg.promptB)

res.append(a)
res.append(sign)
res.append(b)

result = calc.calculate(res[0],res[2],sign,msg.notInteger,msg.badSign)
app.result(result)
