#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


low_memory=False


# In[21]:


#Abrindo os arquivos CSV e produzindo os dataframes.
df_2013 = pd.read_csv ("DM_ALUNO_2013.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_DEF_FISICA"])
df_2014 = pd.read_csv ("DM_ALUNO_2014.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_DEF_FISICA"])
df_2015 = pd.read_csv ("DM_ALUNO_2015.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_DEF_FISICA"])
df_2016 = pd.read_csv ("DM_ALUNO_2016.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_DEF_FISICA"])
df_2017 = pd.read_csv ("DM_ALUNO_2017.CSV", delimiter = '|', encoding = "iso-8859-1", usecols = ["IN_DEFICIENCIA_FISICA"])


# In[23]:


#Declarando váriaveis para produzir o gráfico
def_2013 = (df_2013.query("IN_DEF_FISICA == 1")["IN_DEF_FISICA"].count())
def_2014 = (df_2014.query("IN_DEF_FISICA == 1")["IN_DEF_FISICA"].count())
def_2015 = (df_2015.query("IN_DEF_FISICA == 1")["IN_DEF_FISICA"].count())
def_2016 = (df_2016.query("IN_DEF_FISICA == 1")["IN_DEF_FISICA"].count())
def_2017 = (df_2017.query("IN_DEFICIENCIA_FISICA == 1")["IN_DEFICIENCIA_FISICA"].count())


# In[24]:


#Imprimindo o número de deficientes fisicos nas faculdades 
print(f"O número de deficientes fisicos nas faculdades em 2013 era de {def_2013} .")
print(f"O número de deficientes fisicos nas faculdades em 2014 era de {def_2014} .")
print(f"O número de deficientes fisicos nas faculdades em 2015 era de {def_2015} .")
print(f"O número de deficientes fisicos nas faculdades em 2016 era de {def_2016} .")
print(f"O número de deficientes fisicos nas faculdades em 2017 era de {def_2017} .")


# In[29]:


x = [2013, 2014, 2015, 2016, 2017]
y = [(def_2013), (def_2014), (def_2015), (def_2016), (def_2017)]

plt.title('Deficientes Fisicos nas Faculdades')
plt.xlabel('ANO')
plt.ylabel('Deficientes Fisicos')
plt.bar(x, y)
plt.show()


# In[ ]:




