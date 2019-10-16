from flask import Flask, redirect, url_for, request
from utils import Trainer
from dictionary import samples
import numpy as np

app = Flask(__name__)


@app.route('/')
def hello():
    lessons = np.unique([x['lesson'] for x in samples])
    list_str = '<option value="0">all</option>'
    for x in lessons:
        list_str = list_str + '<option value="{}">{}</option>'.format(x, x)
    
    
    
    return '<form action = "start" method = "post"><p>pinin <input type = "checkbox", name="pinin"></p><p>hieroglyph<input type = "checkbox", name="hieroglyph"></p><p>translate <input type = "checkbox", name="translate"></p> <p>lesson <select name="lesson">{}</select></p><p><input type = "submit" value = "submit" /></p></form>'.format(list_str)
    #return "pinin <input type = 'checkbox'>"
    #return '<h1>{}</h1>'.format(samples[25]['hieroglyph'])
    
    
@app.route('/start', methods = ['POST', 'GET'])
def start():
    if request.method == 'POST':
        try:
            pinin = int(request.form['pinin'] == 'on')
        except:
            pinin = 0
        try:    
            hieroglyph = int(request.form['hieroglyph'] == 'on')
        except:
            hieroglyph = 0
        try:    
            translation = int(request.form['translate'] == 'on')
        except:
            translation = 0
            
#         pinin = int(request.form['pinin'] == 'on')
#         hieroglyph = int(request.form['hieroglyph'] == 'on')
#         translation = int(request.form['translate'] == 'on')
            
        lesson = request.form['lesson']
    
    if lesson != 0:
        lesson_samples = [x for x in samples if x['lesson'] == int(lesson)]
    else:
        lesson_samples = samples
        
    print_str = ''
    for x in lesson_samples:
        print_str = print_str + '<h1>{}</h1><h1>{}</h1><h1>{}</h1></br>'.format(x['pinin'], x['hieroglyph'], x['translate'])

    if int(lesson) != 0:
        idxs = np.where([x['lesson'] == int(lesson) for x in samples])[0]
        new_idx = np.random.choice(idxs)
    else:
        new_idx = np.random.randint(len(samples))
   
    return '<a href="/randomize/{}/{}/{}/{}/{}">randomize</a> {}'.format(pinin, hieroglyph, translation, lesson, new_idx, print_str)

    
@app.route('/randomize/<int:pinin>/<int:hieroglyph>/<int:translate>/<int:lesson>/<int:idx>')
def randomize(pinin, hieroglyph, translate, lesson, idx):
    mode = np.random.choice(np.array(['pinin', 'hieroglyph', 'translate'])[np.where([pinin, hieroglyph, translate])[0]])
    return '<a href="/answer/{}/{}/{}/{}/{}">answer</a><h1>{}</h1>'.format(pinin, hieroglyph, translate, lesson, idx, samples[idx][mode])


@app.route('/answer/<int:pinin>/<int:hieroglyph>/<int:translate>/<int:lesson>/<int:idx>')
def answer(pinin, hieroglyph, translate, lesson, idx):
    if lesson != 0:
        idxs = np.where([x['lesson'] == int(lesson) for x in samples])[0]
        new_idx = np.random.choice(idxs)
    else:
        new_idx = np.random.randint(len(samples))

    return '<a href="/randomize/{}/{}/{}/{}/{}">randomize</a><h1>{}</h1><h1>{}</h1><h1>{}</h1>'.format(pinin, hieroglyph, translate, lesson, new_idx, samples[idx]['pinin'], samples[idx]['hieroglyph'], samples[idx]['translate'])



# @app.route('/hello/<int:score>/<int:size>')
# def hello_name(score, size):
#     return "Hello World! {}_{}".format(score, size)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)
    
    
    
    
    