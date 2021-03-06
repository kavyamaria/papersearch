from searching import *
from parse import *

# function that adds score to the respective article's dictionary for
# the top ten results
def getFinalResults(lines, score, results):
    scores = list(zip(lines, score))
    sorted_scores = sorted(scores, key=lambda tup: -tup[1])
    final_results = [{}] * 10

    for t in range(10):
        dct = results[sorted_scores[t][0]]
        dct["title"] = sorted_scores[t][0]
        dct["score"] = sorted_scores[t][1]
        final_results[t] = dct

    return final_results

# function that uses lists of tuples to assign a weighted score to each
# article in dictionary of articles & returns the top ten final results
def rankResults(abstract, title, citation, download, results):
    with open('titles/titles.dat') as f:
        lines = f.read().splitlines()

    score = [0] * len(lines)
    size = min(len(abstract), len(title), len(citation))
    for x in range(size):
        score_val = 20 - x
        score[abstract[x][0]] += score_val * .4
        score[title[x][0]] += score_val * .4
        score[citation[x][0]] += score_val * .1
        score[download[x][0]] += score_val * .1

    finalResults = getFinalResults(lines, score, results)

    return finalResults

# function that takes a user string & topic (int) to return the top ten
# final results
# wrapper function -- the only function that needs to be called
# the topics & their corresponding number is as follows:
    # 1. Software Foundations
    # 2. Algorithms and Models of Computation
    # 3. Intelligence and Big Data
    # 4. Human and Social Impact
    # 5. Media
    # 6. Scientific, Parallel, and High Performance Computing
    # 7. Distributed Systems, Networking, and Security
    # 8. Machines
def getScores(query, topic):
    results = createFiles(query, topic)

    sortedAbstracts = rankAbstracts()
    sortedTitles = rankTitles()

    sortedCitations = sortCitations(results)
    sortedDownloads = sortDownloads(results)

    scores = rankResults(sortedAbstracts, sortedTitles,
        sortedCitations, sortedDownloads, results)

    return scores

if __name__ == "__main__":
    scores = getScores("peer instruction", 4)

    for x in scores:
        print(x["title"], x["score"])
