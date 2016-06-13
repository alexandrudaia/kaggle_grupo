# In[141]:

#n=500- number  of  stores-500*1000 random samples
#for  test purpose  i  have    only  4 files
import  os 
os.chdir('/media/machine_learning/A80C461E0C45E7C0/bilboa')
#first  ds
f='store'+str(1)+".csv"
num_lines = sum(1 for l in open(f))
size = 500
skip_idx = random.sample(range(1, num_lines), num_lines - size)
colect_data=  pd.read_csv(f, skiprows=skip_idx)

n=500
for i in  range(2,n+1):
    f='store'+str(i)+".csv"
    print(f)
    num_lines = sum(1 for l in open(f))
    if num_lines < 500 :
       size=num_lines-1
    else:
        size = 1000
 
    #this will make  us   train  file   of about  500k  features
    skip_idx = random.sample(range(1, num_lines), num_lines - size)
    data = pd.read_csv(f, skiprows=skip_idx)
    frames=[colect_data,data]
    colect_data=pd.concat(frames)


# In[142]:

features=['Agencia_ID','Canal_ID','Ruta_SAK','Cliente_ID','Producto_ID']
target=['Demanda_uni_equil']


# In[143]:

trainvec=colect_data[features]
y=colect_data[target]
trainvec=np.array(trainvec)
y=np.array(y)
#test=pd.read_csv('test.csv')
#id=test['id']
#testvec=test[features]
#testvec=np.array(testvec)

