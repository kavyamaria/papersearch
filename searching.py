from parse import *

# takes dictionary of article information to create a file of abstracts
# for corpus
def createFileAbstract(dct):
    file = open("abstracts/abstracts.dat", "w+")
    for t in dct.keys():
        abs = dct[t]["abstract"]
        abs = abs.replace("\n", "") + "\n"
        file.write(abs)

# takes dictionary of article information to create a file of article titles
# for corpus
def createFileTitles(dct):
    file = open("titles/titles.dat", "w+")
    for t in dct.keys():
        t = t + "\n"
        file.write(t)

# takes user query string to create a file to be used by ranking functions
def createQueryFile(query):
    file = open("query.txt", "w+")
    file.write(query)

# takes dictionary of article information & returns list of tuples (docid, rank)
# where rank is defined by citation count
def sortCitations(dct):
    pairs = []
    count = 0
    for t in dct.keys():
        if "citations" not in dct[t].keys():
            num_citations = 0
        else:
            num_citations = int(dct[t]["citations"])
        pairs.append((count, num_citations))
        count += 1
    sorted_pairs = sorted(pairs, key=lambda tup: -tup[1])
    print("Citations:")
    print(sorted_pairs[:20])
    print()
    return sorted_pairs[:20]

# takes dictionary of article information & returns list of tuples (docid, rank)
# where rank is defined by download count
def sortDownloads(dct):
    pairs = []
    count = 0
    for t in dct.keys():
        if "downloads" not in dct[t].keys():
            num_downloads = 0
        else:
            num_downloads = dct[t]["downloads"]
            if num_downloads == "NA":
                num_downloads = 0
            else:
                num_downloads = int(num_downloads.replace(",", ""))
        pairs.append((count, num_downloads))
        count += 1
    sorted_pairs = sorted(pairs, key=lambda tup: -tup[1])
    print("Downloads:")
    print(sorted_pairs[:20])
    print()
    return sorted_pairs[:20]

# wrapper function that creates dictionary of article information & respective
# files
def createFiles(query, topic):
    results = searchsig(query.replace(" ", "+"), topic)

    createFileAbstract(results)
    createFileTitles(results)
    createQueryFile(query)

    return results

# function that uses BM25 to return a list of tuples (docid, rank) where rank
# is defined by abstract's relevance to user query
def rankAbstracts():
    cfg = "config_abstracts.toml"

    idx = metapy.index.make_inverted_index(cfg)
    ranker = metapy.index.OkapiBM25()

    query_path = "query.txt"

    query = metapy.index.Document()
    query_file=open(query_path)
    for query_num, line in enumerate(query_file):
        query.content(line.strip())
        res = ranker.score(idx, query, 20)
    query_file.close()
    shutil.rmtree("idx")
    print("Abstracts:")
    print(res)
    print()
    return res

# function that uses BM25 to return a list of tuples (docid, rank) where rank
# is defined by article title's relevance to user query
def rankTitles():
    cfg2 = "config_titles.toml"
    idx2 = metapy.index.make_inverted_index(cfg2)
    ranker = metapy.index.OkapiBM25()

    query_path = "query.txt"
    query = metapy.index.Document()
    query_file=open(query_path)
    for query_num, line in enumerate(query_file):
        query.content(line.strip())
        res2 = ranker.score(idx2, query, 20)
    query_file.close()
    shutil.rmtree("idx")
    print("Titles:")
    print(res2)
    print()

    return res2
