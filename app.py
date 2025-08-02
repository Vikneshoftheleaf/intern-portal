from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('dashboard.html')

@app.route("/login")
def login():
    return render_template('login.html')
    
@app.route("/signup")
def signup():
    return render_template('signup.html')
    
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/api/leaderboard')
def leaderboard_api():
    res = requests.get("https://randomuser.me/api/?results=10")
    users = res.json()['results']

    leaderboard = []
    for i, user in enumerate(users):
        leaderboard.append({
            "position": i + 1,
            "name": f"{user['name']['first']} {user['name']['last']}",
            "image_url": user['picture']['large'],
            "no_of_donations": (10 - i) * 2,
            "total_donation": (10 - i) * 500
        })

    return jsonify(leaderboard)

@app.route('/api/dashboard')
def dashboard_data():
    return jsonify({
        "profile": {
            "name": "Aarav Mehta",
            "email": "aarav.mehta@example.com",
            "image_url": "https://randomuser.me/api/portraits/men/45.jpg",
            "member_since": "2022-04-15",
            "referal_code":"mehta@2025"
        },
        "donation": {
            "total_donations": 12,
            "total_amount": 7200,
            "last_donation": "2025-07-25"
        },
        "rewards": {
            "total_rewards": 5,
            "items": [
                {
                    "name": "Top Donor",
                    "image_url": "https://img.icons8.com/color/96/crown.png"
                },
                {
                    "name": "Early Supporter",
                    "image_url": "https://img.icons8.com/color/96/medal2.png"
                },
                {
                    "name": "Monthly Giver",
                    "image_url": "https://img.icons8.com/color/96/gift.png"
                },
                {
      "name": "Consistent Contributor",
      "image_url": "https://img.icons8.com/color/96/star.png"
    },
    
                
                
            ]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
    
    