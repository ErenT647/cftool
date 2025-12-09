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

def get_user_subs(user):
    req = requests.get(f"https://codeforces.com/api/user.status?handle={user}")
    info = req.json()["result"]
    total_solved = 0
    month_solved = 0
    streak = 0
    max_streak = 0

    curr_time = datetime.now()
    last = curr_time
    curr_streak = 1
    for s in info:
        sub_time = datetime.fromtimestamp(int(s["creationTimeSeconds"]), tz=datetime.timezone(timedelta(hours=-6)))
        if s["verdict"] != "OK":
            continue
                
        total_solved += 1
        if sub_time.month == curr_time.month:
            month_solved += 1

        max_streak = max(max_streak, curr_streak)

        if timedelta(sub_time, curr_time).days < 1:
            streak = 1
            continue
        
        if timedelta(sub_time, curr_time) < 1:
            streak += 1
            curr_time = sub_time

        if timedelta(sub_time, last).days < 1:
            continue

        if timedelta(sub_time, last).days > 1:
            last = sub_time

        curr_streak += 1
        
        max_streak = max(max_streak, curr_streak)
    return {
        "maxStreak": max_streak,
        "streak": streak,
        "problemsSolved": total_solved,
        "problemsSolvedInLastMonth": month_solved
    }

