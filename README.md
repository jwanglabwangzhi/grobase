# grobase
## Description
This is a nascent RNA database from GRO-Seq.  
## Here is the api doc.
1 get three select dict  

function: get a dict of species, cell lines, treatments;  

method: get;  

url: http://39.105.21.162:8000/api/species_json/;  

results:  

```
[
    {
        "id": 1,
        "sources": [
            {
                "id": 1,
                "process": [
                    {
                        "id": 1,
                        "is_active": false,
                        "bwsize": "6.39",
                        "process_name": "no",
                        "citation": "Nascent RNA sequencing reveals distinct features in Plant transcription",
                        "gse": "GSE83108",
                        "gsm": "GSM2193125",
                        "oganization": "University of California, San Diego",
                        "pmid": "27729530",
                        "srr": "SRR3647035",
                        "submit_date": "8-Jun-16",
                        "tissue": "seedling",
                        "source": 1
                    },
```



