#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# 데이터 가져오기
code = pd.read_csv('./data/corpgeneral.csv')
code


# In[9]:


# 데이터 전처리
# 특정 칼럼 자르기
code = code[['회사명','종목코드']]

# 칼럼명 바꾸기(영어로)
code_result = code.rename(columns={'회사명':'corp','종목코드':'code'})
code_result


# In[10]:


# 해당 기업의 코드번호만 추출하기
corp_name = '카카오'
condition = "corp=='{}'".format(corp_name)
kakao = code_result.query(condition)
kakao = kakao['code']

# index는 제외하고 저장
kakao_string = kakao.to_string(index=False)
kakao_string = kakao_string.strip()

# 6자리 만들고 없으면 0 출력
kakao_string = kakao_string.rjust(6,'0')
kakao_code = kakao_string + '.KS'
kakao_code


# In[34]:


#conda install -c anaconda pandas-datareader


# In[11]:


# 해당 기업에 대한 정보 yahoo에서 가져오기
import pandas_datareader as pdr

kakao_stock_df = pdr.get_data_yahoo(kakao_code)
kakao_stock_df


# In[15]:


# 카카오 종가추출
kakao_stock_df['Close'].plot()


# In[3]:


from datetime import datetime


# In[12]:


code = pd.read_csv('./data/corpgeneral.csv', header=0)
code = code[['회사명','종목코드']]
code_result = code.rename(columns={'회사명':'corp','종목코드':'code'})
code_result


# In[13]:


# 해당 기업의 코드 가져오기
def get_code(code_result, corp_name):
    condition = "corp == '{}'".format(corp_name)
    code = code_result.query(condition)['code'].to_string(index=False)
    code = code.strip()
    code = code.rjust(6,'0')
    code = code + '.KS'
    return code


# In[14]:


samsung_code = get_code(code_result, "삼성전자")
samsung_code


# In[15]:


companies = ['삼성전자', 'LG전자', '카카오', 'NAVER', 'CJ', '한화', '현대자동차', '기아자동차']
start = datetime(2020,1,1)
end = datetime(2020,12,31)

# 데이터 프레임 생성
stocks_of_companies = pd.DataFrame({'Date':pd.date_range(start=start, end=end)})
stocks_of_companies


# In[16]:


for company in companies:
    company_code = get_code(code_result, company)
    stock_df = pdr.get_data_yahoo(company_code, start, end)
    # 종가 데이터 넣기
    stocks_of_companies = stocks_of_companies.join(pd.DataFrame(stock_df['Close']).rename(columns={'Close':company}), on='Date')
    


# In[28]:


corr_data = stocks_of_companies.corr()


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False


# In[25]:


plt.figure(figsize=(5,3))
corr_data = sns.lineplot(data=kakao_stock_df['Close'])


# In[29]:


plt.figure(figsize=(10,10))
# 히트맵으로 그리기
sns.heatmap(data= corr_data, annot=True, fmt = '.2f', linewidths=.5,cmap='Blues')
plt.show()


# In[30]:





# In[ ]:




