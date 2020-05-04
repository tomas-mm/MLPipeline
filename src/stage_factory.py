from pyspark.ml import *


class StageFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_stage(name: str):
        expr = name + "()"
        return eval(expr)

    @staticmethod
    def set_params(stage, params):
        if not params:
            # Set default params
            stage.setParams()
        else:
            if isinstance(stage, Pipeline):
                params["stages"] = [StageFactory.create_stage(s_conf) for s_conf in params["stages"]]
            stage.setParams(**params)

    @staticmethod
    def create_stage(stage_conf):
        if not isinstance(stage_conf, dict):
            # Stage conf is already a stage
            return stage_conf

        name = stage_conf["name"]
        params = stage_conf["params"]

        stage = StageFactory.get_stage(name)
        StageFactory.set_params(stage, params)

        return stage
