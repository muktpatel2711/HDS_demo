import requests
import json

url = "https://api.uat.bapsapps.org/mis/api/v2/AdvanceSearch?pageNumber=1&pageSize=10&keyword=personId&sortBy=asc"

payload = json.dumps({
  "BAPSId": "",
  "address": "",
  "attendanceGrade": None,
  "city": "",
  "culturalRoot": None,
  "dataFlexField": None,
  "defaultMandalId": [
    9,
    16,
    15,
    14,
    20,
    17,
    18,
    1,
    2,
    3,
    4,
    10,
    11,
    5,
    6,
    7,
    8,
    12,
    13
  ],
  "degree": None,
  "departmentId": "0",
  "divisionGeoLevel": 1,
  "email": "",
  "firstName": "",
  "gender": [
    "M",
    "F"
  ],
  "isBusiness": False,
  "isPerson": True,
  "isPrimaryPerson": False,
  "lastName": "",
  "nativePlace": None,
  "otherName": "",
  "overwrittenFunctionalEntityId": 1,
  "pageName": "SP",
  "pendingInfo": None,
  "personId": "",
  "personType": "A",
  "phone": "",
  "profession": "",
  "samaj": None,
  "samparkAssigned": 0,
  "samparkOptOut": None,
  "samparkAssignmentSearchType": "All",
  "samparkStatusType": None,
  "samparkKarykarPairType": None,
  "samparkTags": None,
  "school": None,
  "sevaDepartment": None,
  "sevaGeoLevel": None,
  "sevaRole": None,
  "sevaTag": None,
  "statusType": [
    "A",
    "P",
    "R"
  ],
  "tag": None,
  "tagAssignments": None,
  "totalCount": None,
  "totalPledge": None,
  "zipCode": "",
  "requestToDelete": False
})
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0',
  'Accept': 'application/json',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'sso-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik5vbmUiLCJyZXF1ZXN0b3JpZCI6Ik5vbmUiLCJyZXNvdXJjZXVyaSI6IiIsImFkZGl0aW9uYWxpbmZvIjoiTm9uZSIsIm5vbmNlIjoiTm9uZSIsInVpZCI6ImVkNjhhODUwLWFiNTUtNGI5OS05MTIzLWIzOWRiOWJkYjEwNCIsInNpZCI6IjEzOTBkZmQ4LWY3MWQtNGM5Ny1hNWZmLWVlMGE1MWZmZjM2MSIsImFpZCI6ImM4YTFlYmY3LTVlNGMtNDQ5Yi1hODA0LWEzMGJhZjQ0MjA1MCIsImNpZCI6IjA3NENFRjg0LTBEQjktNEEwNi1BQkY2LTZBRUQ2NDU0MjE5MSIsImF1dGgiOiJ2ZXJpZmllZCIsImZuIjoiSGl0ZXNoIiwibG4iOiJQYXRlbCIsInBpZCI6IjM3OTQiLCJjdCI6ImF0Iiwicm9sZSI6IlVuZGVmaW5lZCIsIm5iZiI6MTcyODg2NjUwMiwiZXhwIjoxNzI4ODczNzAyLCJpYXQiOjE3Mjg4NjY1MDIsImlzcyI6Imh0dHBzOi8vYmFwcy5vcmciLCJhdWQiOiJNZW1iZXJzIn0.SPqGrdBWaXA-AEX4rUus6dQ0qMyLKLB0zBT5FOrROjs',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjU1MzkyIiwiUm9sZUlkIjoiMSIsIlVzZXJEaXZpc2lvbklkIjoiMSIsIlVzZXJHZW9MZXZlbElkIjoiMSIsIlVzZXJEZXBhcnRtZW50SWQiOiIxIiwiVXNlclBlcnNvbklkIjoiMzc5NCIsIldpbmciOiJlIiwiVXNlclBlcnNvbk1hc3RlckVudGl0eUlkIjoiMTA0OTMiLCJVc2VyRGVwYXJ0bWVudElzQWRtaW4iOiJUcnVlIiwiSXNMZWFkUm9sZSI6IlRydWUiLCJJc0NvTGVhZFJvbGUiOiJUcnVlIiwiUG9zaXRpb25JZCI6IjU1MzkyIiwiUG9zaXRpb25FbnRpdHlJZCI6IjEiLCJTYXRzYW5nQWN0aXZpdHkiOiJGYWxzZSIsIm5iZiI6MTcyODg2NjUwMiwiZXhwIjoxNzI4OTUyOTAyLCJpYXQiOjE3Mjg4NjY1MDJ9.Lr_j3YGGghzVAOjmWAPir94YPtOrChg_3mkXejQt15Q',
  'CultureInfo': 'EN',
  'Content-Type': 'application/json',
  'Origin': 'https://uat.baps.dev',
  'Connection': 'keep-alive',
  'Referer': 'https://uat.baps.dev/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'Priority': 'u=0',
  'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

json_data = response.json()
print(json_data)

personId = json_data["data"][0]["personId"]

print(personId)




