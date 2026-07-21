from flask import Flask, jsonify, render_template, request
print("1. Flask imported")

from flask_cors import CORS
print("2. Flask-CORS imported")

from db import cursor, connection
print("3. Database imported")

app = Flask(__name__)
print("4. App created")

CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


# GET
@app.route("/user", methods=["GET"])
def getUser():
    cursor.execute("SELECT * FROM user_table")
    data = cursor.fetchall()
    return jsonify(data)


# POST
@app.route("/user", methods=["POST"])
def addUser():
    data = request.get_json()

    eid = data["eid"]
    ename = data["ename"]
    email = data["email_id"]

    sql = """
    INSERT INTO user_table (eid, ename, email_id)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (eid, ename, email))
    connection.commit()

    return jsonify({"message": "User added successfully"})


# PUT
@app.route("/user/<int:eid>", methods=["PUT"])
def updateUser(eid):
    data = request.get_json()

    ename = data["ename"]
    email = data["email_id"]

    sql = """
    UPDATE user_table
    SET ename=%s,
        email_id=%s
    WHERE eid=%s
    """

    cursor.execute(sql, (ename, email, eid))
    connection.commit()

    return jsonify({"message": "User updated successfully"})


# PATCH
@app.route("/user/<int:eid>", methods=["PATCH"])
def patchUser(eid):
    data = request.get_json()

    if "ename" in data:
        cursor.execute(
            "UPDATE user_table SET ename=%s WHERE eid=%s",
            (data["ename"], eid)
        )

    if "email_id" in data:
        cursor.execute(
            "UPDATE user_table SET email_id=%s WHERE eid=%s",
            (data["email_id"], eid)
        )

    connection.commit()

    return jsonify({"message": "User patched successfully"})


# DELETE
@app.route("/user/<int:eid>", methods=["DELETE"])
def deleteUser(eid):
    cursor.execute("DELETE FROM user_table WHERE eid=%s", (eid,))
    connection.commit()

    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    print("5. Starting Flask Server...")
    app.run(debug=True)