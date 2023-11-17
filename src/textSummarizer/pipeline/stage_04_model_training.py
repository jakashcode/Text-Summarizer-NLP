

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modeltraining import ModelTrainer

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
 



 