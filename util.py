from ast import Num
import random
import requests
import matplotlib.pyplot as plt

def generateRandomValue():
  r = random.randint(0, 100)
  return r

def generateGaussianDistribution(mu: Num, sigma: Num):
  return random.gauss(mu, sigma)

# nums = []
# mu = 15
# sigma = 10

# for i in range(1000):
#   temp = generateGaussianDistribution(mu, sigma)
#   nums.append(temp)
  
# plt.hist(nums, bins = 200)
# plt.show()

def transformRandomValueResult(num: int):
  if num <= 0:
    return "So little it would be shameful to expose it to others."
  return f"My dick is {str(num)} cm"

def getActivity():
  r = requests.get('http://www.boredapi.com/api/activity')
  return r.json()

# print(getActivity()['activity'].lower())