---

### 1. **Fetching Data**
Decide whether you'll use an API or scrape a website. Here's how you can practice each:

#### **Using an API**:
- **Task**: Learn how to make an API request.
- Example:
  ```python
  import requests

  # Replace with the API URL for LCK data
  url = "https://example.com/lck/matches"
  
  # Send a GET request
  response = requests.get(url)
  
  # Check response
  if response.status_code == 200:
      print(response.json())  # Practice exploring the JSON structure
  else:
      print(f"Failed to fetch data: {response.status_code}")
  ```
- **Challenge**: 
  - Read the API documentation.
  - Figure out how to filter matches by date or week using query parameters.

---

#### **Web Scraping**:
- **Task**: Practice fetching HTML content from a website.
- Example:
  ```python
  from bs4 import BeautifulSoup
  import requests

  url = "https://example.com/lck-results"
  response = requests.get(url)
  
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
      print(soup.prettify())  # Practice exploring the HTML structure
  else:
      print("Failed to fetch the webpage")
  ```
- **Challenge**:
  - Identify the HTML tags and classes/IDs that contain match results.

---

### 2. **Processing the Data**
Now that you have data, focus on parsing and filtering.

#### **For APIs (JSON Data)**:
- **Task**: Practice extracting specific fields.
- Example:
  ```python
  data = {
      "matches": [
          {"team1": "T1", "team2": "DK", "date": "2025-01-20", "score": "2-1"},
          {"team1": "GEN", "team2": "HLE", "date": "2025-01-21", "score": "2-0"}
      ]
  }

  # Filter matches for a specific date range
  for match in data["matches"]:
      if "2025-01-20" <= match["date"] <= "2025-01-26":
          print(match)
  ```
- **Challenge**:
  - Write a function that filters matches based on a given week.

---

#### **For Web Scraping (HTML Data)**:
- **Task**: Extract specific elements from HTML.
- Example:
  ```python
  html = """
  <div class="match">
      <span class="team1">T1</span> vs <span class="team2">DK</span>
      <span class="score">2-1</span>
  </div>
  """

  soup = BeautifulSoup(html, "html.parser")
  
  # Extract match info
  for match in soup.find_all("div", class_="match"):
      team1 = match.find("span", class_="team1").text
      team2 = match.find("span", class_="team2").text
      score = match.find("span", class_="score").text
      print(f"{team1} vs {team2}: {score}")
  ```
- **Challenge**:
  - Handle multiple matches dynamically.

---

### 3. **Displaying the Results**
Once you have the filtered data, practice presenting it.

#### **Task**: Format and print results cleanly.
- Example:
  ```python
  matches = [
      {"team1": "T1", "team2": "DK", "date": "2025-01-20", "score": "2-1"},
      {"team1": "GEN", "team2": "HLE", "date": "2025-01-21", "score": "2-0"}
  ]

  for match in matches:
      print(f"{match['date']}: {match['team1']} vs {match['team2']} - {match['score']}")
  ```
- **Challenge**:
  - Use `tabulate` or similar libraries to display results in a table.

---

### 4. **Organizing the Script**
- Break down the script into **functions**:
  - `fetch_data()`: Fetches data from the API or website.
  - `process_data()`: Filters matches by the week.
  - `display_results()`: Formats and prints the results.

- **Challenge**:
  - Pass data between these functions and ensure they are reusable.

---

### 5. **Handling User Input**
- **Task**: Prompt the user for input (e.g., a week number or date range).
- Example:
  ```python
  week = input("Enter the week number (e.g., 1, 2, 3): ")
  print(f"Fetching results for Week {week}...")
  ```
- **Challenge**:
  - Translate the week number into a date range.

---

### 6. **Error Handling and Validation**
- Practice handling:
  - API errors (e.g., invalid response).
  - Invalid user input.
- Example:
  ```python
  try:
      week = int(input("Enter the week number: "))
      if week < 1 or week > 10:
          raise ValueError("Week number must be between 1 and 10")
  except ValueError as e:
      print(f"Invalid input: {e}")
  ```

---

### 7. **Testing and Debugging**
- Use **print statements** or a debugger to test each part.
- Example:
  ```python
  print("Debugging data:", data)
  ```

---