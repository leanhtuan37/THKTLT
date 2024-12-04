print('danh sách có bao nhiêu số')
n=int(input())
lap=range(0,n,1)
ds=[]
for x in lap:
          print('nhập  số',x ' = ')
          gt=int(input())
          ds.append(gt)
ln=ds[0]
for x in ds:
       if(x>ln):
           ln=x
print('số lớn nhất là:',ln)
          
