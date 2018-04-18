from urllib.request import urlopen, Request

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

def setup():
    query = "peer+instruction"
    req = Request("https://dl.acm.org/results.cfm?within=owners.owner%3DHOSTED&srt=_score&query=" +
        query + "&Go.x=0&Go.y=0", headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "lxml")
    #print(soup.prettify())
    results = {}
    x = soup.find_all("div", class_="title")
    for t in range(len(x)):
        results[t] = {}
        results[t]["title"] = x[t].a.get_text()
    x = soup.find_all("div", class_="authors")
    for t in range(len(x)):
        a = x[t].findAll('a')
        at = []
        for r in a:
            at.append(r.get_text())
        results[t]["authors"] = at
    x = soup.find_all("div", class_="source")
    for t in range(len(x)):
        a = x[t].findAll("span")
        results[t]["publication date"] = a[0].get_text()
        if len(a) > 1:
            results[t]["paper"] = a[1].get_text()
        else:
            results[t]["paper"] = "NA"
    x = soup.find_all("div", class_="publisher")
    for t in range(len(x)):
        results[t]["publisher"] = (x[t].get_text().replace("\nPublisher: ", "")).replace("\n", "")
    x = soup.find_all("div", class_="metricsCol2")
    for t in range(len(x)):
        results[t]["citations"] = x[t].find('span', class_="citedCount").text.replace("Citation Count: ", "")
        results[t]["downloads"] = x[t].find('span', class_="downloadAll")
        if results[t]["downloads"] != None:
            results[t]["downloads"] = results[t]["downloads"].text.replace("Downloads (Overall): ", "")
        else:
            results[t]["downloads"] = "NA"
    x = soup.find_all("div", class_="abstract")
    for t in range(len(x)):
        results[t]["abstract"] = x[t].get_text()
    #x = soup.find_all("div", class_="ft")
    #for t in range(len(x)):
        #results[t]["href"] = x[t].a['href']
    return results

def printit(dct):
    for t in dct.keys():
        r = dct[t]
        print(r["title"])
        print("\t" + str(r["authors"]))
        print("\t" + r["publication date"])
        print("\t" + r["paper"])
        print("\tPublisher: " + r["publisher"])
        print("\tNumber of Citations: " + r["citations"])
        print("\tNumber of Downloads: " + r["downloads"])
        if "abstract" in r.keys():
            print("\t" + r["abstract"])
        #print("\t" + r["href"])
        print()

results = setup()
printit(results)
