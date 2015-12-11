import numpy as np

class Distance:
      def __init__(self,histA,histB):
           self.histA=histA # image A histogram
           self.histB=histB #image B histogram
      # chi distance formula P*sigma[(a-b)^2/a+b+eps]
      def chi_distance(self,eps = 1e-10):
                  # compute the chi-squared distance
                  d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(self.histA,self.histB)])
                  return d


def hello():
    return "you are in distance module"
