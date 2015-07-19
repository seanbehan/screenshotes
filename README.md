# Screenshot.es

Webservice to snap full size screenshots of websites.

### Usage

The API can be used from within an application or straight from the command line.

Make a GET request to http://www.screenshot.es/screenshot?url=example.com replacing the url parameter with the URL you wish to capture.

The JSON response will contain meta information about the page and the location of the screenshot png file.

Images are saved on the server for a short period of time and are randomly deleted after each request.

```
curl "http://www.screenshot.es/screenshot?url=http://example.com"
```

Will return...

```json
{
  "title": "Example Domain",
  "url": "https://example.com/",
  "screenshot": {
    "url": "https://www.screenshot.es/static/screenshots/c984d06aafbecf6bc55569f964148ea3.png",
    "taken_at": "2014-12-14 22:31:16.757027",
    "size": 21004
  }
}
```

### Additional Arguments

You can set width, height and background parameters.

The width and height set the dimensions of the browser window before snapping the screenshot.

The background param sets the background color. By default, the background is transparent. The background color must be a valid CSS color. E.g., white, black, #fefefe... etc.

```
curl "http://www.screenshot.es/screenshot?url=http://example.com&width=200&height=200&background=white"
```
