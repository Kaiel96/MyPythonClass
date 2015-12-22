class Time: 
   def __init__(self, h, m, s):
      self.h=h 
      self.m=m
      self.s=s

class Timer: 
   '''A class to represent a timer
      Attributes: StartTime- a Time object 
                  StopTime- a Time object'''
   def __init__(self, startTime,stopTime): 
      self.startTime=startTime
      self.stopTime=stopTime

