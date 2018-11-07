# Code by Vineet Kumar Doshi from HackerRank

if __name__ == '__main__':
    score_list = {}

    # Reads in an integer for number of students
    for _ in range(int(input())):

        # Reads in name and score for each student
        name = input()
        score = float(input())
        
        # Populates a dictionary (score_list) with each unique score as the key
        # and a list of student names as the values for each score
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]
           
    students_by_score = []

    # Populates a nested list with scores and lists of names for each score
    for i in score_list:
        students_by_score.append([i, score_list[i]])

    students_by_score.sort()

    # The list of student names with the second lowest score
    result = students_by_score[1][1]
    result.sort()
    print(*result, sep="\n")