from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tape = ""
head = 0

# Helper functions for operations
def increment_binary(tape):
    head = len(tape) - 1
    new_tape = list(tape)
    carry = True
    while head >= 0 and carry:
        if new_tape[head] == '1':
            new_tape[head] = '0'
        else:
            new_tape[head] = '1'
            carry = False
        head -= 1
    if carry:
        new_tape.insert(0, '1')
    return ''.join(new_tape)

def check_palindrome(tape):
    return tape == tape[::-1]

def check_even_ones(tape):
    return tape.count('1') % 2 == 0

def find_ones_complement(tape):
    return ''.join('0' if bit == '1' else '1' for bit in tape)

def find_twos_complement(tape):
    ones_complement = find_ones_complement(tape)
    return increment_binary(ones_complement)

def decimal_to_binary(number):
    return bin(number)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_hexadecimal(number):
    return hex(number)[2:].upper()

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perform_action', methods=['POST'])
def perform_action():
    global tape
    action = request.json['action']
    tape = request.json['tape']
    
    if action == "increment_binary":
        result = increment_binary(tape)
    elif action == "check_palindrome":
        result = "Yes" if check_palindrome(tape) else "No"
    elif action == "check_even_ones":
        result = "Yes" if check_even_ones(tape) else "No"
    elif action == "ones_complement":
        result = find_ones_complement(tape)
    elif action == "twos_complement":
        result = find_twos_complement(tape)
    else:
        result = "Invalid action"

    return jsonify(result=result)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
