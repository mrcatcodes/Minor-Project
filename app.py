from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/recommend', methods=['POST'])
def get_investment_recommendation():
    data = request.get_json()
    income = data.get('income')
    risk_tolerance = data.get('risk_tolerance')

    # Replace with your actual recommendation logic
    if risk_tolerance == 'low':
        recommendation = "Consider low-risk options like savings accounts or government bonds."
    elif risk_tolerance == 'medium':
        recommendation = "Explore options like index funds or mutual funds with moderate risk."
    elif risk_tolerance == 'high':
        recommendation = "Consider investing in stocks or higher-risk assets."
    else:
        recommendation = "Invalid risk tolerance."

    return jsonify({'recommendation': recommendation})

@app.route('/track_expenses', methods=['POST'])
def track_expense():
    data = request.get_json()
    income = data.get('income', 0.0)
    expenses = data.get('expenses', []) 
    savings_goal = data.get('savings_goal', 0.0)

    total_expenses = sum(expense['amount'] for expense in expenses)
    savings = income - total_expenses
    advice = "You are on track with your savings!" if savings >= savings_goal else f"You need to save {savings_goal - savings} more."

    return jsonify({'total_expenses': total_expenses, 'savings': savings, 'advice': advice})

if __name__ == '__main__':
    app.run(debug=True)