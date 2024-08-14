# from signlanguage.logger import logging
# from signlanguage.exception import SignException
# import sys


# # logging.info("Hello  ") 

# try :
#    a= 7/'9'
# except Exception as e:
#     raise SignException("Error occurred", sys) from e  


from signlanguage.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline() 
