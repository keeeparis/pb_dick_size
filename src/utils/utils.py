import random

step_0 = ["🤬", "😤", "😡", "👿", "😠", "🤡"]
step_5 = ["😧", "🥺", "😱", "😯", "😮", "😓"]
step_10 = ["😰", "😩", "😦", "😣", "😥", "🙁"]
step_15 = ["😐", "😬", "😑", "🙄", "🤭"]
step_20 = ["😎", "🤓", "🤠", "🥳", "😋"]
step_25 = ["🤩", "😇", "😘"]

def getRandom(arr: list[str]) -> str:
  return random.choice(arr)

def generateGaussianDistribution(mu: int, sigma: int) -> float:
  return random.gauss(mu, sigma)

def transformRandomValueResult(num: int) -> str:
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


