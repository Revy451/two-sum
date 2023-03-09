from typing import List

class Answer(object):
  List = []
  List= list(map(int, input("리스트 숫자 입력(띄어쓰기로 구분):").split()))
  target = input("타겟 숫자 입력: ")

  def twoSum(nums: List[int], target: int) :
    for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
  twoSum(List,target)