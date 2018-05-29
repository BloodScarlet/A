from flask import Flask, request, jsonify
import json
import pymysql, requests

app = Flask(__name__)
data = json.load(open("../config.json"))
passw = data["dbpass"]
webhook = data["votehook"]

def update(user):
    try:
        connection = pymysql.connect(host="localhost", user="root", password=passw,
                                    db="hentaiboi", port=3306)
        db = connection.cursor()
        db.execute(f"INSERT INTO votes VALUES ({user})")
        connection.commit()
    except Exception as e:
        print(e)
    webhook_post(user)

def webhook_post(user):
    try:
        payload = {
            "embeds": [{
                "title": "Vote",
                "description": f"<@{user}> has voted!",
                "color": 9174919
            }]
        }
        res = requests.post(webhook, json=payload)
        print(f"Posted to webhook! {res.status_code}")
    except Exception as e:
        print(f"Failed to POST Webhook, {e}")

@app.route("/", methods=['POST'])
def on_push():
    data = request.data
    data = data.decode("utf-8")
    data = json.loads(data)
    try:
        update(data['user'])
    except Exception as e:
        print("Failed to update, {}".format(e))

    return jsonify({'success': True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
