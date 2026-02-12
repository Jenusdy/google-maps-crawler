# Google Maps Crawler -  Points Crawler

A data crawling project Google Maps to identify and collect geographic coordinates.

## Overview

This project crawls and processes data to extract their locations using the Google Maps. It handles data collection, geocoding, and storage of results.

## Project Structure

```
├── Crawling-Points.ipynb       # Main Jupyter notebook with crawling logic
├── input/                       # Input data directory
│   └── Flat_sekolah_terdampak.csv
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

Run the Jupyter notebook :

The notebook will:
- Read input data from `input/`
- Read for Google Maps Search
- Process 
- Output results to the same file

## License

MIT

## Author

JJ
