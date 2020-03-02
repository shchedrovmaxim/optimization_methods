
# coding: utf-8

# In[97]:


import math as m


# In[98]:


def f(x,y):
    return x**2 + 8 * y**2 + 0.001 * x * y - x - y  


# In[99]:


def derivative_x(x,y, h=0.001):
    return ((f(x + h,y) - f(x-h,y)) / (2*h))
def derivative_y(x,y, h=0.001):
    return ((f(x,y + h) - f(x,y-h)) / (2*h))


# In[104]:


def grad_des1(alpha,eps, next_x, next_y):
    step = 1
    while(True):
    
        curent_x = next_x
        curent_y = next_y

        next_x = curent_x - alpha * derivative_x(curent_x,curent_y) 
        next_y = curent_y - alpha * derivative_y(curent_x,curent_y)
        
        norm = m.sqrt((curent_x - next_x)**2 +(curent_y - next_y)**2)
        
        print(step,'f(x,y)=',f(curent_x,curent_y),'\t','f_prime(x,y)=',derivative(curent_x,curent_y),'\n',
              'norm(x_k-x_k+1)=',norm,'\t','alpha=',alpha,'\n',
              'x=',next_x,'\t','y=',next_y,'\n')
        
        step = step + 1
        if f(next_x,next_y) > f(current_x,current_y):
            alpha = alpha / (step ** 2)
        
        if norm<eps:
            break
    return next_x,next_y


# In[105]:


grad_des1(0.99,1e-6,14,0)


# In[108]:


gr = (m.sqrt(5) + 1) / 2
def grad_des2(alpha,eps, next_x, next_y):
    step = 1
    while(True):
    
        curent_x = next_x
        curent_y = next_y

        next_x = curent_x - alpha * derivative_x(curent_x,curent_y) 
        next_y = curent_y - alpha * derivative_y(curent_x,curent_y)
        
        norm = m.sqrt((curent_x - next_x)**2 +(curent_y - next_y)**2)
        
        print(step,'f(x,y)=',f(curent_x,curent_y),'\t','f_prime(x,y)=',derivative(curent_x,curent_y),'\n',
              'norm(x_k-x_k+1)=',norm,'\t','alpha=',alpha,'\n',
              'x=',next_x,'\t','y=',next_y,'\n')
        
        step = step + 1
        
        
        
        a = 0
        b = 1
        toch = 1e-5
        while True:
            x1 = b-((b-a)/gr)
            x2 = a+((b-a)/gr)
            y1 = f(curent_x - x1 * derivative_x(curent_x,curent_y),curent_y - x1 * derivative_x(curent_x,curent_y))
            y2 = f(curent_x - x2 * derivative_x(curent_x,curent_y),curent_y - x2 * derivative_x(curent_x,curent_y))
            if (y1>=y2): a=x1
            else: b = x2
            if abs(b-a)<toch:
                alpha = (a+b)/2
                break
        

        
        if norm<eps:
            break
    return next_x,next_y


# In[109]:


grad_des2(0.99,1e-6,14,0)

