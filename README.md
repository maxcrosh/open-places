# Web-scraping template

[**Scrapy documentation**](https://docs.scrapy.org//)

A project to extract GeoJSON from the web focusing on websites that have 'store locator' pages like restaurants, gas stations, retailers, etc. Each chain has its own bit of software to extract useful information from their site (a "spider"). Each spider can be individually configured to throttle request rate to act as a good citizen on the Internet. 

The project is built using [`scrapy`](https://scrapy.org/), a Python-based web scraping framework. Each target website gets its own [spider](https://doc.scrapy.org/en/latest/topics/spiders.html), which does the work of extracting interesting details about locations and outputting results in a useful format.

## Adding a spider

To scrape a new website for locations, you'll want to create a new spider. You can copy from existing spiders or start from a blank, but the result is always a Python class that has a `process()` function that `yield`s [`GeojsonPointItem`s](https://github.com/iandees/all-the-places/blob/master/locations/items.py). The Scrapy framework does the work of outputting the GeoJSON based on these objects that the spider generates.

## Development setup

To get started, you'll want to install the dependencies for this project.

1. This project uses `pipenv` to handle dependencies and virtual environments. To get started, make sure you have [`pipenv` installed](https://github.com/kennethreitz/pipenv#installation).

2. With `pipenv` installed, make sure you have the `all-the-places` repository checked out

   ```
   git clone git@github.com:maxcrosh/open-places.git
   ```

3. Then you can install the dependencies for the project

   ```
   cd open-places
   pipenv install
   ```

1. After dependencies are installed, make sure you can run the `scrapy` command without error

   ```
   pipenv run scrapy
   ```

1. If `pipenv run scrapy` ran without complaining, then you have a functional `scrapy` setup and are ready to write a scraper.

## Create a new spider
