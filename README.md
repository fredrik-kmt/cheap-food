# Danish Discount Food Scraper

A simple, static web application to search for food discounts in Denmark across Netto, Rema 1000, Coop 365, and Spar.

## Features

- **Search Offers:** Real-time search for discounts using the Tjek (eTilbudsavis) API.
- **Store Filtering:** Searches specifically for Netto, Rema 1000, Coop 365, and Spar.
- **Shopping List:** Add items to a local shopping list (saved in your browser).
- **Minimalistic UI:** Clean, responsive design using Tailwind CSS.

## Usage

### Local Development
1. Clone the repository.
2. Open `index.html` in your browser.
   - Note: Some browsers may block API calls from `file://`. It is recommended to use a local server:
   ```bash
   python3 -m http.server
   ```
   Then open `http://localhost:8000`.

### Deployment (GitHub Pages)
1. Push this repository to GitHub.
2. Go to Settings > Pages.
3. Select the `main` branch as the source.
4. Your site will be live!

## Tech Stack

- **Frontend:** HTML, JavaScript (Vanilla), Tailwind CSS (CDN).
- **Data Source:** Tjek Public API.
