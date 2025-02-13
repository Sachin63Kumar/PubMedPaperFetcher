import requests
import csv
import argparse
import re
import os
from typing import List, Dict, Optional
from Bio import Entrez

# Set your email for PubMed API access
Entrez.email = "your-email@example.com"

class PubMedFetcher:
    def __init__(self, query: str):
        self.query = query
    
    def fetch_papers(self, max_results: int = 10) -> List[Dict[str, str]]:
        """Fetches papers from PubMed based on a query."""
        handle = Entrez.esearch(db="pubmed", term=self.query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()
        pmids = record["IdList"]

        papers = []
        for pmid in pmids:
            paper_data = self.fetch_paper_details(pmid)
            if paper_data:
                papers.append(paper_data)
        return papers

    def fetch_paper_details(self, pmid: str) -> Optional[Dict[str, str]]:
        """Fetch details of a paper using PubMed ID."""
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="xml", retmode="text")
        record = Entrez.read(handle)
        handle.close()

        paper_info = record["PubmedArticle"][0]["MedlineCitation"]
        title = paper_info["Article"]["ArticleTitle"]
        pub_date = paper_info["Article"]["Journal"]["JournalIssue"]["PubDate"]
        authors = paper_info.get("Article", {}).get("AuthorList", [])
        
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None
        
        for author in authors:
            if "AffiliationInfo" in author:
                affiliation = author["AffiliationInfo"][0]["Affiliation"]
                if self.is_non_academic(affiliation):
                    non_academic_authors.append(author["LastName"] + " " + author["ForeName"])
                    company_affiliations.append(affiliation)
            if "ElectronicAddress" in author:
                corresponding_email = author["ElectronicAddress"]
        
        if not non_academic_authors:
            return None

        return {
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email or "N/A",
        }

    def is_non_academic(self, affiliation: str) -> bool:
        """Identify non-academic institutions based on heuristics."""
        academic_keywords = ["university", "college", "institute", "school", "lab", "research center"]
        return not any(keyword.lower() in affiliation.lower() for keyword in academic_keywords)