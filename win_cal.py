lv=3
for i in range(lv):
    for j in range(lv):
            print(i+lv*j)
for i in range(lv*lv):
    if i%lv==0:
        for j in range(lv):
            print(i+j)
for k in range(lv):
        print(0+(lv+1)*k)
for k in range(lv):
        print(lv-1+(lv-1)*k)