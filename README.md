# Textual Analysis CLI

An command-line interface (CLI) application for scraping and performing textual analysis on website content.

## Features

- Web scraping capabilities to extract content from given URLs.
- Textual analysis, including word frequency, average word length, total sentences, and sentiment analysis.
- Supports multiple top counts to display frequent words and letters.
- Verbose mode for detailed data.
- User-friendly command-line options and parameters.

## Installation

1. Ensure you have Python 3.x installed.
2. Clone this repository:

`git clone git@github.com:hilyas/text-analyzer.git`

3. Navigate to the repository directory:

`cd text-analyzer`

4. Install the required packages:

`pip install -r requirements.txt`

## Usage

To use the Textual Analysis CLI, run:

`python cli.py analyze --url [WEBSITE_URL] --top [NUMBER] --type [words/letters/both] --verbose`

- `--url`: The URL of the website to analyze.
- `--top`: Multiple top counts e.g. `--top 5 --top 10`. Default is `10`.
- `--type`: Type of analysis (words, letters, or both). Default is `both`.
- `--verbose`: Verbose mode to print more data.

## Dependencies

- `click`: For creating the CLI.
- `nltk`: For natural language processing tasks.
- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.

