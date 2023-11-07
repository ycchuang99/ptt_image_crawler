# PTT Image Crawler

## Installation

To get started, install the required dependencies using the following command:

```bash
pip install -r requirement.txt
```

## Usage

You can use the provided Python script to scrape images from a PTT board. Use the following command to see the available options:

```bash
python main.py -h
```

This will display the following usage information:

```bash
usage: main.py [-h] [--board BOARD] [--pages PAGES]

optional arguments:
  -h, --help            show this help message and exit
  --board BOARD, -b BOARD   Choose a PTT board, e.g., Food
  --pages PAGES, -p PAGES   Set the maximum number of pages, default is all
```

## Example

To scrape all images from the PTT Food board, use the following command:

```
python main.py --board Food
```

## Docker Support

You can also run the PTT Image Crawler in a Docker container. First, build the Docker image using the following command:

```bash
docker build -t my-python-app .
```

Then, execute the image with the specified options. For example, to scrape images from the Food board and save them to a local directory, use this command:
```bash
docker run -it --rm -v /where/you/want/to/save:/usr/src/app/img --name my-running-app my-python-app --board Food
```
This will run the crawler in an isolated environment within a Docker container.


