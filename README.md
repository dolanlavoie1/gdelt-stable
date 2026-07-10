# GDELT-STABLE

Python package to do gdelt stuff

## GDELT 1.0:
Official Documentation: http://data.gdeltproject.org/documentation/GDELT-Global_Knowledge_Graph_Codebook.pdf

 - All cols: Keyword - Word to search entries for
 - Col 1: Start date - YYYYMMDD. Goes as far back as 20130401
 - Col 1: Start date - YYYYMMDD. Updated daily
 - Col 1: Timespan - How long of a range to search for
 - Col 2: Num Arts - Number of documents referencing this dataset
 - Col 3: Counts - A count of something
   - Count type - Indicates what the count is counting. (Ex. ARREST, KIDNAP, KILL)
   - Count - The actual count being reported
   - Count object type - What the number is. (Ex. Christian missionaries)
 - Col 4: Themes - List of themes that describe the topic of the document (Ex. NATURAL DISASTER)
 - Col 5: Location - Where the event takes place
   - Location type
      1. Country
      2. USSTATE
      3. USCITY
      4. WORLDCITY
      5. WORLDSTATE
   - Location full name - Human readable name of the location (Ex. United States)
   - Country code - FIPS10-4 country code (Ex. US)
   - Administrative division 1 code - FIPS10-4 country code, followed by FIPS10-4 ADM1 code, or US state abbreviation (Ex. USCA)
   - Location lattitude - Lattitude of the center of the location
   - Location longitude - Longitude of the center of the location
   - GNIS feature id or ADM1 code
 - Col 6: Persons - List of all people referenced in the document (Ex. Tom Cruise)
 - Col 7: Orginizations - List of all orginizations referenced in the document (Ex. United Nations)
 - Col 8: Tone - Numbers describing the tone of the document
   - Tone - The average tone of the document, from -100 to 100
   - Positive Score - The percentage of words in the document that are considered positive in tone
   - Negative Score - The percentage of words in the document that are considered negative in tone
   - Polarity - The percentage of words that have emotional value
   - Activity Refernce Density - Precentage of words that are active words
   - Self/Group Reference Density - Percentage of all words that are pronouns
   - Word Count - Count of all words in the document
 - Col 9: Cameo Event IDs - List of GlobalEventIDs from the master GDELT event stream
 - Col 10: Sources - Usually just a domain name, but can also be the actual name of the source or have multiple sources (Ex. BBC Monitoring)
 - Col 11: Source URLs - List of all articles mentioning the nameset (Ex. https://www.bbc.com/news/live/cp9l8l05vxet)



## GDELT 2.0:
Official Documentation: http://data.gdeltproject.org/documentation/GDELT-Global_Knowledge_Graph_Codebook-V2.1.pdf

 - All cols: Keyword - Word to search entries for
 - Col 2: Start date/time - YYYYMMDDHHMMSS. Goes as far back as 20150218
 - Col 2: End date/time - YYYYMMDDHHMMSS. Updated every 15 minutes
 - Col 2: How long of a range to search for
 - Col 3: Source type
   1. WEB - Originates from the open web
   2. CITATIONONLY - Originates from an offline source
   3. CORE - Originates from the CORE archive
   4. DTIC - Originates from the DTIC archive
   5. JSTOR - Originates from the JSTOR archive
   6. NONTEXTUALSOURCE - Originates from a non textual source, like a video
 - Col 4: Source name - Usually just domain name, but can also be the actual name of the source (Ex. BBC Monitoring)
 - Col 5: Document identifier - Usually just a url, but can also be DOI numbers or citations (Ex. https://www.bbc.com/news/live/cp9l8l05vxet)
 - Col 7: Count - A count of something
   - Count type - Indicates what the count is counting. (Ex. ARREST, KIDNAP, KILL)
   - Count - The actual count being reported
   - Count object type - What the number is. (Ex. Christian missionaries)
   - Offset - How far into the document the count is found
 - Col 9: Themes - List of themes that describe the topic of the document
   - Theme - The theme found in the document (Ex. NATURAL_DISASTER)
   - Offset - How far into the document the theme is found
 - Col 11: Location - Where the event takes place
   - Location type
      1. Country
      2. USSTATE
      3. USCITY
      4. WORLDCITY
      5. WORLDSTATE
   - Location full name - Human readable name of the location (Ex. United States)
   - Country code - FIPS10-4 country code (Ex. US)
   - Administrative division 1 code - FIPS10-4 country code, followed by FIPS10-4 ADM1 code, or US state abbreviation (Ex. USCA)
   - Location lattitude - Lattitude of the center of the location
   - Location longitude - Longitude of the center of the location
   - GNIS feature id or ADM1 code
   - Offset - How far into the document the location is found
 - Col 13: Persons - List of all people referenced in the document
   - Person - The person found in the document (Ex. Tom Cruise)
   - Offset - How far into the document the person is found
 - Col 15: Orginizations - List of all orginizations referenced in the document
   - Orginization - The orginization found in the document (Ex. United Nations)
   - Offset - How far into the document the orginization is found
 - Col 16: Tone - Numbers describing the tone of the document
   - Tone - The average tone of the document, from -100 to 100
   - Positive Score - The percentage of words in the document that are considered positive in tone
   - Negative Score - The percentage of words in the document that are considered negative in tone
   - Polarity - The percentage of words that have emotional value
   - Activity Refernce Density - Precentage of words that are active words
   - Self/Group Reference Density - Percentage of all words that are pronouns
   - Word Count - Count of all words in the document
 - Col 17: Date References - Additional dates referenced in the document
   - Date Resolution - Resolution of additional dates that are mentioned in the document
      1. Year only
      2. Month and year
      3. Month, year, and date
      4. Month and day but no year
   - Month - Numerical month for additional dates, or 0 if not mentioned
   - Day - Numerical day for additional dates, or 0 if not mentioned
   - Year - Year for additional dates, or 0 if not mentioned
   - Offset - How far into the document the date is found
 - Col 18: V2GCAM - Vector stuff
 - Col 19: Sharing Image - Linked image url to display when the article is shared (Ex. https://www.eveningnews24.co.uk/resources/images/16461119/?type=og-image)
 - Col 20: Related Images - List of image urls that are related to the story (Ex. https://www.eveningnews24.co.uk/resources/images/16461129.jpg?type=mds-article-575)
 - Col 21: Social Media Embeds - Links to embedded twitter and instagram posts on an article (Ex. https://pic.twitter.com/X2v6pDecqP)
 - Col 22: Social Video Embeds - Links to embedded videos or related channels on youtube, dailymotion, vimeo, or vine (Ex. https://youtube.com/watch?v=LMXqw7Pe-AQ&ab_channel=OhioRails)
 - Col 23: Quotations - A quotation from a person relating to an event
   - Offset - How far into the document the quotation is found
   - Length - The length of the quoted segment
   - Verb - The verb used to introduce the quote
   - Quote - The quotation itself (Ex. 2022 was a year of missed chances)
 - Col 24: All Names - A list of ALL proper names found in a document
   - Name - The name found in the document (Ex. Washington State)
   - Offset - How far into the document the name is found
 - Col 25: All Amounts - A list of all numerical values found in a document
   - Amount - The amount found in the document
   - Object - The object the amount refers to. (Ex. Combat Soldiers)
   - Offset - How far into the document the amount is found
 - Col 26: Translation Info - Records information for machine translated documents
   - SRCLC - ISO639-2 code of the language of the original source material. (Ex. spa)
   - ENG - Indicates the engines and models used to translate the document. (Ex. Moses 2.1.1 / MosesCore Europarl fr-en / GT-FRA 1.0)
 - Col 27: Extra XML - Extra information about the document
   - Authors - List of authors Ex. \<AUTHOR\>Kalev Hannes Leetaru\</AUTHOR\>
   - Title - Title of the document
   - Book Title - Title of the document if it is a book
   - Date - Date of the document
   - Journal - The journal that the document was published in
   - Volume - The volume of the journal that the document was published in
   - Issue - The issue of the journal issue that the document was published in
   - Pages - The page range of the document
   - Institution - The institutional affiliation of the document
   - Publisher - The publisher of the document
   - Location - The location of publisher of the document
   - Marker - This is the textual marker used to identify the work in the text (Leetaru et al, 2014)

## GDELT API:
Official Documentation: https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/

 - Keyword - Word to search for (Ex. "donald trump")
 - Domain - Specific domain to searh for (Ex. domain:cnn.com)
 - Domain Is - Specific domain to search for, requiring exact match (Ex. domainis:un.org)
 - Image Face Tone - Average tone of faces in images (Ex. imagefacetone<-1.5)
 - Image Num Faces - Number of faces in an image (Ex. imagenumfaces>3)
 - ImageOCRMeta - Search for text found in an image (Ex. imageocrmeta:"zika")
 - Image Tag - Search for a image tag (Ex. imagetag:"safesearchviolence")
 - Image Web Count - Search for how many times an image has been used (Ex. imagewebcount<10)
 - Image Web Tag - Search for a tag relating to the image's context (Ex. imagewebtag:"drone")
 - Near - Set of words that must appear near each other (Ex. near20:"trump putin")
 - Repeat - Word that must repeat a certain number of times (Ex. repeat3:"trump")
 - Source Country - Articles published in a certain country (Ex. sourcecountry:france)
 - Source Language - Articles originally published in a given language (Ex. sourcelang:spanish)
 - Theme - Articles with the given theme (Ex. theme:TERROR)
 - Tone - How positive or negative the article is (Ex. tone<-5)
 - ToneAbs - How emotional the article is (Ex. toneabs>10)
 - Timespan - How long of a range to search for (Ex. timespan=1week)
 - Start date/time - When to begin the search in YYYYMMDDHHMMSS
 - End date/time - When to end the search in YYYYMMDDHHMMSS
 - Max Records - Number of records to return. 75 by default, max 250. (Ex. maxrecords=100)
 - Trans - Translate everything into a requested language (Ex. trans=french)
 - Sort - Sort by a specific attribute (Ex. sort=datedesc)
   - DateDesc - Most recent articles first
   - DateAsc - Oldest articles first
   - ToneDesc - Most positive articles first
   - ToneAsc - Most negative articles first
   - HybridRel - Default sorting mode by relevance