import tweetAnalizer
import tweetGetter

#ID's de Meade, AMLO, Anaya y Margarita
subjects = [237372254, 82119937, 151968088, 97017966]

subjectNames = ["@JoseAMeadeK", "@lopezobrador_", "@RicardoAnayaC", "@Mzavalagc"]

for subjectIndex in range(len(subjects)):
    subject = subjects[subjectIndex]
    account = accountGetter(subject)
    tweetMentions = getMentions(subject)
    repliesDictionary = {}
    for tweet in account.tweets:
        repliesDictionary[tweet.id] = []
        for mention in tweetMentions:
            if(mention.in_reply_to_status_id == tweet.id):
                repliesDictionary[tweet.id].append(mention.id)
    writeJSON(repliesDictionary, subjectNames[subjectIndex]+ "_replies")
                
        
