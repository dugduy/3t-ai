def wincal(lv):
    crs=[[0+(lv+1)*k for k in range(lv)],[lv-1+(lv-1)*k for k in range(lv)]]
    cols=[]
    rows=[]
    for k in range(lv):
        cols.append([k+lv*j for j in range(lv)])
        rows.append([k*3+j for j in range(lv)])
    result=crs+cols+rows
    return result
print(wincal(3))