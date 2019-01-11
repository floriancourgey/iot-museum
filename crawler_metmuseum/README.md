# The US NYC Met Museum Crawler

Crawlers are located in `management/commands` and can be called from the root folder with `python manage.py filename`.

2 APIs:
- https://collectionapi.metmuseum.org/public/collection/v1/objects (Classic API) - see `metmuseum_objects.py`
- https://www.metmuseum.org/api/collection/collectionlisting (used on https://www.metmuseum.org/art/collection/search via Angular) - see `metmuseum_highlights.py`
