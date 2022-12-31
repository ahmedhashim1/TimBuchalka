required_skills = ['python', 'github', 'linux']
candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'linux', 'github', 'python'},
    'carol': {'linux', 'github', 'python', 'javascript', 'html'},
    'daniel': {'java', 'github', 'pascal', 'c++'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'java', 'linux', 'github', 'pascal', 'c', 'lisp', 'modula-2', 'perl'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)
