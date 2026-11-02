import requests
import concurrent.futures
from tabulate import tabulate

def get_status(url):
    headers = {
        "Accept": "application/json",
        "authorization": "Bearer `Your API Key Here`"
    }
    response = requests.get(url=url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()

def get_urls(urls):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_status, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            try:
                results.append(future.result())
            except requests.RequestException as e:
                print(f"Request failed: {e}")
    return results

def get_clans_history(tag):
    tag = tag.strip().lstrip("#").upper()

    try:
        response = requests.get(
            f"https://api.clashofstats.com/players/{tag}/history/clans",
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return {"success": False, "error": str(e)}

    if data.get("error"):
        return {"success": False, "error": "Clan history is private or unavailable"}

    clans_map = data.get("clansMap", {})

    clan_urls = [
        f"https://api.clashofclans.com/v1/clans/%23{clan_tag.lstrip('#')}"
        for clan_tag in clans_map.keys()
    ]

    clans_result = get_urls(clan_urls)

    clans_info = [
        {
            "name": clan.get("name", "Unknown"),
            "location": clan.get("location", {}).get("name", "Unknown")
        }
        for clan in clans_result
    ]

    return {"success": True, "clans_info": clans_info}

def display_clans_history(result):
    if not result.get("success"):
        print(f"\nError: {result.get('error', 'Unknown error')}")
        return

    clans = result.get("clans_info", [])

    if not clans:
        print("\nNo clan history found.")
        return

    headers = ["No.", "Clan Name", "Location"]
    rows = [
        [index, clan["name"], clan["location"]]
        for index, clan in enumerate(clans, start=1)
    ]

    print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    tag = input("Enter Player Tag: ").strip()

    if not tag:
        print("Player tag cannot be empty.")
    else:
        result = get_clans_history(tag)
        display_clans_history(result)