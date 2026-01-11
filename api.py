import requests

BASE_URL = "https://api.etilbudsavis.dk/v2"
# Default location (Copenhagen) for proximity search
DEFAULT_LAT = 55.676098
DEFAULT_LNG = 12.568337
DEFAULT_RADIUS = 10000

# Dealer IDs for Netto, Rema 1000, Spar, Coop 365
TARGET_DEALER_IDS = ["9ba51", "11deC", "88ddE", "DWZE1w"]

def fetch_offers(query=None, limit=20):
    """
    Fetches offers from the API.
    If query is provided, uses the search endpoint.
    Otherwise, uses the list endpoint (though list endpoint might need params to show relevant stuff).
    """
    params = {
        'limit': limit,
        'r_lat': DEFAULT_LAT,
        'r_lng': DEFAULT_LNG,
        'r_radius': DEFAULT_RADIUS,
        'dealer_ids': ",".join(TARGET_DEALER_IDS)
    }

    if query:
        url = f"{BASE_URL}/offers/search"
        params['query'] = query
    else:
        url = f"{BASE_URL}/offers"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching offers: {e}")
        return []

def format_offer(offer):
    """
    Helper to extract relevant fields for the UI.
    """
    pricing = offer.get('pricing', {})
    branding = offer.get('branding', {})
    images = offer.get('images', {})

    return {
        'id': offer.get('id'),
        'heading': offer.get('heading'),
        'description': offer.get('description'),
        'price': pricing.get('price'),
        'currency': pricing.get('currency'),
        'store_name': branding.get('name'),
        'store_logo': branding.get('logo'),
        'image': images.get('view') or images.get('thumb'),
        'run_from': offer.get('run_from'),
        'run_till': offer.get('run_till'),
    }
