# Google Maps API - School Points Crawler

A data crawling project that uses the Google Maps API to identify and collect geographic coordinates for affected schools.

## Overview

This project crawls and processes data about schools to extract their locations using the Google Maps API. It handles data collection, geocoding, and storage of results.

## Project Structure

```
├── Crawling-Points.ipynb       # Main Jupyter notebook with crawling logic
├── input/                       # Input data directory
│   └── Flat_sekolah_terdampak.csv
├── output/                      # Generated output directory
│   └── Flat_sekolah_terdampak.csv
├── test/                        # Test HTML files for validation
│   ├── found-exact-one.html
│   ├── found-many.html
│   ├── klik-hasil.html
│   └── not-found.html
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Requirements

- Python 3.6+
- Jupyter Notebook
- Libraries (see notebook for full requirements):
  - requests
  - pandas
  - beautifulsoup4
  - (Google Maps API Python client or similar)

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Google Maps API key in a `.env` file or `config.json` (not committed to git)

## Usage

Run the Jupyter notebook to crawl and process school location data:

```bash
jupyter notebook Crawling-Points.ipynb
```

The notebook will:
- Read input data from `input/`
- Query Google Maps API for school locations
- Process and validate results
- Output results to `output/`

## Notes

- API keys and credentials should **never** be committed to the repository
- Use `.env` file or environment variables for sensitive configuration
- Test HTML files are provided for validation purposes

## License

[Add your license here]

## Author

[Add author information here]
