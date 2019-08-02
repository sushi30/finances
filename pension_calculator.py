#%%
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[3]:


sns.set()


# In[4]:


def annuity(c, t, r):
    return c*((1-(1/(1+r)**t))/r)

def required_cash_flow(FV, t, r):
    return FV/sum(map(lambda x: (1+r)**x,range(t + 1)))

def future_value(c, t, r):
    return c * sum(map(lambda x: (1+r)**x, range(t+1)))

def commas(x):
    return '{:,}'.format(x)


# In[5]:


r = 1.04**(1/12) - 1
retiring_age = 62
pension_payment = 16_000
life_expectancy = 95


# In[6]:


required = annuity(pension_payment, (life_expectancy - retiring_age)*12, r)
print("required assets at retirement:", commas((round(required))))

for i in [30, 35, 40]:
    start_saving = i
    print("start saving at {}: ".format(i), end="")
    print(commas(round(inverse_annuity(total, (retiring_age - start_saving)*12, r))))


# In[ ]:


plt.plot(list(range(30, 45)), [inverse_annuity(total, (retiring_age - i)*12, r) for i in range(30, 45)])
plt.show()

