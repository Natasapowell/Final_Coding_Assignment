

testscores = {"Python": [80, 90, 70, 95], "Stata": [90, 100, 95, 90], "R": [100, 90, 90, 100]}

print(testscores)

# to get the respective values we can ask for a key
print(testscores["Python"]) 

#an attempt for dictionary using an exercise from another class
testscores = {
  'Python': [80, 90, 70, 95],
  'Stata': [90, 100, 95, 90],
  'R': [100, 90, 90, 100]}

average = {}

for subject, scores in testscores.items():
  average_score = sum(scores) / len(scores)
  average[subject] = average_score
  print(f"{subject}'s average score: {average_score:.2f}")


