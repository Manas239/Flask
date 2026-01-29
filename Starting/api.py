### Put and delete
### Working with API's --- Json
from flask import Flask, request, jsonify

app = Flask(__name__)

##initial data in to do list

items = [
    {"id": 1, "name": "item 1","Discription": "this is item 1"},
    {"id": 2, "name": "item 2","Discription": "this is item 2"},
]

@app.route("/")
def home():
    return "Welcome to the sampple  To-Do List APP"

##Get: retrive all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

##Get: retrive specipic item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):

    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"message":"Item not found"}),404
    return jsonify(item)

## Post : create new task
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"message":"Invalid data"}),400
    
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "Discription": request.json.get("Discription")
    }
    items.append(new_item)
    return jsonify(new_item),201


## Put : update existing item/task
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item= next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"message":"Item not found"}),404
    item["name"] = request.json.get("name", item["name"])
    item["Discription"] = request.json.get("Discription", item["Discription"])
    return jsonify(item)

## Delete : delete existing item/task
@app.route("/items/<int:item_id>", methods=["DELETE"])  
def delete_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"message":"Item not found"}),404
    items.remove(item)
    return jsonify({"message":"Item deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)