twitter_consumer_key = "i79vFSddTfJikvHHA3ztDSyli"
twitter_consumer_secret = "jQ3ipTewTYKU5tHy0Nyis6IG3sqAE3k80vfW1SfvO1viEcrJlo"
twitter_access_token = "1366285789215166467-hVpOD2tyg4ypyekvmoGfqHFmd0Gnyo"
twitter_access_secret = "PeMnD2UiMECGajyYE1DS0mXM9sCkH2JtPzeDgZw2l5QTu"

import twitter
from flask import Flask
from flask import request, render_template, redirect, url_for

app = Flask(__name__)

s = "123"
@app.route('/')
def hello_world():
    return 'Hello, World!'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token,
                          access_token_secret=twitter_access_secret)




def twitt():
    user_list = []
    id = 0
    users = ["@elonmusk", "@Ripple", "@ethereum", "@dogecoin", "@justinsuntron", "@whale_alert"]
    for user in users:
        id += 1
        query = user
        tweets = twitter_api.GetUserTimeline(screen_name=query, count=5, include_rts=True, exclude_replies=False)
        for tweet in tweets:
            text = tweet.text
            pubdate = tweet.created_at
            retweet = tweet.retweet_count
            user_list.append({'user' : user , 'text': text, 'pubdate': pubdate, 'retweet': retweet ,'id': id})
    return user_list


@app.route("/list", methods=["GET"])
def abc():
    id = request.args.get('id')
    if id is not None:
        return redirect(url_for("twitt_detail", idx=id))
    print(id)
    return render_template("new2.html")

@app.route("/view/<idx>", methods=["GET"])
def twitt_detail(idx):
    user_list = twitt()
    results = []
    for i in user_list:
        if i['id'] == int(idx):
            results.append(i)

    return render_template("detail.html", results=results)







if __name__ == "__main__":
    app.run(debug=True, port=9000)


