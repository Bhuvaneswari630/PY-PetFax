from flask import ( Blueprint, render_template, request, redirect)
import json

bp = Blueprint('facts',
                __name__, 
                url_prefix='/facts')

@bp.route('/new')
def new_facts_form():
     return render_template(
        'new_facts_form.html'
    )