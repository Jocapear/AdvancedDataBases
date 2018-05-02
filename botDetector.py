import tweetAnalizer
import tweetGetter
import json
from tweetGetter import accountGetter
from tweetGetter import getMentions
from tweetGetter import writeJSON
from tweetAnalizer import isBot
from tweetGetter import accountGetterNoWritting
#ID's de Meade, AMLO, Anaya y Margarita
subjects = [237372254, 82119937, 151968088, 97017966]

subjectNames = ["@JoseAMeadeK", "@lopezobrador_", "@RicardoAnayaC", "@Mzavalagc"]

scoresDictionary = {}

scores = json.load(open("complete_scores" + ".json"))
for subjectIndex in range(len(subjects)):
    print("--------------- Analysing " + subjectNames[subjectIndex] + "--------------------" )
    subject = subjects[subjectIndex]
    subjectName = subjectNames[subjectIndex]
    account = accountGetter(subject)
    tweetMentions = getMentions(subjectName)
    print("Menciones encontradas " + str(len(tweetMentions)))

    for tweetStr in account["tweets"]:
        tweet = json.loads(tweetStr)
        if not tweet["id"] in scores[subjectName]:  
            scores[subjectName][tweet["id"]] = {}
        print("Tweet " + str(tweet["id"]))
        for mentionStr in tweetMentions:
            mention = json.loads(mentionStr)
            if(mention["in_reply_to_status_id"] == tweet["id"]):

                suspect = accountGetterNoWritting(mention["user"]["id"])

                score = isBot(suspect)
                scores[subjectName][tweet["id"]][mention["user"]["screen_name"]] = score
                print("     Mention found from " + str(mention["user"]["screen_name"]) + " with a score of " + str(score))
writeJSON(scores, "complete_scores")

        
