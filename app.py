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

    id = data["id"]
    name = data["name"]
    email = data["email_id"]

    sql = """
    INSERT INTO user_table (id, name, email_id)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (id, name, email))
    connection.commit()

    return jsonify({"message": "User added successfully"})


# PUT
@app.route("/user/<int:id>", methods=["PUT"])
def updateUser(id):
    data = request.get_json()

    name = data["name"]
    email = data["email_id"]

    sql = """
    UPDATE user_table
    SET name=%s,
        email_id=%s
    WHERE id=%s
    """

    cursor.execute(sql, (name, email, id))
    connection.commit()

    return jsonify({"message": "User updated successfully"})


# PATCH
@app.route("/user/<int:id>", methods=["PATCH"])
def patchUser(id):
    data = request.get_json()

    if "name" in data:
        cursor.execute(
            "UPDATE user_table SET name=%s WHERE id=%s",
            (data["name"], id)
        )

    if "email_id" in data:
        cursor.execute(
            "UPDATE user_table SET email_id=%s WHERE id=%s",
            (data["email_id"], id)
        )

    connection.commit()

    return jsonify({"message": "User patched successfully"})


# DELETE
@app.route("/user/<int:id>", methods=["DELETE"])
def deleteUser(id):
    cursor.execute("DELETE FROM user_table WHERE id=%s", (id,))
    connection.commit()

    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    print("5. Starting Flask Server...")
    app.run(debug=True)