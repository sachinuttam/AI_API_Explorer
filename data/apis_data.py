"""
apis_data.py
-------------
A curated database of real, publicly documented APIs across many topics.
Each entry is used by the search engine in search_utils.py to find the
best matching APIs for whatever a user searches for.

Fields:
    name         - display name of the API
    category     - broad topic/category
    description  - one-line description of what the API does
    docs_url     - link to the official documentation / homepage
    tags         - list of keywords used for search matching
    icon         - emoji shown on the card
    free_tier    - short note on free-tier availability
"""

APIS = [
    # ------------------------------------------------------------------ Weather
    {
        "name": "OpenWeatherMap API",
        "category": "Weather",
        "description": "Current weather, forecasts, and historical weather data for any location worldwide.",
        "docs_url": "https://openweathermap.org/api",
        "tags": ["weather", "forecast", "climate", "temperature", "rain", "meteorology"],
        "icon": "☁️",
        "free_tier": "Free tier available",
    },
    {
        "name": "WeatherAPI.com",
        "category": "Weather",
        "description": "Real-time weather, forecast, astronomy, and air quality data with a simple REST API.",
        "docs_url": "https://www.weatherapi.com/docs/",
        "tags": ["weather", "forecast", "air quality", "astronomy", "climate"],
        "icon": "🌦️",
        "free_tier": "Free tier available",
    },
    {
        "name": "NOAA Weather API",
        "category": "Weather",
        "description": "Official US government weather data, alerts, and forecasts from the National Weather Service.",
        "docs_url": "https://www.weather.gov/documentation/services-web-api",
        "tags": ["weather", "government", "alerts", "forecast", "usa"],
        "icon": "🌤️",
        "free_tier": "Completely free",
    },

    # -------------------------------------------------------------------- News
    {
        "name": "NewsAPI",
        "category": "News",
        "description": "Search and retrieve live headlines and articles from thousands of news sources worldwide.",
        "docs_url": "https://newsapi.org/docs",
        "tags": ["news", "headlines", "articles", "media", "journalism"],
        "icon": "📰",
        "free_tier": "Free tier available",
    },
    {
        "name": "The Guardian Open Platform",
        "category": "News",
        "description": "Access The Guardian's full article archive and content through a free, open API.",
        "docs_url": "https://open-platform.theguardian.com/documentation/",
        "tags": ["news", "articles", "journalism", "media"],
        "icon": "🗞️",
        "free_tier": "Free tier available",
    },
    {
        "name": "GNews API",
        "category": "News",
        "description": "Simple JSON API for searching and retrieving news articles from around the world.",
        "docs_url": "https://gnews.io/docs/v4",
        "tags": ["news", "headlines", "search", "articles"],
        "icon": "📡",
        "free_tier": "Free tier available",
    },

    # ---------------------------------------------------------------- Finance
    {
        "name": "Alpha Vantage",
        "category": "Finance",
        "description": "Stock market data, forex rates, and technical indicators for financial analysis.",
        "docs_url": "https://www.alphavantage.co/documentation/",
        "tags": ["finance", "stocks", "market", "trading", "investing", "forex"],
        "icon": "💰",
        "free_tier": "Free tier available",
    },
    {
        "name": "IEX Cloud",
        "category": "Finance",
        "description": "Real-time and historical stock market data, company financials, and market news.",
        "docs_url": "https://iexcloud.io/docs/api/",
        "tags": ["finance", "stocks", "market", "trading", "investing"],
        "icon": "📈",
        "free_tier": "Free tier available",
    },
    {
        "name": "Yahoo Finance API",
        "category": "Finance",
        "description": "Stock quotes, historical prices, and financial news via Yahoo Finance data.",
        "docs_url": "https://www.yahoofinanceapi.com/",
        "tags": ["finance", "stocks", "market", "quotes", "investing"],
        "icon": "💹",
        "free_tier": "Free tier available",
    },

    # ---------------------------------------------------------- AI & Machine Learning
    {
        "name": "OpenAI API",
        "category": "AI & Machine Learning",
        "description": "Access GPT language models, image generation, and embeddings for building AI apps.",
        "docs_url": "https://platform.openai.com/docs",
        "tags": ["ai", "ml", "machine learning", "gpt", "llm", "chatbot", "nlp"],
        "icon": "🤖",
        "free_tier": "Paid, free trial credits",
    },
    {
        "name": "Anthropic Claude API",
        "category": "AI & Machine Learning",
        "description": "Build with Claude — Anthropic's family of large language models for chat, coding, and analysis.",
        "docs_url": "https://docs.claude.com",
        "tags": ["ai", "ml", "machine learning", "claude", "llm", "chatbot", "nlp"],
        "icon": "🧠",
        "free_tier": "Paid, free trial credits",
    },
    {
        "name": "Hugging Face Inference API",
        "category": "AI & Machine Learning",
        "description": "Run thousands of open-source machine learning models for NLP, vision, and audio via API.",
        "docs_url": "https://huggingface.co/docs/api-inference/index",
        "tags": ["ai", "ml", "machine learning", "nlp", "models", "huggingface"],
        "icon": "🤗",
        "free_tier": "Free tier available",
    },
    {
        "name": "Google Cloud Vision API",
        "category": "AI & Machine Learning",
        "description": "Detect objects, faces, text, and landmarks in images using Google's vision models.",
        "docs_url": "https://cloud.google.com/vision/docs",
        "tags": ["ai", "ml", "vision", "image recognition", "ocr", "google"],
        "icon": "👁️",
        "free_tier": "Free tier available",
    },

    # -------------------------------------------------------- Maps & Geolocation
    {
        "name": "Google Maps Platform",
        "category": "Maps & Geolocation",
        "description": "Maps, directions, places search, and geocoding for location-based applications.",
        "docs_url": "https://developers.google.com/maps",
        "tags": ["maps", "location", "geocoding", "directions", "places", "gps"],
        "icon": "🗺️",
        "free_tier": "Free tier available",
    },
    {
        "name": "Mapbox API",
        "category": "Maps & Geolocation",
        "description": "Customizable maps, navigation, and geospatial data for web and mobile apps.",
        "docs_url": "https://docs.mapbox.com/",
        "tags": ["maps", "location", "geocoding", "navigation", "geospatial"],
        "icon": "📍",
        "free_tier": "Free tier available",
    },
    {
        "name": "OpenCage Geocoding API",
        "category": "Maps & Geolocation",
        "description": "Convert addresses into coordinates and coordinates into addresses (geocoding).",
        "docs_url": "https://opencagedata.com/api",
        "tags": ["maps", "geocoding", "location", "address", "coordinates"],
        "icon": "🧭",
        "free_tier": "Free tier available",
    },

    # ------------------------------------------------------------- Movies & TV
    {
        "name": "TMDB API",
        "category": "Movies & TV",
        "description": "Movie, TV show, and cast/crew data including posters, ratings, and release info.",
        "docs_url": "https://developer.themoviedb.org/docs",
        "tags": ["movies", "tv", "films", "entertainment", "actors", "ratings"],
        "icon": "🎬",
        "free_tier": "Completely free",
    },
    {
        "name": "OMDb API",
        "category": "Movies & TV",
        "description": "Simple API for retrieving movie and series information, plot summaries, and ratings.",
        "docs_url": "https://www.omdbapi.com/",
        "tags": ["movies", "tv", "films", "ratings", "plot"],
        "icon": "🍿",
        "free_tier": "Free tier available",
    },

    # ------------------------------------------------------------------- Music
    {
        "name": "Spotify Web API",
        "category": "Music",
        "description": "Access music catalog data, playlists, artists, albums, and audio features.",
        "docs_url": "https://developer.spotify.com/documentation/web-api",
        "tags": ["music", "songs", "playlists", "artists", "audio", "streaming"],
        "icon": "🎵",
        "free_tier": "Free with Spotify account",
    },
    {
        "name": "Deezer API",
        "category": "Music",
        "description": "Music catalog, playlists, and streaming previews from Deezer's library.",
        "docs_url": "https://developers.deezer.com/api",
        "tags": ["music", "songs", "playlists", "streaming", "audio"],
        "icon": "🎧",
        "free_tier": "Completely free",
    },

    # ----------------------------------------------------------------- Sports
    {
        "name": "TheSportsDB API",
        "category": "Sports",
        "description": "Free sports database with team info, player stats, schedules, and league data.",
        "docs_url": "https://www.thesportsdb.com/api.php",
        "tags": ["sports", "teams", "players", "scores", "leagues"],
        "icon": "⚽",
        "free_tier": "Free tier available",
    },
    {
        "name": "football-data.org",
        "category": "Sports",
        "description": "Live scores, fixtures, and standings for major football/soccer competitions worldwide.",
        "docs_url": "https://www.football-data.org/",
        "tags": ["sports", "football", "soccer", "scores", "fixtures", "standings"],
        "icon": "🏆",
        "free_tier": "Free tier available",
    },
    {
        "name": "Ergast F1 API",
        "category": "Sports",
        "description": "Historical Formula 1 racing data including race results, drivers, and standings.",
        "docs_url": "https://ergast.com/mrd/",
        "tags": ["sports", "formula 1", "f1", "racing", "motorsport"],
        "icon": "🏎️",
        "free_tier": "Completely free",
    },

    # --------------------------------------------------------------- Social Media
    {
        "name": "YouTube Data API",
        "category": "Social Media",
        "description": "Search videos, retrieve channel stats, and manage playlists on YouTube.",
        "docs_url": "https://developers.google.com/youtube/v3",
        "tags": ["social media", "youtube", "videos", "channels", "google"],
        "icon": "📺",
        "free_tier": "Free tier available",
    },
    {
        "name": "Reddit API",
        "category": "Social Media",
        "description": "Access posts, comments, and subreddit data from Reddit communities.",
        "docs_url": "https://www.reddit.com/dev/api/",
        "tags": ["social media", "reddit", "posts", "comments", "community"],
        "icon": "👽",
        "free_tier": "Free with account",
    },

    # -------------------------------------------------------------------- Books
    {
        "name": "Google Books API",
        "category": "Books",
        "description": "Search millions of books, get descriptions, covers, and preview links.",
        "docs_url": "https://developers.google.com/books",
        "tags": ["books", "reading", "library", "literature", "google"],
        "icon": "📚",
        "free_tier": "Completely free",
    },
    {
        "name": "Open Library API",
        "category": "Books",
        "description": "Free, open access to book metadata, covers, and reading lists from the Internet Archive.",
        "docs_url": "https://openlibrary.org/developers/api",
        "tags": ["books", "reading", "library", "literature", "open source"],
        "icon": "📖",
        "free_tier": "Completely free",
    },

    # --------------------------------------------------------------- Food & Recipes
    {
        "name": "Edamam Recipe API",
        "category": "Food & Recipes",
        "description": "Search recipes with detailed nutrition analysis based on ingredients and diet.",
        "docs_url": "https://developer.edamam.com/",
        "tags": ["food", "recipes", "cooking", "nutrition", "diet"],
        "icon": "🍔",
        "free_tier": "Free tier available",
    },
    {
        "name": "Spoonacular API",
        "category": "Food & Recipes",
        "description": "Recipe search, meal planning, and grocery/ingredient data for food apps.",
        "docs_url": "https://spoonacular.com/food-api",
        "tags": ["food", "recipes", "cooking", "meal planning", "ingredients"],
        "icon": "🍳",
        "free_tier": "Free tier available",
    },

    # ------------------------------------------------------------------- Games
    {
        "name": "PokéAPI",
        "category": "Games",
        "description": "Comprehensive RESTful API with data on every Pokémon, move, and ability.",
        "docs_url": "https://pokeapi.co/",
        "tags": ["games", "pokemon", "gaming", "fun"],
        "icon": "🎮",
        "free_tier": "Completely free",
    },
    {
        "name": "RAWG Video Games API",
        "category": "Games",
        "description": "Database of over 500,000 video games with details, ratings, and screenshots.",
        "docs_url": "https://rawg.io/apidocs",
        "tags": ["games", "video games", "gaming", "ratings"],
        "icon": "🕹️",
        "free_tier": "Free tier available",
    },

    # ------------------------------------------------------------ Cryptocurrency
    {
        "name": "CoinGecko API",
        "category": "Cryptocurrency",
        "description": "Live cryptocurrency prices, market cap, trading volume, and historical data.",
        "docs_url": "https://www.coingecko.com/en/api",
        "tags": ["crypto", "cryptocurrency", "bitcoin", "blockchain", "finance", "prices"],
        "icon": "🪙",
        "free_tier": "Completely free",
    },
    {
        "name": "CoinMarketCap API",
        "category": "Cryptocurrency",
        "description": "Cryptocurrency market data, rankings, and price conversion tools.",
        "docs_url": "https://coinmarketcap.com/api/",
        "tags": ["crypto", "cryptocurrency", "bitcoin", "blockchain", "finance", "market cap"],
        "icon": "₿",
        "free_tier": "Free tier available",
    },

    # ---------------------------------------------------------------- Translation
    {
        "name": "DeepL API",
        "category": "Translation",
        "description": "High-quality, natural-sounding machine translation across dozens of languages.",
        "docs_url": "https://www.deepl.com/docs-api",
        "tags": ["translation", "language", "text", "localization"],
        "icon": "🌐",
        "free_tier": "Free tier available",
    },
    {
        "name": "LibreTranslate API",
        "category": "Translation",
        "description": "Free and open-source machine translation API you can even self-host.",
        "docs_url": "https://libretranslate.com/docs/",
        "tags": ["translation", "language", "text", "open source"],
        "icon": "🗣️",
        "free_tier": "Completely free",
    },

    # ------------------------------------------------------------ Space & Science
    {
        "name": "NASA Open APIs",
        "category": "Space & Science",
        "description": "Astronomy picture of the day, Mars rover photos, near-earth asteroid data, and more.",
        "docs_url": "https://api.nasa.gov/",
        "tags": ["space", "science", "nasa", "astronomy", "mars", "planets"],
        "icon": "🚀",
        "free_tier": "Completely free",
    },
    {
        "name": "Open Notify (ISS API)",
        "category": "Space & Science",
        "description": "Real-time location of the International Space Station and astronauts currently in space.",
        "docs_url": "http://open-notify.org/Open-Notify-API/",
        "tags": ["space", "science", "iss", "astronauts", "astronomy"],
        "icon": "🛰️",
        "free_tier": "Completely free",
    },

    # ---------------------------------------------------------------- Fun & Random
    {
        "name": "Chuck Norris Jokes API",
        "category": "Fun & Random",
        "description": "Random Chuck Norris jokes delivered as simple JSON, great for testing and fun projects.",
        "docs_url": "https://api.chucknorris.io/",
        "tags": ["fun", "jokes", "random", "entertainment"],
        "icon": "🎉",
        "free_tier": "Completely free",
    },
    {
        "name": "Giphy API",
        "category": "Fun & Random",
        "description": "Search and share GIFs and stickers from Giphy's massive animated library.",
        "docs_url": "https://developers.giphy.com/",
        "tags": ["fun", "gifs", "memes", "entertainment", "stickers"],
        "icon": "🎊",
        "free_tier": "Free tier available",
    },
    {
        "name": "Unsplash API",
        "category": "Fun & Random",
        "description": "Access millions of free high-resolution stock photos for apps and websites.",
        "docs_url": "https://unsplash.com/documentation",
        "tags": ["photos", "images", "stock photos", "fun", "design"],
        "icon": "🖼️",
        "free_tier": "Free tier available",
    },

    # --------------------------------------------------------------- Communication
    {
        "name": "Twilio API",
        "category": "Communication",
        "description": "Send SMS, make calls, and build messaging or voice features into your app.",
        "docs_url": "https://www.twilio.com/docs",
        "tags": ["communication", "sms", "messaging", "voice", "calls"],
        "icon": "📩",
        "free_tier": "Paid, free trial credits",
    },
    {
        "name": "SendGrid API",
        "category": "Communication",
        "description": "Reliable transactional and marketing email delivery for developers.",
        "docs_url": "https://www.twilio.com/docs/sendgrid",
        "tags": ["communication", "email", "messaging", "marketing"],
        "icon": "✉️",
        "free_tier": "Free tier available",
    },

    # -------------------------------------------------------------------- Payments
    {
        "name": "Stripe API",
        "category": "Payments",
        "description": "Accept online payments, manage subscriptions, and handle billing for your app.",
        "docs_url": "https://stripe.com/docs/api",
        "tags": ["payments", "billing", "ecommerce", "subscriptions", "checkout"],
        "icon": "💳",
        "free_tier": "Pay per transaction",
    },
    {
        "name": "PayPal API",
        "category": "Payments",
        "description": "Integrate PayPal checkout, payouts, and invoicing into websites and apps.",
        "docs_url": "https://developer.paypal.com/docs/api/overview/",
        "tags": ["payments", "billing", "ecommerce", "checkout", "invoicing"],
        "icon": "💵",
        "free_tier": "Pay per transaction",
    },

    # ------------------------------------------------------------------ E-commerce
    {
        "name": "Shopify Admin API",
        "category": "E-commerce",
        "description": "Manage products, orders, and customers for Shopify-powered online stores.",
        "docs_url": "https://shopify.dev/docs/api/admin",
        "tags": ["ecommerce", "shopping", "store", "products", "orders"],
        "icon": "🛒",
        "free_tier": "Free with Shopify account",
    },
    {
        "name": "eBay API",
        "category": "E-commerce",
        "description": "Search listings, prices, and product data across eBay's global marketplace.",
        "docs_url": "https://developer.ebay.com/docs",
        "tags": ["ecommerce", "shopping", "marketplace", "listings", "auctions"],
        "icon": "🏷️",
        "free_tier": "Free tier available",
    },

    # ------------------------------------------------------------------- General
    {
        "name": "REST Countries API",
        "category": "General / Reference",
        "description": "Detailed information about every country: capital, population, flag, currency, and more.",
        "docs_url": "https://restcountries.com/",
        "tags": ["countries", "reference", "geography", "general", "world"],
        "icon": "🌍",
        "free_tier": "Completely free",
    },
    {
        "name": "Exchangerate.host",
        "category": "General / Reference",
        "description": "Free currency exchange rates and conversion API updated in real time.",
        "docs_url": "https://exchangerate.host/",
        "tags": ["currency", "exchange rate", "finance", "conversion", "money"],
        "icon": "💱",
        "free_tier": "Completely free",
    },
    {
        "name": "GitHub REST API",
        "category": "Developer Tools",
        "description": "Manage repositories, issues, pull requests, and users on GitHub programmatically.",
        "docs_url": "https://docs.github.com/en/rest",
        "tags": ["developer", "github", "code", "repositories", "git"],
        "icon": "🐙",
        "free_tier": "Free with account",
    },
    {
        "name": "JSONPlaceholder",
        "category": "Developer Tools",
        "description": "Free fake REST API for testing and prototyping frontend and backend apps.",
        "docs_url": "https://jsonplaceholder.typicode.com/",
        "tags": ["developer", "testing", "prototyping", "fake data", "rest"],
        "icon": "🧪",
        "free_tier": "Completely free",
    },
]
