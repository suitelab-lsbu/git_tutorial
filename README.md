# Basic Calculator API
Complete the functions for the build test to pass

## Instructions to Complete
The functions should be shared among the team members such that each team member completes at least one function.

## Steps
* One member of the team (Student A) should `fork` the repository
* the other members should `clone` the repository from Student A
* each student completes at least one function and sends a `pull request` to student A
* Once all the functions has been `merged` to student A's repository, the build will pass

### Multiply function
* change the the `multiply` function in `app.py` to the following

```python
@app.route('/multiply/<a>/<b>', methods=['GET'])
def multiply(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a * b})
```

### Add Function
* change the the `add` function in `app.py` to the following

```python
@app.route('/add/<a>/<b>', methods=['GET'])
def add(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a + b})
```

### Subtract Function
* change the the `subtract` function in `app.py` to the following

```python
@app.route('/subtract/<a>/<b>', methods=['GET'])
def subtract(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    return jsonify({'result': a - b})
```

### Divide Function
* change the the `divide` function in `app.py` to the following

```python
@app.route('/divide/<a>/<b>', methods=['GET'])
def divide(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    if b == 0:
        return jsonify({'Value Error': "Cannot divide by zero"})
    return jsonify({'result': a / b})
```


### Modulus Function
* change the the `modulus` function in `app.py` to the following

```python
@app.route('/mod/<a>/<b>', methods=['GET'])
def modulus(a, b):
    try:
        a, b = float(a), float(b)
    except ValueError:
        return jsonify({'Value Error': "Only numbers Please"})
    if b == 0:
        return jsonify({'Value Error': "Cannot modulo by zero"})
    return jsonify({'result': a // b})
```