scores = [91,95,97,99,92,93,96,98]
scores_lower = []

import numpy as np
average = np.mean(scores)
print('平均成绩是:{}'.format(average))

for i in scores:
    if i < average:
        scores_lower = scores.append(i)

print(scores_lower)
#print('低于平均分的有:{}'.format(scores_lower))