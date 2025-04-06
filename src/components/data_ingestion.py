# this file involves reading the data from the csv file and converting it into a pandas dataframe
# and then converting it into a numpy array
# and then converting it into a list and dividing it into train and test data

# now all eda code should be done in this components folder to have CI/CD implemented

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# just to test DataTransformation
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
# just to test DataTransformation

# just to test the model trainer file
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig
# just to test the model trainer file

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')
            return (
                self.config.train_data_path,
                self.config.test_data_path,
                self.config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys) from e
        

# if __name__ == "__main__":
#     obj = DataIngestion()
#     # obj.initiate_data_ingestion()
#     train_data, test_data = obj.initiate_data_ingestion()

#     data_transformation = DataTransformation()
#     data_transformation.initiate_data_transformation(train_data, test_data)

# just to test the DataTransformation file
# if __name__ == "__main__":
#     obj = DataIngestion()
#     train_data, test_data, raw_data = obj.initiate_data_ingestion()

#     data_transformation = DataTransformation()
#     data_transformation.initiate_data_transformation(train_data, test_data)
# just to test the DataTransformation file

# just to test the model trainer file
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    ModelTrainer = ModelTrainer()
    print(ModelTrainer.initiate_model_trainer(train_arr, test_arr)) # 0.8795158595242263 is the r2 score
# Now run the file data_ingestion.py
# just to test the model trainer file