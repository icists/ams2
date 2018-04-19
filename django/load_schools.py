import json

from accounts.models import School

with open('schools.json') as file:
    schools = json.loads(file.read())
    for school in schools:
        try:
            School.objects.create(
                name=school['name'],
                country=school['alpha_two_code'],
            )
        except Exception as e:
            print(e)
