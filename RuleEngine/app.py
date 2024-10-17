from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule
from models import db, Rule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
db.init_app(app)

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    data = request.json
    rule_string = data.get('rule_string')
    ast = create_rule(rule_string)
    # Store the rule in the database if needed
    return jsonify({"ast": ast.__dict__}), 201

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": combined_ast.__dict__}), 200

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    data = request.json
    # Make sure to parse AST correctly if needed
    attributes = data.get('attributes')
    ast = data.get('ast')  # You might want to convert back from JSON to Node
    result = evaluate_rule(ast, attributes)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
