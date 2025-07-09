# get-papers-tool

## Overview
A Python CLI tool to fetch PubMed research papers and filter authors affiliated with non-academic institutions (like biotech or pharma companies). Returns results as a CSV file.

## Features
- Fetches papers using PubMed API
- Filters authors based on affiliation
- Outputs CSV or console print
- CLI options: `--query`, `--file`, `--debug`

## Tech Stack
- Python 3
- Biopython
- Typer
- Pandas
- Poetry

## Installation

git clone https://github.com/junaid876/get-papers-tool
cd get-papers-tool
poetry install

## Usage
poetry run get-papers-list --query "covid vaccine" --file results.csv
poetry run get-papers-list --query "diabetes" --debug
poetry run get-papers-list --help

### Output CSV Format
- **PubmedID**  
- **Title**  
- **Publication Date**  
- **Non-Academic Authors**  
- **Company Affiliations**  
- **Corresponding Email**

### Tools Used
- ChatGPT (for project guidance)
- Biopython
- Poetry
- pandas


Author
Mohammad Junaid
