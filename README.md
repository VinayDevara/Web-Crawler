# WebCrawler
Developed a web crawler which can actively crawl through sites with active cpu monitorisation with an interface

# Web Crawling Project

## Project Overview
This project implements a web crawler designed to extract specific metrics and data from target websites. It employs multithreading and concurrency concepts to enhance performance and efficiency in data retrieval. The extracted data includes CPU and memory usage metrics from various system monitoring websites.

## Features
- **Multithreaded Crawling**: Utilizes concurrent threads to fetch data from multiple sources simultaneously.
- **Metric Extraction**: Parses HTML pages to extract CPU and memory usage metrics.
- **Error Handling**: Implements robust error handling to ensure data integrity and reliability.
- **Metrics Display**: Displays retrieved metrics in real-time for monitoring purposes.
- **Optimization**: Implemented a database-backed system to track visited URLs, preventing redundant requests.

<img width="1470" alt="image" src="https://github.com/Gnaneshwar7020/WebCrawler/assets/70259681/53da7236-1f47-42ee-9659-5c69ba363515">

## Requirements
- Python 3.x
- Required Python packages: requests, beautifulsoup4, PSutil

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/VinayDevara/Web-Crawler.git
   ```
2. Navigate to the project directory:
   ```
   cd WebCrawler
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script:
   ```
   python app.py
   ```
2. Monitor the console output for real-time metrics retrieved from the specified websites.
3. Run the crawler script:
   ```
   python crawler.py
   ```
4. Crawler starts working and you can observe the cpu state.

## Configuration
- Customize the list of target URLs and other parameters in `config.py` according to your requirements.

## Contributing
Contributions are welcome! Fork the repository and submit a pull request with your enhancements.


---

Feel free to customize the sections and details based on your specific project and preferences!
