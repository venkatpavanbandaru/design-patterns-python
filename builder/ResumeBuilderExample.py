class Resume:
    def __init__(self, name, age, grade,
                 skills, projects, awards,
                 hobbies, contact_email, linkedin_url):
        self.name = name
        self.age = age
        self.grade = grade
        self.skills = skills
        self.projects = projects
        self.awards = awards
        self.hobbies = hobbies
        self.contact_email = contact_email
        self.linkedin_url = linkedin_url

class ResumeBuilder:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._grade = ""
        self._skills = []
        self._projects = []
        self._awards = []
        self._hobbies = []
        self._contact_email = ""
        self._linkedin_url = ""

    def add_name(self, name):
        self._name = name
        return self

    def add_age(self, age):
        self._age = age
        return self

    def add_grade(self, grade):
        self._grade = grade
        return self

    def add_skill(self, skill):
        self._skills.append(skill)
        return self

    def add_project(self, project):
        self._projects.append(project)
        return self

    def add_award(self, award):
        self._awards.append(award)
        return self

    def add_hobby(self, hobby):
        self._hobbies.append(hobby)
        return self

    def add_contact_email(self, email):
        self._contact_email = email
        return self

    def add_linkedin_url(self, url):
        self._linkedin_url = url
        return self

    def add_education(self, education):
        self._grade = education
        return self

    def add_experience(self, experience):
        self._projects.append(experience)
        return self

    def build(self):
        return Resume(
            self._name,
            self._age,
            self._grade,
            self._skills,
            self._projects,
            self._awards,
            self._hobbies,
            self._contact_email,
            self._linkedin_url
        )

# Example usage
builder = ResumeBuilder()
resume = (
    builder
    .add_name("Venkat Pavan Bandaru")
    .add_education("B.Tech in CSE")
    .add_experience("2 years at TCS")
    .add_skill("Python")
    .add_skill("OOP")
    .build()
)
print(resume.__dict__)