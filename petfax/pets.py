from flask import ( Blueprint, render_template, request, redirect)
import json


bp = Blueprint('pets',
                __name__, 
                url_prefix='/pets')

@bp.route('/')
def index(): 
    pets = json.load(open('pets.json'))
    print(pets)
    return render_template(
        'index.html',
        pets=pets,
        title='This is Petfax'
    )

@bp.route('/<int:index>')
def show_pet(index):
    pet = json.load(open('pets.json'))[index]
    return render_template(
        'show_pet.html',
        pet=pet
    ) 

@bp.route('/adopt', methods=['POST'])
def adopt():
    print(request.form)
    # return 'You have adopted a pet'
    return redirect('/pets')
