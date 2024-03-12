response_status = int(input("Response Status: "))
if response_status == 400:
    print("Bad Request")
elif response_status == 404:
    print("Not found")
elif response_status == 403:
    print("Forbidden")

result = ""
match response_status:
    case 400:
        result = "Bad Request"
    case 404:
        result = "Not found"
    case 403:
        result = "Forbidden"
    case _:
        result = "Error"
    

print(result)