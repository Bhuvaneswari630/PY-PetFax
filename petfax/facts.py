from flask import ( Blueprint, render_template, request, redirect)
from . import models
import json

bp = Blueprint('facts',
                __name__, 
                url_prefix='/facts')

@bp.route('/')
def index():
     results = models.Fact.query.all()
     for result in results:
          print(result)
          
     return render_template(
        'facts/index.html', facts=results
    )

@bp.route('/<fact_id>', methods=['GET','DELETE', 'POST'])
def delete(fact_id):
      fact = models.Fact.query.get(fact_id)
      if request.method == 'GET':
        #   render edit form
          url = f"/facts/{fact_id}" if fact else ''
          return render_template('facts/new_facts_form.html', fact=fact, url=url)
        #   delete fact
      elif request.method == 'DELETE':
        models.db.session.delete(fact) 
        #  update db 
      else:
        fact.submitter = request.form['submitter']
        fact.fact = request.form['fact']

      models.db.session.commit()
      return redirect('/facts')

@bp.route('/new', methods=['GET', 'POST'])
def new_facts_form():
     if request.method == 'POST':
          submitter = request.form['submitter']
          fact = request.form['fact']
          new_fact = models.Fact(submitter=submitter, fact=fact)
          models.db.session.add(new_fact)  
          models.db.session.commit()
          return redirect('/facts')
     
     
     return render_template(
        'facts/new_facts_form.html'
    )