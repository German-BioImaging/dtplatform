
Leap D1 Demonstrator
====================

# publication records
  
```sparql
## Leap group leaders
  
```sparql
#title:Leap group leaders  
SELECT * WHERE {  
   VALUES ?leapauthor {  
       wd:Q59830751  
       wd:Q59679079  
       wd:Q59679079  
       wd:Q59674360  
       wd:Q5107972  
       wd:Q39049575  
       wd:Q30004330  
       wd:Q55101059  
       wd:Q88590244  
       wd:Q88797604  
       wd:Q5638525  
       wd:Q96210212  
       wd:Q49516549  
      }  
  
  ?leapauthor rdfs:label ?leapauthorLabel .  
  
  FILTER (lang(?leapauthorLabel)="en")  
}

<iframe style="width: 80vw; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23title%3ALeap%20group%20leaders%0ASELECT%20%2A%20WHERE%20%7B%0A%20%20%20VALUES%20%3Fleapauthor%20%7B%0A%20%20%20%20%20%20%20wd%3AQ59830751%0A%20%20%20%20%20%20%20wd%3AQ59679079%0A%20%20%20%20%20%20%20wd%3AQ59679079%0A%20%20%20%20%20%20%20wd%3AQ59674360%0A%20%20%20%20%20%20%20wd%3AQ5107972%0A%20%20%20%20%20%20%20wd%3AQ39049575%0A%20%20%20%20%20%20%20wd%3AQ30004330%0A%20%20%20%20%20%20%20wd%3AQ55101059%0A%20%20%20%20%20%20%20wd%3AQ88590244%0A%20%20%20%20%20%20%20wd%3AQ88797604%0A%20%20%20%20%20%20%20wd%3AQ5638525%0A%20%20%20%20%20%20%20wd%3AQ96210212%0A%20%20%20%20%20%20%20wd%3AQ49516549%0A%20%20%20%20%20%20%7D%0A%0A%20%20%3Fleapauthor%20rdfs%3Alabel%20%3FleapauthorLabel%20.%0A%0A%20%20FILTER%20%28lang%28%3FleapauthorLabel%29%3D%22en%22%29%0A%7D"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>

  
```sparql
## Group leaders and their past and present affiliations
  
```sparql
#title: Group leaders and their past and present affiliations  
PREFIX wd: <http://www.wikidata.org/entity/>  
PREFIX wdt: <http://www.wikidata.org/prop/direct/>  
PREFIX wikibase: <http://wikiba.se/ontology#>  
PREFIX bd:<http://www.bigdata.com/rdf#>  
  
SELECT DISTINCT ?leapauthor ?leapauthorLabel ?affiliation ?affiliationLabel WHERE {  
   VALUES ?leapauthor {wd:Q59830751 wd:Q59679079 wd:Q59679079 wd:Q59674360 wd:Q5107972 wd:Q39049575 wd:Q30004330 
wd:Q55101059 wd:Q88590244 wd:Q88797604 wd:Q5638525 wd:Q96210212 wd:Q49516549}  
  
  ?leapauthor wdt:P108 ?affiliation .  
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }  
}  
ORDER BY ?leapauthor

<iframe style="width: 80vw; height: 50vh; border: none;" 
src="https://query.wikidata.org/embed.html#%23title%3A%20Group%20leaders%20and%20their%20past%20and%20present%20affiliations%0APREFIX%20wd%3A%20%3Chttp%3A//www.wikidata.org/entity/%3E%0APREFIX%20wdt%3A%20%3Chttp%3A//www.wikidata.org/prop/direct/%3E%0APREFIX%20wikibase%3A%20%3Chttp%3A//wikiba.se/ontology%23%3E%0APREFIX%20bd%3A%3Chttp%3A//www.bigdata.com/rdf%23%3E%0A%0ASELECT%20DISTINCT%20%3Fleapauthor%20%3FleapauthorLabel%20%3Faffiliation%20%3FaffiliationLabel%20WHERE%20%7B%0A%20%20%20VALUES%20%3Fleapauthor%20%7Bwd%3AQ59830751%20wd%3AQ59679079%20wd%3AQ59679079%20wd%3AQ59674360%20wd%3AQ5107972%20wd%3AQ39049575%20wd%3AQ30004330%20wd%3AQ55101059%20wd%3AQ88590244%20wd%3AQ88797604%20wd%3AQ5638525%20wd%3AQ96210212%20wd%3AQ49516549%7D%0A%0A%20%20%3Fleapauthor%20wdt%3AP108%20%3Faffiliation%20.%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D%0AORDER%20BY%20%3Fleapauthor%0A"
 referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>

