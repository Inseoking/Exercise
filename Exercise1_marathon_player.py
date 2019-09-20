# 완주하지 못한 1명을 찾는 예제
p=open("participant.txt",'rt')
c=open("completion.txt",'rt')

p_data=p.read()
c_data=c.read()
pp=p_data.split()
cc=c_data.split()
while len(pp)!=1:
    for i in pp:
        for j in cc:
            if i==j:
                pp.remove(i)
                cc.remove(j)`
            else:
                continue
print(pp)