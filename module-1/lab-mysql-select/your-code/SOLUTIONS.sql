#CHALLENGE 1

SELECT authors.au_id AS AUTHOR_ID, 
	authors.au_lname AS LAST_NAME, 
    authors.au_fname AS FIRST_NAME, 
    titles.title AS TITLE,
    publishers.pub_name AS PUBLISHER
    
FROM authors

INNER JOIN publications.titleauthor
ON authors.au_id = titleauthor.au_id

INNER JOIN publications.titles
ON titleauthor.title_id = titles.title_id

INNER JOIN publications.publishers
ON titles.pub_id = publishers.pub_id  


#Porqué esta no funciona???

#FROM publications.titles titles
#INNER JOIN publications.titleauthor titleauthor
#	ON titles.title_id = titleathor.title_id
    
#INNER JOIN publications.authors author
#	ON titleauthor.au_id = authors.au_id;


# CHALLENGE 2

SELECT authors.au_id AS AUTHOR_ID, 
	authors.au_lname AS LAST_NAME, 
    authors.au_fname AS FIRST_NAME, 
    publishers.pub_name AS PUBLISHER,
    COUNT(titles.title_id)  AS TITLE_COUNT
    
FROM authors

INNER JOIN publications.titleauthor
ON authors.au_id = titleauthor.au_id

INNER JOIN publications.titles
ON titleauthor.title_id = titles.title_id

INNER JOIN publications.publishers
ON titles.pub_id = publishers.pub_id  

GROUP BY AUTHOR_ID, LAST_NAME, FIRST_NAME, PUBLISHER
ORDER BY TITLE_COUNT DESC

#CHALLENGE 3

SELECT authors.au_id AS AUTHOR_ID,
authors.au_lname AS LAST_NAME,
authors.au_fname AS FIRST_NAME,
SUM(sales.qty) AS TOTAL 

FROM authors

INNER JOIN publications.titleauthor
ON titleauthor.au_id = authors.au_id

INNER JOIN publications.titles
ON titles.title_id = titleauthor.title_id

INNER JOIN publications.sales
ON sales.title_id = titles.title_id

GROUP BY AUTHOR_ID, LAST_NAME, FIRST_NAME
ORDER BY TOTAL DESC 
	LIMIT 3

#CHALLENGE 4

SELECT authors.au_id AS AUTHOR_ID,
authors.au_lname AS LAST_NAME,
authors.au_fname AS FIRST_NAME,
SUM(sales.qty) AS TOTAL 

FROM authors

INNER JOIN publications.titleauthor
ON titleauthor.au_id = authors.au_id

INNER JOIN publications.titles
ON titles.title_id = titleauthor.title_id

INNER JOIN publications.sales
ON sales.title_id = titles.title_id

GROUP BY AUTHOR_ID, LAST_NAME, FIRST_NAME
ORDER BY TOTAL DESC 
	
#BONUS CHALLENGE

SELECT authors.au_id AS AUTHOR_ID, 
	authors.au_lname AS LAST_NAME, 
    authors.au_fname AS FIRST_NAME, 
	SUM(titles.advance) + SUM(titles.royalty) AS PROFIT
   
FROM authors

INNER JOIN publications.titleauthor
ON authors.au_id = titleauthor.au_id

INNER JOIN publications.titles
ON titleauthor.title_id = titles.title_id

GROUP BY AUTHOR_ID, LAST_NAME, FIRST_NAME

ORDER BY PROFIT DESC
