import ssl
import certifi
from typing import List, Dict
from Bio import Entrez

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = lambda: ssl_context

Entrez.email = "mdjunaid34343@gmail.com"

def search_pubmed(query: str, max_results: int = 10) -> List[str]:
    """Search PubMed for a query and return a list of PMIDs."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch paper details from a list of PubMed IDs."""
    ids_str = ",".join(pubmed_ids)
    handle = Entrez.efetch(db="pubmed", id=ids_str, rettype="medline", retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    results = []

    for article in records["PubmedArticle"]:
        paper = {}
        medline = article.get("MedlineCitation", {})
        article_data = medline.get("Article", {})

        paper["PubmedID"] = medline.get("PMID", "")
        paper["Title"] = article_data.get("ArticleTitle", "")
        paper["PublicationDate"] = article_data.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "")

        affiliations = []
        non_academic = []
        companies = []

        authors = article_data.get("AuthorList", [])

        for author in authors:
            aff_info = author.get("AffiliationInfo", [])
            aff = aff_info[0].get("Affiliation", "") if aff_info else ""
            name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()

            if aff:
                affiliations.append((name, aff))
                if not any(x in aff.lower() for x in ["university", "college", "institute", "school", "hospital"]):
                    non_academic.append(name)
                    companies.append(aff)

        paper["NonAcademicAuthors"] = "; ".join(set(non_academic))
        paper["CompanyAffiliations"] = "; ".join(set(companies))

        # Optional: Try to extract an email from affiliation
        paper["CorrespondingEmail"] = ""
        for name, aff in affiliations:
            if "@" in aff:
                words = aff.split()
                for word in words:
                    if "@" in word:
                        paper["CorrespondingEmail"] = word.strip(";.,()[]")
                        break
                break

        results.append(paper)

    return results
