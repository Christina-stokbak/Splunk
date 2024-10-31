# Splunk

## Download Splunk Enterprise
Der skal oprettes en bruger for at kunne downloade Splunk Enterprise. <br>
Splunk Enterprise kan downloades [her](https://www.splunk.com/en_us/download/splunk-enterprise.html)

## Docker
Følgense kommando kan køres i docker for at starte en container på port 8000 med Splunk Enterprise <br>
``docker run -d -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=<password>" --name splunk splunk/splunk:latest`` <br>
- Brugernavn: admin
- Password: Det password der indsættes i kommandoen

## Lav queries på data i python
Splunk sdk'en skal installeres før det kan køres. Lav evt. et environment og kør derefter kommandoen `pip install splunk-sdk` i roden på python projektet <br>

[Splunkservice](pythonApp\splunkservice.py) filen indeholder en simpel query. Ved at køre kommandoen `python splunkservice.py` fra et kommandprompt i den sti filen ligger i vil den hente data **More description to come
