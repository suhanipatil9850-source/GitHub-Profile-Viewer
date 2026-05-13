import requests

def github_profile(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n?? GitHub Profile\n")
        print("Name:", data.get("name"))
        print("Username:", data.get("login"))
        print("Bio:", data.get("bio"))
        print("Followers:", data.get("followers"))
        print("Following:", data.get("following"))
        print("Public Repos:", data.get("public_repos"))
        print("Profile URL:", data.get("html_url"))

    else:
        print("? User not found!")

username = input("Enter GitHub username: ")
github_profile(username)
