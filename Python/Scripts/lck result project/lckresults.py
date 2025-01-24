# import requests

# url = "https://lol.fandom.com/wiki/LCK/2025_Season/Cup"

# response = requests.get(url)

# if response.status_code == 200:
#     print("reponse.text")
# else:
#     print("failed to get the data : [", response.status_code, "]")

# from leaguepedia_parser import LeaguepediaParser

# # Initialize the parser
# parser = LeaguepediaParser()

# # Fetch matches
# matches = parser.get_matches(tournament="LCK 2025 Cup 1")

# # Display the results
# for match in matches:
#     print(f"{match['team1']} vs {match['team2']}: {match['result']}")
