from voting_app import app

voting_app.secret_key = '6dbf23122cb5046cc5c0c1b245c75f8e43c59ca8ffeac292715e5078e631d0c9'
voting_app.config['SESSION_TYPE'] = 'filesystem'

voting_app.run(debug=True, port=8080)