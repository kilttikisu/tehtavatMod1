from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Reitti: http://127.0.0.1:3000/alkuluku/<numero>
@app.route('/alkuluku/<int:numero>', methods=['GET'])
def tarkista_alkuluku(numero):
    tulos = on_alkuluku(numero)
    return jsonify({"Number": numero, "isPrime": tulos})

if __name__ == '__main__':
    app.run(port=3000, debug=True)
