'''import pandas as pd
ss1 = pd.Series([4,7,5,3],index=['a','b','c','d'])
print(ss1.index)
print(ss1['a'])
print('a'in ss1)
print(7 in ss1.values)
ss = pd.Series([1,-3,5,-7])
print(ss)
print('----')
print(ss.values)
print('----')
print(ss.index)
list_ex=["A",123,"B",456,"C",789]
list_to_Series=pd.Series(list_ex)
print(list_to_Series)
print('_'*10)
dic_ex={"A":123,"B":456,"C":789}
dic_to_Series=pd.Series(dic_ex)
print(dic_to_Series)
data={"name":['Bob','Nancy'],"year":[1996,1997],"month":[8,1],"day":[11,8],"ABC":['A','B']}
df=pd.DataFrame(data)
print(df)
print('________________________________')
df1=pd.DataFrame(data,columns=["name","day","month","year","ABC"],index=['甲','乙'])
print(df1)

df=pd.read_csv('csvsample.csv')
print(df.head(6))
print("___")
X=[['Amy','F',80],['Bob','M',65],['Cindy','F',73],['Dave','M',46],['Eva','F',46]]
df1=pd.DataFrame(X,columns=['name','gender','mathgrade'])
print("__________顯示方式一__索引方式_________")
print(df1['name'])
print(df1['name'].values)
print(df1['name'][1])
print(df1['name'][1].values)
import pandas as pd
df=pd.read_csv("nba.csv")
print(df['Name'])
print(df['Name'][0:6])
print(df[['Name','Team']].head(10))
df.insert(1,column="Sport",value="checked")
print(df.head())
df=df.drop("Sport",axis=1) 
print(df.head())  
df=df.drop(0,axis=0) 
print(df.head())
df=df.dropna() 
print('----')
df=pd.read_csv("nba.csv")
print(df.head())
   
df=df.fillna(10000) 
print(df.head()) 
df=pd.read_csv("nba.csv")
print(df.head(6))
print(df.sort_values('Age').head(6))
print(df.sort_values("Name",ascending=False).head(6))
import numpy as np 
frame = pd.DataFrame(np.random.rand(3,3),index=list('xyz'),columns=list('XYZ'))  
print(frame)   
print(frame.loc['x','X'])  
print(frame.loc['x':'y',:])
print(frame.loc[:,'X':'Y'])
print(frame.loc['x':'y','X':'Y'])
print(frame.loc[['x','z'],['X','Z']]) 
print(frame.iloc[0,0])   
print(frame.iloc[0:2,:])     
print(frame.iloc[:,0:2])  
print(frame.iloc[0:2,0:2])  
print(frame.iloc[[0,2],[0,2]]) 
import pandas as pd 
df=pd.read_csv("nba.csv")
print(df["Age"]>=25)
mask=(df["Age"]>=25)
print(df[mask].head(8))
import pandas as pd
col = ['class','name','bd']
data = [['classA','小明','1995-08-01'],
        ['classB','小美','1995-10-02'],
        ['classC','小黃','1995-06-01'],
        ['classC','小陳','1993-11-03'],
        ['classA','小花','1996-01-02'],
        ['classB','小雨','1996-02-03'],]
frame = pd.DataFrame(data,columns=col)
frame_class = frame.groupby('class')
print(frame_class.groups)
print(frame_class.get_group("classA"))'''

import numpy as np
import pandas as pd 
df = pd.DataFrame(
{'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
 'B':['one','one','two','three','two','two','one','three'],
 'C':np.random.randa(8),
 'D':np.random.randa(8)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['B','A']).sum())



                                         


