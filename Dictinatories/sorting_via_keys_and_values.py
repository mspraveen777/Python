# sorting the dict
marks  = {"science": 90,"maths": 89,"english":97}
ans = dict(sorted(marks.items(), key = lambda x:x[1]))
print(ans)