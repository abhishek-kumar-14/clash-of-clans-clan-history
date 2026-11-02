# Clash of Clans Clan History Lookup

A Python command-line tool that looks up a player's previous clan history and displays the clan names and their locations in a formatted table.

## Features

- Accepts a Clash of Clans player tag (with or without `#`).
- Requests the player's clan history from Clash of Stats.
- Retrieves clan details, including clan name and location, through the Clash of Clans API.
- Displays the results in a readable command-line table.
- Uses concurrent requests when retrieving multiple clan records.

## Example Output

The following screenshot shows an example run of the script:

![Example terminal output](assets/output.png)

## Requirements

- Python 3.8+
- A valid Clash of Clans API key with access to the official API.
- Internet connection.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/clash-of-clans-clan-history.git
cd clash-of-clans-clan-history
```

Install the required Python packages:

```bash
python -m pip install requests tabulate
```

## API Key Configuration

The script uses the official Clash of Clans API to retrieve clan details. You must configure a valid API bearer token in `main.py`.

Find the `authorization` header in `get_status()`:

```python
"authorization": "Bearer `Your API Key Here`"
```

Replace the placeholder with your API token:

```python
"authorization": "Bearer YOUR_ACTUAL_API_TOKEN"
```

Keep your API token private. Do not commit a real token to a public repository. For a public project, load it from an environment variable instead.

You can create/manage API keys through the official developer portal:
https://developer.clashofclans.com/

## Usage

Run the script:

```bash
python main.py
```

When prompted, enter the player's tag:

```text
Enter Player Tag: 2PP
```

The script will attempt to retrieve the player's clan history and print the clan number, clan name, and location.

You can enter the tag with or without the leading `#`.

## Example Table

```text
+------+-----------------+----------+
| No.  | Clan Name       | Location |
+------+-----------------+----------+
| 1    | Example Clan    | Finland  |
+------+-----------------+----------+
```

The example above is illustrative. Actual results depend on the queried player's available history and API responses.

## Limitations

- Clan history may be private, unavailable, or incomplete.
- Clan details require a valid Clash of Clans API key.
- API rate limits and network errors may affect requests.
- The script only displays the clan name and location fields currently implemented.

## Disclaimer

This is an unofficial community project and is not affiliated with, endorsed by, or associated with Supercell or Clash of Clans. Use the relevant APIs in accordance with their terms and rate limits.
