# Academic Paper Search Documentation
**ria nair (rnair20), ann rajan (amrajan2), kavya varghese (kmvargh2)**  
**spring 2018**  

## prompt

*to do: remove this section*

At the end of the semester, each team must submit the software code produced for the project to an open source repository (github) along with a written documentation. The documentation should consist of the following elements: 1) An overview of the function of the code (i.e., what it does and what it can be used for). 2) Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement. 3) Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable. 4) Brief description of contribution of each team member in case of a multi-person team. Note that if you are in a team, it is your responsibility to figure out how to contribute to your group project, so you will need to act proactively and in a timely manner if your group coordinator has not assigned a task to you. There will be no opportunity to make up for any task that you failed to accomplish. In general, all the members of a team will get the same grade for the project unless the documentation submission indicates that some member(s) only superficially participated in the project without doing much actual work; in that case, we will discount the grade. Everyone is expected to spend at least 20 hours to seriously work on your course project as a minimum, not including the time spent for preparing the documentation.  

The 20% for the documentation submission includes 5% for overview of functions, 10% for implementation documentation, 5% for usage documentation.  

## overview

This search engine allows students and faculty to find relevant academic papers given a specific field. The user is prompted to select a topic from a drop down menu and a query. The engine then returns the top results for this query. The tool allows for a more narrow and more thorough search that ranks articles on relevance and credibility.

## implementation details

**Corpus:**  
To build a corpus of relevant articles, the algorithm uses `beautiful soup` to scrape multiple ACM Digital Library sources to build a dictionary of article information.   

**Ranking:**    
Using the corpus, the search engine then builds a file containing all the abstracts and article times. After creating an inverted index for the documents, `BM25` is used to rank the two individually to produce a list of the most relevant documents. To take into account credibility, the algorithm sorts the documents by citation and download count as well. Using these ranks, each document is assigned a score as follows:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. documents corresponding to the top 20 relevant abstracts will have `(20 - rank) * 0.40)` added to their score.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. documents corresponding to the top 20 relevant titles will have `(20-rank) * 0.40` added to their score.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. documents corresponding to the top 20 highest citation count will have `(20 - rank) * 0.10` added to their score.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. documents corresponding to the top 20 highest document count will have `(20 - rank) * 0.10` added to their score.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where rank is defined as where they fall on the respective top 20 lists.   

**Front End:**  
HTML & CSS was used to develop a search engine front end. Flask was used to connect the Python scripts to the HTML to have an interactive front end for the product.  

`getScores(query, topic)` is the overarching wrapper function that takes the passed in user query string and the corresponding topic integer to create a corpus, rank the articles, and return a sorted list of the top ten relevant articles for the given query.  

More documentation on each function can be seen in the respective Python files where  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; parse.py performs the web scraping  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; searching.py performs the necessary rankings  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ranking.py assigns the scores  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; views.py uses Flask to connect the HTML to the Python  
  
The topics are numbered as follows:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Software Foundations  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Algorithms and Models of Computation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Intelligence and Big Data  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. Human and Social Impact  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. Media  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6. Scientific, Parallel, and High Performance Computing  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7. Distributed Systems, Networking, and Security  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 8. Machines  

## software usage

The following packages need to be installed for the program:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; flask  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bs4  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lxml  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; metapy  
This can be done through `pip install -r requirements.txt`.  

To start the application, use `python run.py` and open the browser to the url provided by Flask. To run a search, enter any query and choose a topic from the drop down menu. On the results page, selecting an entry will redirect the user to a download link.  

**Examples of Queries to Run:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "vertex cover", Algorithms and Models of Computation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "interactive tutoring system", Human & Social Impact  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "graphics processing unit", Machines  

## contribution breakdown

The work was split evenly among group members. The following table shows a very brief breakdown of each group member’s contribution to the project.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Ria Nair:** developed front-end and connected to Python scripts using Flask  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Ann Rajan:** developed ranking algorithm & created demo video  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Kavya Varghese:** developed web scraping & ranking algorithm  
