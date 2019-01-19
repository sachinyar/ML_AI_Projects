from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder

builder = ComponentBuilder(use_cache=False)

def train_nlu(data, config_file, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(config_file), builder)
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'Restaurant_NPSR')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/Restaurant_NPSR', builder)
	print(interpreter.parse("show some chinese restaurant in Delhi"))
	
if __name__ == '__main__':
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()
