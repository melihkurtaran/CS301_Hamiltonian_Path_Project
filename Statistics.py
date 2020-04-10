import math  

def calculateSD(data):
  sum = 0
  sD = 0
  for d1 in data:
    sum += d1
  mean = sum / len(data)
  for d2 in data:
    sD += (d2-mean)**2
  sD = math.sqrt(sD/len(data))
  return sD #standart deviation

def calculateStandardError(sD,N):
  return sD / math.sqrt(N)

def getRunningTime(runningTimes):
  sD = calculateSD(runningTimes)
  N = len(runningTimes)
  totalTime = 0
  for r in runningTimes:
    totalTime += r

  m = totalTime / N #sample mean

  tval90 = 1.645 #t-value for 90% confidence
  tval95 = 1.96 #t-value for 95% confidence

  error = calculateStandardError(sD,N)

  upperMean90 = m + tval90*error 
  lowerMean90 = m - tval90*error 
  upperMean95 = m + tval95*error 
  lowerMean95 = m - tval95*error 

  print("Mean Time: ", m)
  print("Standard Deviation: ", sD)
  print("Standard Error: ", error)
  print("90% CL: ", upperMean90,"-",lowerMean90)
  print("95% CL: ", upperMean95,"-",lowerMean95)