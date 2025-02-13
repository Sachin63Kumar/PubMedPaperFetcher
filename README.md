# PubMedPaperFetcher

## Overview
PubMedPaperFetcher is a Python-based command-line tool that allows users to fetch research papers from PubMed based on specified search queries. The tool is useful for researchers, students, and professionals who need to collect relevant papers efficiently.

## Features
- Fetches research papers from PubMed using keyword-based search
- Exports results to a CSV file
- Easy to use command-line interface (CLI)
- Lightweight and fast execution

## Installation

### Prerequisites
Ensure you have Python (>=3.8) and [Poetry](https://python-poetry.org/docs/) installed on your system.

### Install via Poetry
```sh
# Clone the repository
git clone https://github.com/Sachin63Kumar/PubMedPaperFetcher.git
cd PubMedPaperFetcher

# Install dependencies
poetry install
```

### Install via PyPI
```sh
pip install sachin63kumar-paper-fetcher
```

## Usage

### Fetch Papers from PubMed
```sh
poetry run paper-fetcher --query "machine learning in healthcare" --max-results 10
```

### CLI Arguments
| Argument         | Description                              | Example |
|-----------------|------------------------------------------|---------|
| `--query`       | Search query for PubMed papers          | "AI in medicine" |
| `--max-results` | Number of papers to fetch (default: 5) | `10` |
| `--output`      | Output file name (default: results.csv) | `my_results.csv` |

### Example Output
```
Fetching 10 research papers related to "machine learning in healthcare"...
Results saved to results.csv
```

## Development Setup
If you want to contribute or modify the project:
```sh
# Activate virtual environment
poetry shell

# Run tests
pytest
```

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **Sachin Kumar**. Feel free to reach out on [GitHub](https://github.com/yourusername) for any queries or suggestions.
