from ast import Num
import random
import requests
import matplotlib.pyplot as plt

step_0 = ["🤬", "😤", "😡", "👿", "😠", "🤡"]
step_5 = ["😧", "🥺", "😱", "😯", "😮", "😓"]
step_10 = ["😰", "😩", "😦", "😣", "😥", "🙁"]
step_15 = ["😐", "😬", "😑", "🙄", "🤭"]
step_20 = ["😎", "🤓", "🤠", "🥳", "😋"]
step_25 = ["🤩", "😇", "😘"]

def getRandom(arr):
  return random.choice(arr)

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
    return f"My dick is less 1 cm {getRandom(step_0)}"
  if num <= 5:
    return f"My dick is {str(num)} cm {getRandom(step_5)}"
  if num <= 10:
    return f"My dick is {str(num)} cm {getRandom(step_10)}"
  if num <= 15:
    return f"My dick is {str(num)} cm {getRandom(step_15)}"
  if num <= 20:
    return f"My dick is {str(num)} cm {getRandom(step_20)}"
  
  return f"My dick is {str(num)} cm {getRandom(step_25)}"

def getActivity():
  r = requests.get('http://www.boredapi.com/api/activity')
  return r.json()

# print(getActivity()['activity'].lower())