from flask import Flask, jsonify
import math

app = Flask(__name__)

def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    integral = 0.0
    for i in range(N):
        x0 = lower + i * dx
        x1 = lower + (i + 1) * dx
        midpoint = (x0 + x1) / 2
        height = abs(math.sin(midpoint))
        integral += height * dx
    return integral

@app.route('/numericalintegralservice/<lower>/<upper>')
def calculate_integral(lower, upper):
    intervals = [(float(lower), float(upper))]
    results = {}
    for interval in intervals:
        lower, upper = interval
        for N in [10, 100, 100, 1000, 10000, 100000, 1000000]:
            result = numerical_integration(lower, upper, N)
            results[f"N={N}"] = result
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
