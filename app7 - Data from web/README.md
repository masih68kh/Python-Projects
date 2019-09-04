# Web Scraping
## Reading data from a real estate website  

the objective of this app is to read the data of the houses in the following website  
<http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/>  
and save it in a .csv file.

---

`BeautifulSoup` python package is needed for this app.  
using this package, we can capture the data that is wrapped in specific title on a HTML pages

---
*for example, for the above website, the following data header has been captured*  

|Address|Price|Sq Ft|Number of Bedrooms|Number of Bathrooms|
|-------|-----|-----|------------------|-------------------|
|"0 Gateway Rock Springs, WY 82901"|$725,000|790|2|1|
|"1003 Winchester Blvd., Rock Springs, WY 82901"|$452,000|900|4|4|
|"600 Talladega, Rock Springs, WY 82901"|$396,900|3,154|5|3|