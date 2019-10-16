from dictionary import samples
from IPython.display import Markdown, display
import numpy as np

def printmd(string):
    display(Markdown(string))

    
    
class Trainer:
    def __init__(self, mode_list=['pinin', 'hieroglyph', 'translate']):
        self.mode_list = mode_list
        self.dictionary = samples
        self.curr_sample = None
        
    def random_question(self):
        self.curr_sample = np.random.choice(samples)
        mode = np.random.choice(self.mode_list)
        return self.curr_sample[mode]
        #printmd('# {}'.format(self.curr_sample[mode]))
        
    def answer(self):
        return self.curr_sample
        printmd('# {}\n # {}\n # {}'.format(self.curr_sample['hieroglyph'], self.curr_sample['pinin'], self.curr_sample['translate']))
        
        
        
        