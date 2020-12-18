# -*- coding: utf-8 -*-
"""cjamgotc_CPE490_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nb_Pp6mtZALrezGtBTcNfIEteSpU1vRW
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#Helper function to generate random data for given polynomial
def gen_data(noise_scale, number_of_samples):
  x = np.array(25*(np.random.rand(number_of_samples, 1)- 0.8))
  y = np.array(5 * x + 20 * x **2 + 1 * x**3 + noise_scale*np.random.randn(number_of_samples, 1))

  return x, y

Data
plt.style.use('seaborn-whitegrid')
x, y = gen_data(100, 50)
plt.plot(x, y ,'ro')
plt.show()

# data vs poly fit
# chose 3rd degree 
new_x = x.flatten()
new_y = y.flatten()

# models for nth order polynomials
model1 = np.poly1d(np.polyfit(new_x, new_y, 1))
model2 = np.poly1d(np.polyfit(new_x, new_y, 2))
model3 = np.poly1d(np.polyfit(new_x, new_y, 3))
model4 = np.poly1d(np.polyfit(new_x, new_y, 4))
model5 = np.poly1d(np.polyfit(new_x, new_y, 5))
model6 = np.poly1d(np.polyfit(new_x, new_y, 6))
model7 = np.poly1d(np.polyfit(new_x, new_y, 7))
model8 = np.poly1d(np.polyfit(new_x, new_y, 8))

# plot for initial data vs model in 3rd degree
plt.plot(x, y, 'ro')
new_line = np.linspace(-20, 5, 100)
plt.plot(new_line, model8(new_line))
plt.show()

# Mean squared error vs nth degree

# MSE for every nth degree poly
MSE_1 = mean_squared_error(new_y, model1(new_x))
MSE_2 = mean_squared_error(new_y, model2(new_x))
MSE_3 = mean_squared_error(new_y, model3(new_x))
MSE_4 = mean_squared_error(new_y, model4(new_x))
MSE_5 = mean_squared_error(new_y, model5(new_x))
MSE_6 = mean_squared_error(new_y, model6(new_x))
MSE_7 = mean_squared_error(new_y, model7(new_x))
MSE_8 = mean_squared_error(new_y, model8(new_x))



total_MSE = [MSE_1, MSE_2, MSE_3, MSE_4, MSE_5, MSE_6, MSE_7, MSE_8]
order_range = [model1.order, model2.order, model3.order, model4.order, model5.order, model6.order, model7.order, model8.order]

# plotting
plt.ylim(0, 80000)
plt.plot(order_range, total_MSE)
plt.title('MSE vs Order')
plt.xlabel('Degree')
plt.ylabel('Error')

# chose 3rd degree polynomial because it is in the elbow

"""**Part 3:**

"""

def noisechange_and_samples(noise, samples):
  plt.style.use('seaborn-whitegrid')
  x, y = gen_data(noise, samples)
  plt.plot(x, y ,'ro')

  plt.plot(x, y, 'ro')
  plt.title("Poly Fit Order 3, Noise Scale {}".format(noise))
  new_line = np.linspace(-20, 5, 100)
  plt.plot(new_line, model3(new_line))
  plt.show()

noisechange_and_samples(150, 50)
noisechange_and_samples(200, 50)
noisechange_and_samples(400, 50)
noisechange_and_samples(600, 50)
noisechange_and_samples(1000, 50)

"""**Part 4:**"""

def noise_and_sampleschange(noise, samples):
  plt.style.use('seaborn-whitegrid')
  x, y = gen_data(noise, samples)
  plt.plot(x, y ,'ro')

  plt.plot(x, y, 'ro')
  plt.title("Poly Fit Order 3, Sample Size {}".format(samples))
  new_line = np.linspace(-20, 5, 100)
  plt.plot(new_line, model3(new_line))
  plt.show()

noise_and_sampleschange(100, 40)
noise_and_sampleschange(100, 30)
noise_and_sampleschange(100, 20)
noise_and_sampleschange(100, 10)