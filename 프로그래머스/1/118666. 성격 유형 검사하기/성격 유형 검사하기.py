def solution(survey, choices):
    answer = ''
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            types[survey[i][0]] += scores[choices[i]]
        else:
            types[survey[i][1]] += scores[choices[i]]
    
    if types['R'] >= types['T']:
        answer += 'R'
    else:
        answer += 'T'
    if types['C'] >= types['F']:
        answer += 'C'
    else:
        answer += 'F'
    if types['J'] >= types['M']:
        answer += 'J'
    else:
        answer += 'M'
    if types['A'] >= types['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer