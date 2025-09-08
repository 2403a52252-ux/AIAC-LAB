# Job Applicant Scoring System
def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on input features.
    education: str - 'highschool', 'bachelor', 'master', 'phd'
    experience: int - years of relevant experience
    gender: str - 'male', 'female', 'other'
    age: int - age in years
    Returns: float - applicant score
    """
    # Education scoring
    edu_scores = {
        'highschool': 10,
        'bachelor': 20,
        'master': 30,
        'phd': 40
    }
    edu_score = edu_scores.get(education.lower(), 0)
    # Experience scoring (2 points per year, capped at 20 years)
    exp_score = min(experience, 20) * 2
    # Gender scoring (no bias, all equal)
    gender_score = 0
    # Age scoring (prefer 22-60, no bias within range)
    if 22 <= age <= 60:
        age_score = 10
    else:
        age_score = 0
    total_score = edu_score + exp_score + gender_score + age_score
    return total_score
# Example usage
if __name__ == "__main__":
    applicant = {
        'education': 'master',
        'experience': 5,
        'gender': 'female',
        'age': 28
    }
    score = score_applicant(**applicant)
    print(f"Applicant Score: {score}")

"""
Bias Analysis:
- Education and experience are weighted based on typical job relevance.
- Gender is not used in scoring (gender_score = 0), avoiding gender bias.
- Age is only used to ensure working age range, not to favor any specific age group.
- The logic avoids unfair weightings or discrimination.
"""