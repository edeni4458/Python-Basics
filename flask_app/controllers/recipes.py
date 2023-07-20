from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.recipe import Recipe

@app.route('/recipes')
def recipes():
    
    return render_template('recipes.html', recipes=Recipe.get_all())

@app.route('/recipes/new')
def new_recipe():
    return render_template("new_recipe.html")


@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    print (request.form)
    Recipe.save(request.form)
    return redirect('/recipes')


@app.route("/recipes/edit_recipes/<int:id>")
def edit_recipe(id):
    data = {'id': id}
    return render_template("edit_recipes.html", recipe = Recipe.get_one_with_users(data))


@app.route('/recipes/show_recipes/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template("show.html", recipe = Recipe.get_one_with_users(data))

@app.route('/recipes/delete_recipes/<int:id>')
def delete_recipe(id):
    Recipe.delete({'id':id})
    return redirect("/recipes")

@app.route('/edit_recipes', methods = ["POST"])
def update2_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit_recipes/{request.form['id']}")
    Recipe.update(request.form)
    return redirect('/recipes') 
