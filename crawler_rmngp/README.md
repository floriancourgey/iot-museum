# The French Rmn-GP Crawler

# Run
```console
$ python manage.py rmngp_works # download 15 artworks
$ python manage.py rmngp_works --per_page=100 # download 100 artworks (maximum)
$ python manage.py rmngp_works --per_page=100 --page=2 # download 100 artworks, starting at page 2
```

# Source API
1 API:
- https://api.art.rmngp.fr/v1/ (Classic API) - see `rmngp_works.py`

with docs at https://docs.art.rmngp.fr/
