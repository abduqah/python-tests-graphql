import requests
import json

query = """query {
                  ucompare {
                    skills {
                      id,
                      title
                    }

                    professions {
                      id,
                      title  
                    }

                    universities {
                      id,
                      name
                    }

                    companies {
                      id,
                      name
                    }

                    professionLevels {
                      id,
                      title
                    }

                    educationalLevels {
                      id,
                      title
                    }

                    degreeTypes {
                      value,
                      label
                    }

                    workExperiences {
                      value,
                      label
                    }

                    jobLevels {
                      value,
                      label
                    }
                  }
                }"""


r = requests.post('https://uleague.org/graphql', json={'query': query})
json_data = json.loads(r.text)

print("All data: {}\n".format(json_data['data']['ucompare']))
print("Skills: {}\n".format(json_data['data']['ucompare']['skills']))
print("Professions: {}\n".format(json_data['data']['ucompare']['professions']))
print("Universities: {}\n".format(json_data['data']['ucompare']['universities']))
print("Companies: {}\n".format(json_data['data']['ucompare']['companies']))
print("Profession Levels: {}\n".format(json_data['data']['ucompare']['professionLevels']))
print("Educational Levels: {}\n".format(json_data['data']['ucompare']['educationalLevels']))
print("Degree Types: {}\n".format(json_data['data']['ucompare']['degreeTypes']))
print("Work Experiences: {}\n".format(json_data['data']['ucompare']['workExperiences']))
print("Job Levels: {}".format(json_data['data']['ucompare']['jobLevels']))

