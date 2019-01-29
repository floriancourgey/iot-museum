# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Admin Artwork fieldesets (now displays created_datetime and edited_datetime)
- Freeze requirements version
- Heroku demo (with whitenoise, gunicorn, Procfile, env vars, runtime.txt...)
### Changed
- admin CSS in its own file
- Artwork.author is now optional (default='' and blank=True)

## [1.2.1] - 2019-01-29
### Fixed
- Added Pillow as a pip dependency, required by Django ImageField

## [1.2.0] - 2019-01-28
### Added
- Artwork date: "display_date" is a string not an actual timestamp. So it can be "Sept 1789", "Between -500 and -490", etc
- RmnGP crawler updated to handle updates
- New artworks, the db now contains 197 artworks from the RmnGP
- Admin edit artwork features a "Fetch more from this author from the RmnGP" link
### Changed
- RmnGP crawler updated with fields origin_id and date_display
### Fixed
- Artwork history doesn't contain the current arwtork, so the "Previous" button doesn't need to be clicked twice

## [1.1.0] - 2019-01-25
### Added
- Upload a local image
- Bootstrap 4 on every Admin page
- On RmnGP admin, feature "Suggested authors"

### Changed
- New Frontend with VueJS and axios

## [1.0.0] - 2019-01-15
### Added
- First release: fetches a new artwork from db along with artist and title
- Play/Pause
- Previous/Next
- Reset all `timesPlayed` to 0
- Admin GUI
- RmnGP crawler
- Basic unit testing with `django.test` and Travis CI
