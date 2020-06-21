# Pics-galore

Small project to search images using one request from different provider.

Provider available: 

- Flickr : https://www.flickr.com/services/api/flickr.photos.search.html
- Giphy : https://developers.giphy.com/docs/
- Google Images : Crawling

Provider todo:

- Yahoo Images
- DuckDuckGo Images

# Configuration

You need to add a environement file at the root of your project.
This environement file will export all the secret API keys needed for each API requests.

./api_keys.env
```
FLICKR_API_KEY=[YOUR_API_KEY]
GIPHY_API_KEY=[YOUR_API_KEY]
```

# Launch

```
docker-compose up
```


# Test

```
pip install -r requirements.txt
pytest -v
```