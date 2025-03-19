Name = []
score = []
grade = []
a = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

while True:
  try:
    x, y, z = map(str,input().split())
    if z == "P":
      continue
    score.append(float(y)*a[z])
    grade.append(float(y))
  except: break
  

print(sum(score)/sum(grade))
