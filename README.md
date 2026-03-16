# Google Maps Crawler - Points Crawler

A data crawling project using Google Maps to identify and collect geographic coordinates for location-based data.

## Overview

This project crawls and processes location data to extract their geographic coordinates (latitude and longitude) using Google Maps. It handles data collection, geocoding, boundary validation, and storage of results. The crawler includes features for:

- Automated Google Maps searching via Selenium
- Coordinate extraction and validation
- Boundary checking against polygon areas
- Name similarity matching
- Handling of Google blocks and retries
- Parallel data processing through dataframe splitting

## Project Structure

```
├── 1. Split Dataframe.ipynb       # Splits input CSV into manageable chunks
├── 2. Crawling Points.ipynb       # Main crawling notebook with Google Maps scraping logic
├── requirements.txt               # Python dependencies
├── input/                          # Input data directory
│   ├── 20260313 - SBR Jatinegara.csv
│   └── jatinegara-boundary.gpkg    # Boundary polygon for validation
├── proses/                         # Work-in-progress and processed data
└── output/                         # Final output CSV files
└── .gitignore                      # Git ignore rules
```

## Features

### Data Processing
- **Data Splitting**: Split large CSV files into smaller chunks based on row ranges for parallel processing
- **Progress Tracking**: Automatic saving and resuming of crawling progress
- **CSV Handling**: Support for semicolon-separated CSV files

### Crawling Capabilities
- **Google Maps Search**: Automated searching using Selenium WebDriver
- **Multiple Result Handling**: Handles scenarios with direct results, multiple results, and not found cases
- **Coordinate Extraction**: Extracts latitude and longitude from Google Maps URLs
- **Place Name Matching**: Compares input names with Google place names using fuzzy matching

### Validation & Quality Control
- **Boundary Checking**: Validates if coordinates fall within specified polygon boundaries
- **Similarity Scoring**: Calculates name similarity using token set ratio
- **Status Tracking**: Tracks crawling status codes:
  - `0`: Found successfully
  - `1`: Found but no coordinates extracted
  - `2`: Not found on Google Maps
  - `3`: Blocked by Google (retried automatically)
- **Closed Status**: Detects temporarily closed status

### Error Handling
- **Google Block Detection**: Detects and handles CAPTCHA/block scenarios
- **Auto-Retry**: Automatically restarts WebDriver when blocked
- **Robust URL Parsing**: Handles various Google Maps URL formats

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Chrome Browser (for Selenium WebDriver)
- Python libraries:
  - `selenium==4.40.0` - Browser automation
  - `bs4==0.0.2` - HTML parsing
  - `beautifulsoup4==4.12.3` - HTML parsing
  - `pandas==1.5.3` - Data manipulation
  - `tqdm==4.65.0` - Progress bars
  - `geopandas` - Geospatial data handling
  - `shapely` - Geometric operations
  - `rapidfuzz` - Fuzzy string matching

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd google-maps-crawler
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download ChromeDriver compatible with your Chrome browser version and ensure it's in your PATH.

## Usage

### Step 1: Split Data (Optional)

If you have a large dataset, split it into smaller chunks for parallel processing:

1. Open `1. Split Dataframe.ipynb`
2. Update the input file path and row ranges:
   ```python
   df = pd.read_csv('input/your-file.csv', sep=';', dtype=object)
   row_start = 20771
   row_end = 24924
   ```
3. Run the notebook to create split files in the `proses/` directory

### Step 2: Run Crawler

1. Open `2. Crawling Points.ipynb`
2. Configure the parameters:
   ```python
   row_start = 20771
   row_end = 24924
   file_input = f"Data-SBR-{row_start}-{row_end}.csv"
   ```
3. Run the notebook to start crawling

The crawler will:
- Read processed data from `proses/`
- Search Google Maps for each location
- Extract coordinates, place names, and URLs
- Validate against boundary polygon
- Save progress incrementally
- Handle Google blocks automatically
- Output final results to the same CSV file

### Understanding the Output

The output CSV contains these additional columns:
- `latitude`: Extracted latitude
- `longitude`: Extracted longitude
- `nama_google`: Google place name
- `url`: Google Maps URL
- `isna`: Status code (0=found, 1=retry needed, 2=not found, 3=blocked)
- `temporary_closed`: Whether the place is temporarily closed
- `similarity`: Name similarity score (0-100)
- `inside_boundary`: Whether coordinates are within the boundary polygon (0=no, 1=yes)

## Notes

- **Rate Limiting**: Google may block automated searches. The crawler includes retry logic, but consider adding delays between requests.
- **ChromeDriver**: Ensure ChromeDriver version matches your Chrome browser version.
- **Boundary Files**: Boundary files (`.gpkg`) should contain polygon geometry in a compatible coordinate system (default assumes EPSG:4326).
- **CSV Format**: Input CSVs should be semicolon-separated with at least `nama` (location name) and `nmdesa` (village name) columns.

## License

MIT

## Author

JJ
