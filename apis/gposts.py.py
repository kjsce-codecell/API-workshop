from flask import Flask, jsonify
app = Flask(__name__)
data = [
    
  {
     
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipitsuscipit recusandae consequuntur expedita et cumreprehenderit molestiae ut ut quas totamnostrum rerum est autem sunt rem eveniet architecto"
  },
  
  {
     
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitaesequi sint nihil reprehenderit dolor beatae ea dolores nequefugiat blanditiis voluptate porro vel nihil molestiae ut reiciendisqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
     
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iurevoluptatem occaecati omnis eligendi aut advoluptatem doloribus vel accusantium quis pariaturmolestiae porro eius odio et labore et velit aut"
  },
  {
     
    "id": 4,
    "title": "eum et est occaecati",
    "body": "ullam et saepe reiciendis voluptatem adipisci sit amet autem assumenda provident rerum culpa quis hic commodi nesciunt rem tenetur doloremque ipsam iurequis sunt voluptatem rerum illo velit"
  },
  {
     
    "id": 5,
    "title": "nesciunt quas odio",
    "body": "repudiandae veniam quaerat sunt sed alias aut fugiat sit autem sed est voluptatem omnis possimus esse voluptatibus quisest aut tenetur dolor neque"
  }

]
@app.route('/<int:id>',methods=['GET'])
def hello_world(id):
    for d in data:
        if(d['id'] == id):
            return(jsonify(d))


@app.route('/post/<int:id>',methods=['GET','POST'])
def hello(id):
    for d in data:
        if id == d['id']:
            return ("Id already taken, take some other id")
    post={"id":id,
    "title":"hello",
    "body":"Hello Brother"
    } 
    data.append(post)
    return jsonify(data[-1])

@app.route('/all',methods=['GET'])
def helloworld():
    return jsonify(data)
    
