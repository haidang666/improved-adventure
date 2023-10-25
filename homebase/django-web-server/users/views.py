from django.shortcuts import render
import requests

def get_users(request):
    proxy_url = "http://localhost:8080"
    api_url = f"{proxy_url}/api/users"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            users = response.json()
            return render(request, 'users.html', {'users': users})
        else:
            error_message = f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        error_message = f"Request error: {e}"

    return render(request, 'error.html', {'error_message': error_message})