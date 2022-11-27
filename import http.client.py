import http.client

conn = http.client.HTTPSConnection("nutritionix-api.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "8249f77f64msh0340c24930fb03ap11c7dbjsnb0e487646a16",
    'X-RapidAPI-Host': "nutritionix-api.p.rapidapi.com"
    }

conn.request("GET", "/v1_1/search/cheddar%20cheese?fields=item_name%2Cnf_calories%2Cnf_total_fat", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))