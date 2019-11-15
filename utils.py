from dictionary import samples
from IPython.display import Markdown, display
import numpy as np

def printmd(string):
    display(Markdown(string))

    
    
class Trainer:
    def __init__(self, lessons=None, mode_list=['pinin', 'hieroglyph', 'translate']):
        self.mode_list = mode_list
        self.lessons = lessons
        self.dictionary = [x for x in samples if x['lesson'] in self.lessons or len(lessons) == 0]
        self.curr_sample = None
        
    def random_question(self):
        self.curr_sample = np.random.choice(self.dictionary)
        mode = np.random.choice(self.mode_list)
        #return self.curr_sample[mode]
        printmd('# {}'.format(self.curr_sample[mode]))
        
    def answer(self):
        #return self.curr_sample
        printmd('# {}\n # {}\n # {}'.format(self.curr_sample['hieroglyph'], self.curr_sample['pinin'], self.curr_sample['translate']))
        
        
        
        