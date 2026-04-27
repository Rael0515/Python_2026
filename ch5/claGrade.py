def main():
    (kor_score, math_score, eng_score) = InputGrade()
    print("국어 학점은 ", claGrade(kor_score), "입니다.")
    print("수학 학점은 ", claGrade(math_score), "입니다.")
    print("영어 학점은 ", claGrade(eng_score), "입니다.")

def InputGrade():
    kor_score = int(input("국어 점수를 입력 하시오: "))
    math_score = int(input("수학 점수를 입력 하시오: "))
    eng_score = int(input("영어 점수를 입력 하시오: "))

    return (kor_score, math_score, eng_score)

def claGrade(score):
    
    if score >= 95:
        grade = "A+"
    elif 95>score and score>=90:
        grade = "A0"
    elif 90>score and score>=85:
        grade = "B+"
    elif 85>score and score>=80:
        grade = "B0"
    elif 80>score and score>=75:
        grade = "C+"
    elif 75>score and score>=70:
        grade = "C0"
    elif 70>score and score>=65:
        grade = "D+"
    elif 65>score and score>=60:
        grade = "D0"
    else:
        grade = "F"
    return grade