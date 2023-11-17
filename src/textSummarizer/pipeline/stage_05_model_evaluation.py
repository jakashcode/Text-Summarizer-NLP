from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.modelevaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()