# MLPipeline
This project aims to build a library that gives the framework to create [Spark](https://spark.apache.org) pipelines without coding, just by using a configuration file.

Spark [pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html) are used to combine multiple algorithms into a single pipeline, or workflow.

 ## Tasks 
 The goal is to be able to do the following things only with a single config file:
 * [DONE] Create pipelines with multiple stages
 * [DONE] Set stages' attributes
 * [DONE] Perform pipeline steps
    * [DONE] fit, transform (predict)
    * [DONE] save, load
 * [DONE] Dataset operations: 
    * [DONE] load, transform
    * [TODO] save 
 * [TODO] Perform cross validation on a pipeline 
 * [TODO] Perform hyper-parameter tuning on a pipeline 
 * [TODO] Load config from different sources: JSON, YAML.. 
 * [TODO] Combine all these functionalities in one python library
 
 ## Step configuration
 
```
step_config = {
    "name": step_name,
    "params": step_params,
    "stage": step_stage
}
```

* ``step_name`` is the name of the method that will be executed on the step stage (i.e ``fit``, ``transform``, ``save``, ``load``)
* ``step_params`` are the params of the method that will be executed (i.e dataset)
* ``step_stage`` is the stage to execute the step on. The stage could be the output of another step

## Stage configuration

```
stage_config = {
        "name": stage_name,
        "params": stage_params 
}
```

* ``stage_name`` is the name of the stage that will be created. It must have the package paths relative to ``pyspark.ml`` (i.e ``feature.Tokenizer``, ``classification.LogisticRegression``)
* ``stage_params`` are the params of the stage (i.e input and utput columns)