# Danish Discount Food Scraper

A simple web application to search for food discounts in Denmark across major supermarkets (Netto, Rema 1000, Coop365, etc.) and create a shopping list.

## Features

- **Search Offers:** Real-time search for discounts using the Tjek (eTilbudsavis) API.
- **Store Filtering:** Searches across multiple major Danish chains.
- **Shopping List:** Add and remove items from a session-based shopping list.
- **Responsive UI:** Built with Flask, HTMX, and Tailwind CSS for a fast, single-page-like experience.

## Prerequisites

- Python 3.7+
- Internet connection (to query the external API)

## Installation

1. Clone the repository or download the files.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:
   http://127.0.0.1:5000

3. Type in the search box (e.g., "is", "kød", "mælk") and press Enter to see offers.
4. Click "Add to List" on any offer to save it to your shopping list.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS (via CDN), HTMX (via CDN)
- **Data Source:** Tjek Public API (api.etilbudsavis.dk)
