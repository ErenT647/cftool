import requests
import json


def get_user_rating(user):
    return get_user_info(user)["rank"]

def get_user_solved(user):
    pass

def get_user_pending(user):
    pass

def get_templates(idx):
    pass

def get_contest_progress(sub):
    #require: 
    #handle, contest id
    req = requests.get(f"https://codeforces.com/api/contest.standings?contestId={sub["contestId"]}&handles={sub["handles"]}&showUnofficial=true")

    info = req.json()["result"]["rows"][0]

    infoq = info["problemResults"]

    #print(infoq)

    cnt = 0
    rejected = []
    i = 0
    for s in infoq:
        status = "NOT ATTEMPTED"
        if s["rejectedAttemptCount"] > 0:
            status = "WRONG ANSWER"
        if s["points"] > 0:
            status = "ACCEPTED"
        rejected.append({
            "problem": i,
            "rejectedAttempts": s["rejectedAttemptCount"],
            "status": status
        })
        if s["points"] > 0:
            cnt += 1
        i += 1
    return {
        "place": info["rank"],
        "points": info["points"],
        "penalty": info["penalty"],
        "detailedBreakdown": rejected,
        "numberSolved": cnt
    }

def get_user_info(user):
    req = requests.get(f"https://codeforces.com/api/user.info?handles={user};&checkHistoricHandles=false")
    info = req.json()["result"][0]
    return {
        "rating": info["rating"],
        "rank": info["rank"],
        "maxRank": info["maxRank"],
        "organization": info["organization"]
    }
