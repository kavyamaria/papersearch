from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import os

def search(query, link1, link2):
    req = Request(link1 + query + link2, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "lxml")
    #print(soup.prettify())
    results = {}
    x = soup.find_all("div", class_="title")
    titles = []
    for t in range(len(x)):
        tl = x[t].a.get_text()
        titles.append(tl)
        results[tl] = {}
        results[tl]["citation link"] = "https://dl.acm.org/" + x[t].a['href']
    x = soup.find_all("div", class_="authors")
    for t in range(len(x)):
        a = x[t].findAll('a')
        at = []
        for r in a:
            at.append(r.get_text())
        results[titles[t]]["authors"] = at
    x = soup.find_all("div", class_="source")
    for t in range(len(x)):
        a = x[t].findAll("span")
        results[titles[t]]["publication date"] = a[0].get_text()
        if len(a) > 1:
            results[titles[t]]["paper"] = a[1].get_text()
        else:
            results[titles[t]]["paper"] = "NA"
    x = soup.find_all("div", class_="publisher")
    for t in range(len(x)):
        results[titles[t]]["publisher"] = (x[t].get_text().replace("\nPublisher: ", "")).replace("\n", "")
    x = soup.find_all("div", class_="metricsCol2")
    for t in range(len(x)):
        results[titles[t]]["citations"] = x[t].find('span', class_="citedCount").text.replace("Citation Count: ", "")
        results[titles[t]]["downloads"] = x[t].find('span', class_="downloadAll")
        if results[titles[t]]["downloads"] != None:
            results[titles[t]]["downloads"] = results[titles[t]]["downloads"].text.replace("Downloads (Overall): ", "")
        else:
            results[titles[t]]["downloads"] = "NA"
    x = soup.find_all("div", class_="abstract")
    for t in range(len(x)):
        results[titles[t]]["abstract"] = x[t].get_text()
    return results

def printit(dct):
    c = 0
    for t in dct.keys():
        r = dct[t]
        print(t)
        #print(r["title"])
        print("\t" + str(r["authors"]))
        print("\t" + r["publication date"])
        print("\t" + r["paper"])
        print("\tPublisher: " + r["publisher"])
        print("\tNumber of Citations: " + r["citations"])
        print("\tNumber of Downloads: " + r["downloads"])
        if "abstract" in r.keys():
            print("\t" + r["abstract"])
        print("\t" + r["citation link"])
        print()
        c += 1
        if c == 5:
            break

def searchsig(query, ipt):
    link1 = "https://dl.acm.org/results.cfm?within=owners.owner%3DHOSTED&srt=_score&query="
    link2 = "&Go.x=0&Go.y=0"
    r = search(query, link1, link2)
    res = r

    if ipt == 1:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP950&withindisp=SIGSOFT&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP946&withindisp=SIGPLAN&query"
        r = search(query, link1, link2)

        res.update(r)
    elif ipt == 2:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP914&withindisp=SIGACT&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP5335&withindisp=SIGLOG&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 3:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP918&withindisp=SIGAI&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP935&withindisp=SIGIR&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP939&withindisp=SIGMIS&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 4:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP1530&withindisp=SIGACCESS&query="
        link2 = "&Go.x=31&Go.y=13"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP922&withindisp=SIGCAS&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP923&withindisp=SIGCHI&query"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP927&withindisp=SIGCSE&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP947&withindisp=SIGSAC&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 5:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP923&withindisp=SIGCHI&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP932&withindisp=SIGGRAPH&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP940&withindisp=SIGMM&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP949&withindisp=SIGSIM&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 6:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP916&withindisp=SIGAPP&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP1481&withindisp=SIGBED&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP4767&withindisp=SIGHPC&query="
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP945&withindisp=SIGOPS&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 7:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP1481&withindisp=SIGBED&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP947&withindisp=SIGSAC&query="
        r = search(query, link1, link2)
        res.update(r)

    elif ipt == 8:
        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP917&withindisp=SIGARCH&query="
        link2 = "&Go.x=0&Go.y=0"
        r = search(query, link1, link2)
        res.update(r)

        link1 = "https://dl.acm.org/results.cfm?within=sponsors.sponsorID%3DSP938&withindisp=SIGMICRO&query="
        r = search(query, link1, link2)
        res.update(r)

    return res

if __name__ == "__main__":
    #print("Search within a topic (input only the digit of the topic you want):")
    #print("1. Software Foundations")
    #print("2. Algorithms and Models of Computation")
    #print("3. Intelligence & Big Data")
    #print("4. Human & Social Impact")
    #print("5. Media")
    #print("6. Scientific, Parallel, & High Performance Computing")
    #print("7. Distributed Systems, Networking, & Security")
    #print("8. Machines")
    #ipt = int(input("Search within a topic (input only the digit of the topic you want): "))
    #query = input("Query: ").replace(" ", "+")
    results = searchsig("drones", 3)
