from .HandleBankStatement import HandleBankStatement
from flask import Flask


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    result = str(''.join(str(e) for e in HandleBankStatement.handle_bankstatement()))

    return str("<html><head></head><body>"+result+"</body></html>")
