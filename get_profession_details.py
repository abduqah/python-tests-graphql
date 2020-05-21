import requests
import json

query = """query {
    profession(id: 13620){
        id,
        title,
        averageSalaryEu,
        averageSalaryUs,
        summary,
        roleDescription
    }
}"""


r = requests.post('https://uleague.org/graphql', json={'query': query})
json_data = json.loads(r.text)
print(json_data)
