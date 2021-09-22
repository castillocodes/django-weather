from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=6BB719CD-EA41-4E99-A4CB-3A35EF4E0E4D")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 to 50 = Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 to 100 = Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 to 150 = Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "unhealthyforsensitivegroups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 to 200 = Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 to 300 = Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "300+ = Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75251&distance=5&API_KEY=6BB719CD-EA41-4E99-A4CB-3A35EF4E0E4D")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 to 50 = Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 to 100 = Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 to 150 = Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "unhealthyforsensitivegroups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 to 200 = Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 to 300 = Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "300+ = Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description, 
            'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})