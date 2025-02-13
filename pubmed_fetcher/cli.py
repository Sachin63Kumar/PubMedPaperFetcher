import argparse
import logging  # Add this import
from pubmed_fetcher.fetcher import PubMedFetcher
import csv
from pubmed_fetcher.utils import setup_logger

def save_to_csv(papers, filename):
    keys = papers[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)

def main():
    logger = setup_logger()
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)  # Now logging is properly defined
    
    logger.info("Fetching papers...")
    fetcher = PubMedFetcher(args.query)
    papers = fetcher.fetch_papers()
    
    if not papers:
        logger.warning("No relevant papers found.")
        return
    
    if args.file:
        save_to_csv(papers, args.file)
        logger.info(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
