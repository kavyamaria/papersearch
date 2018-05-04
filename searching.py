from parse import *

def createFileAbstract(dct):
    file = open("abstracts/abstracts.dat", "w+")
    for t in dct.keys():
        abs = dct[t]["abstract"]
        abs = abs.replace("\n", "") + "\n"
        file.write(abs)

def createFileTitles(dct):
    file = open("titles/titles.dat", "w+")
    for t in dct.keys():
        t = t + "\n"
        file.write(t)

def createQueryFile(query):
    file = open("query.txt", "w+")
    file.write(query)

def sortCitations(dct):
    # assuming doc index starts at 1
    pairs = []
    count = 1
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

def sortDownloads(dct):
    pairs = []
    count = 1
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

def createFiles(query, topic):
    results = searchsig(query.replace(" ", "+"), topic)

    createFileAbstract(results)
    createFileTitles(results)
    createQueryFile(query)

    return results

def rankAbstracts():
    cfg = "config_abstracts.toml"

    idx = metapy.index.make_inverted_index(cfg)
    ranker = metapy.index.OkapiBM25()

    query_path = "query.txt"

    query = metapy.index.Document()
    with open(query_path) as query_file:
        for query_num, line in enumerate(query_file):
            query.content(line.strip())
            res = ranker.score(idx, query, 20)
    shutil.rmtree("idx")
    print("Abstracts:")
    print(res)
    print()
    return res

def rankTitles():
    cfg2 = "config_titles.toml"
    idx2 = metapy.index.make_inverted_index(cfg2)
    ranker = metapy.index.OkapiBM25()

    query_path = "query.txt"
    query = metapy.index.Document()
    with open(query_path) as query_file:
        for query_num, line in enumerate(query_file):
            query.content(line.strip())
            res2 = ranker.score(idx2, query, 20)
    shutil.rmtree("idx")
    print("Titles:")
    print(res2)
    print()

    return res2
