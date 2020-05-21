import requests
import json
from decouple import config

query = {'email': config('EMAIL'), 'password': config('PASSWORD')}

r = requests.post('https://uleague.org/session', json= query)
json_data = json.loads(r.text)

print("All data: {}\n".format(json_data))

mutation = """mutation{
    collateUcompare(input: {
        userData: {
          universityId: 3,
          educationalLevel: 1,
          selectedSkills: [290, 272],
          companyId: 8,
          workExperience: 3,
          jobLevel: 36,
          professionId: 13620,
          professionalLevel: 1,
          degreeType: 5
        }
    }){
    result,
    suggestedCourses{
      id,
      percentageIncrease
        }
    }
}"""

cookies = r.cookies

r = requests.post('https://uleague.org/graphql', json={'query': mutation}, cookies=cookies)
json_data = json.loads(r.text)

print(json_data)
print("\nResult: {}".format(json_data['data']['collateUcompare']['result']))
