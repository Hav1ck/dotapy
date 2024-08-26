from requests import get

GITHUB_REPO = "Hav1ck/timing_checker"  # Define the repository and current version
CURRENT_VERSION = "v1.0.0"  # Current version of the application

def get_latest_release():
    # Fetches the latest release tag from the GitHub repository.
    # Returns the tag name of the latest release or None if the request fails.
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    response = get(url)
    
    if response.status_code == 200:
        latest_release = response.json()
        return latest_release["tag_name"]
    else:
        print(f"Failed to fetch the latest release. Status code: {response.status_code}")
        return None

def check_for_update():
    # Compares the current version with the latest release version.
    # Prints messages indicating if an update is available or if the current version is up to date.
    latest_version = get_latest_release()
    
    if latest_version:
        print(f"Latest version on GitHub: {latest_version}")
        if latest_version != CURRENT_VERSION:
            print("Update available!")
            print(f"Current version: {CURRENT_VERSION}")
            print(f"New version: {latest_version}")
        else:
            print("You are using the latest version.")
    else:
        print("Could not retrieve the latest version.")

if __name__ == "__main__":
    check_for_update()
