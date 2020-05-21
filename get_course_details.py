import requests
import json

query = """query {
    course(id: 194){
        id,
        title,
        objective,
        howWillItHelp,
        summary,
        description
    }
}"""


r = requests.post('https://uleague.org/graphql', json={'query': query})
json_data = json.loads(r.text)
print(json_data)
