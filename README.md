
# PubMedPaperFetcher

## Overview
PubMed Paper Fetcher is a Python-based command-line tool that allows users to fetch research papers from PubMed based on specified search queries. The tool is useful for researchers, students, and professionals who need to collect relevant papers efficiently.

## Project Structure
```
└── 📁PubMedPaperFetcher
    └── 📁__pycache__
    └── 📁dist
    └── 📁pubmed_fetcher
        └── 📁__pycache__
        └── __init__.py
        └── cli.py
        └── fetcher.py
        └── utils.py
    └── .gitignore
    └── poetry.lock
    └── pyproject.toml
    └── README.md
    └── results.csv
```

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
poetry run get-papers-list "machine learning in healthcare" -f results.csv 

```

### Example Output
```
2025-02-13 17:08:31,956 - INFO - Fetching papers...
{'PubmedID': '39939160', 'Title': "What makes a 'good' decision with artificial intelligence? A grounded theory study in paediatric care.", 'Publication Date': {'Year': '2025', 'Month': 'Feb', 'Day': '12'}, 'Non-academic Author(s)': 'McCradden Melissa D, Assadi Azadeh', 'Company Affiliation(s)': 'The Hospital for Sick Children, Toronto, Ontario, Canada melissa.mccradden@adelaide.edu.au., The Hospital for Sick Children, Toronto, Ontario, Canada.', 'Corresponding Author Email': 'N/A'}
{'PubmedID': '39937162', 'Title': "Exploring Older Adults' Perspectives and Acceptance of AI-Driven Health Technologies: Qualitative Study.", 'Publication Date': {'Year': '2025', 'Month': 'Feb', 'Day': '12'}, 'Non-academic Author(s)': 'Yang Shulan', 'Company Affiliation(s)': 'Nursing Department, Zhejiang Hospital, Hangzhou, China.', 'Corresponding Author Email': 'N/A'}
{'PubmedID': '39935613', 'Title': 'Advanced sleep disorder detection using multi-layered ensemble learning and advanced data balancing techniques.', 'Publication Date': {'Year': '2024'}, 'Non-academic Author(s)': 'Uddin Md Zia', 'Company Affiliation(s)': 'Sustainable Communication Technologies, SINTEF Digital, Oslo, Norway.', 'Corresponding Author Email': 'N/A'}
{'PubmedID': '39934485', 'Title': 'The Many Facets of PPAR-γ Agonism in Obesity and Associated Comorbidities: Benefits, Risks, Challenges, and Future Directions.', 'Publication Date': {'Year': '2025', 'Month': 'Feb', 'Day': '12'}, 'Non-academic Author(s)': 'Vallianou Natalia G', 'Company Affiliation(s)': 'First Department of Internal Medicine, Sismanogleio General Hospital, 15126, Athens, Greece.', 'Corresponding Author Email': 'N/A'}
{'PubmedID': '39934248', 'Title': 'MedFuseNet: fusing local and global deep feature representations with hybrid attention mechanisms for medical image segmentation.', 'Publication Date': {'Year': '2025', 'Month': 'Feb', 'Day': '11'}, 'Non-academic Author(s)': 'He Saiqi', 'Company Affiliation(s)': 'Hengyang Central Hospital, Hengyang, Hunan, 421000, China.', 'Corresponding Author Email': 'N/A'}
{'PubmedID': '39934077', 'Title': 'Machine Learning Methods Based on Chest CT for Predicting the Risk of COVID-19-Associated Pulmonary Aspergillosis.', 'Publication Date': {'Year': '2025', 'Month': 'Feb', 'Day': '10'}, 'Non-academic Author(s)': 'Zhang Juntao, Fang Caiyun', 'Company Affiliation(s)': "GE Healthcare PDX GMS Medical Affairs, Shanghai, China\xa0(J.Z.)., Department of Radiology, Guang'anmen Hospital Jinan Hospital, Jinan, China\xa0(C.F.).", 'Corresponding Author Email': 'N/A'}

Fetched research papers related to "machine learning in healthcare"...
Results saved to results.csv
```

## Command-line Program Features Testing
1. Accepting the Query as a Command-line Argument
```sh
poetry run get-papers-list "cancer research"
```
#### Expected Output:
- The script should fetch research papers related to "cancer research" and display them on the console.

2. -h or --help Option (Usage Instructions)
```sh
poetry run get-papers-list -h

```
#### Expected Output:
- Should display usage instructions explaining how to use the command.

3. -d or --debug Option (Debug Mode)
```sh
poetry run get-papers-list "cancer research" -d

```
#### Expected Output:
- Debug logs should be displayed.

4. -f or --file Option (Saving Results to CSV)
```sh
poetry run get-papers-list "cancer research" -f results.csv
```
#### Expected Output:
- The fetched papers should be saved in results.csv.
- You should see a log message:
    ```
    INFO - Results saved to results.csv
    ```
- Open results.csv in Excel or a text editor to check if the results are correctly written.


## Development Setup
If you want to contribute or modify the project:
```sh
# Activate virtual environment
poetry shell

# Run tests
pytest
```

## Tools & Libraries Used
- **Poetry** - Dependency management ([Learn more](https://python-poetry.org/))
- **Requests** - HTTP requests for fetching data ([Learn more](https://docs.python-requests.org/en/latest/))
- **Pandas** - Data processing ([Learn more](https://pandas.pydata.org/))

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
