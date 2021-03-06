from thyroid.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, \
                     ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from thyroid.util.util import read_yaml_file

import os

from thyroid.constant import *




class Configuration:
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        ) ->None:
        self.config_info = read_yaml_file(file_path = config_file_path)
        self.get_training_pipeline_config = self.get_training_pipeline_config()

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass

    def get_data_validation_config(self) ->DataValidationConfig:
        pass

    def get_data_transformation_config(self) ->DataTransformationConfig:
        pass

    def get_model_trainer_config(self) ->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) ->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        pass

