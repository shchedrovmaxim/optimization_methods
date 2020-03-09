
# coding: utf-8

# In[1]:


import math as m


# In[2]:


def f(x,y):
    return x**2 + 8 * y**2 + 0.001 * x * y - x - y  


# In[3]:


def derivative_x(x,y, h=0.001):
    return ((f(x + h,y) - f(x-h,y)) / (2*h))
def derivative_y(x,y, h=0.001):
    return ((f(x,y + h) - f(x,y-h)) / (2*h))


# In[70]:


def grad_des1(alpha,eps, next_x, next_y):
    step = 1
    while(True):
    
        curent_x = next_x
        curent_y = next_y

        next_x = curent_x - alpha * derivative_x(curent_x,curent_y) 
        next_y = curent_y - alpha * derivative_y(curent_x,curent_y)
        
        norm = m.sqrt((curent_x - next_x)**2 +(curent_y - next_y)**2)
        
        print(step,'f(x,y)=',f(curent_x,curent_y),'\t','x_k= ',curent_x,'y_k=',curent_y,
              '\n','f_prime_x=',derivative_x(curent_x,curent_y),'f_prime_y',derivative_y(curent_x,curent_y),'\n',
              'norm(x_k-x_k+1)=',norm,'\t','alpha=',alpha,'\n',
              'x=',next_x,'\t','y=',next_y,'\n')
        
        step = step + 1
        if f(next_x,next_y) > f(curent_x,curent_y):
            alpha = alpha / (step ** 2)
        
        if norm<eps:
            break
    return next_x,next_y


# In[73]:


grad_des1(1,1e-6,1,1)


# In[76]:


gr = (m.sqrt(5) + 1) / 2
def grad_des2(alpha,eps, next_x, next_y):
    step = 1
    while(True):
    
        curent_x = next_x
        curent_y = next_y

        next_x = curent_x - alpha * derivative_x(curent_x,curent_y) 
        next_y = curent_y - alpha * derivative_y(curent_x,curent_y)
        
        norm = m.sqrt((curent_x - next_x)**2 +(curent_y - next_y)**2)
        
        print(step,'f(x,y)=',f(curent_x,curent_y),'\t','x_k= ',curent_x,'y_k=',curent_y,
              '\n','f_prime_x=',derivative_x(curent_x,curent_y),'f_prime_y',derivative_y(curent_x,curent_y),'\n',
              'norm(x_k-x_k+1)=',norm,'\t','alpha=',alpha,'\n',
              'x=',next_x,'\t','y=',next_y,'\n')
        
        step = step + 1
        
        
        
        a = 0
        b = 1
        toch = 1e-5
        x1 = b-((b-a)/gr)
        x2 = a+((b-a)/gr)
        y1 = f(curent_x - x1 * derivative_x(curent_x,curent_y),curent_y - x1 * derivative_x(curent_x,curent_y))
        y2 = f(curent_x - x2 * derivative_x(curent_x,curent_y),curent_y - x2 * derivative_x(curent_x,curent_y))
        while True:
            if (y1 > y2): 
                a=x1
                x1=x2
                x2 = a+(b-a)/gr
                y1 = y2
                y2 = f(curent_x - x2 * derivative_x(curent_x,curent_y),curent_y - x2 * derivative_x(curent_x,curent_y))
            else: 
                b = x2
                x2 = x1
                x1 = b - (b-a)/gr
                y2 = y1
                y1 = f(curent_x - x1 * derivative_x(curent_x,curent_y),curent_y - x1 * derivative_x(curent_x,curent_y))
            if abs(b-a)<toch:
                alpha = a
                break
        

        
        if norm<eps:
            break
    return next_x,next_y


# In[86]:


grad_des2(1,1e-5,14,0)

