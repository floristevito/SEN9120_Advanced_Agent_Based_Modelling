Created by Group 22:
|Name|Student Number|
| --- | :-- |
|Floris Boendermaker|4655605|
|Bram Boereboom|4556232|
|Bruno Hermans|4690435|

# SEN9120 Advanced Agent Based Modelling
 Repository for model made in regard to the TU Delft Master course SEN9120 Advanced Agent Based Modelling
 
## Folder Structure 
An overview of the main structure of this submission folder is shown below. 
```
├── README.md         <- you are here    
├── model             <- main directory that holds all model files and tests
    ├── model.py           <- includes the overall model instance
    ├── components.py      <- includes all model components, such as EVs and municipalities
├── data              <- all data files, both input and output    
├── figures           <- all generated figures for the report   
├── geo_files         <- input spatial data  
├── report            <- full Latex report code
```
## Requirements
This project uses Python version 3.9. All requirements can be found in the requirements.txt file in the root folder of this directory, and can be installed using pip with the following command.

`pip install -r requirements.txt`

## Running the model
The model can be run from the model directory. 

To perform a single run with settings specified in params.json:

`model_run.py`

*Note that all model logs are saved in the automatically created model.log file in the working directory.*

To run multiple experiments (we have devided it into 3 experiment files, so they could be split over multiple virtual machines):

`experiments1.py`

## Running model visualization
We have seperated model visualization from the model itself (seperation of concerns). Since visualization is not an import element of this research, only a very basic one is included.

To run the model with visualization (according to specified params.jon), have a look at:

`visualization_demo.ipynb`

An example of a basic model visualization with 1000 EVs and 50% smart can be seen below:

![Alt Text](https://github.com/floristevito/SEN9120_Advanced_Agent_Based_Modelling/blob/main/figures/vis.gif)

## Running python tests
Pytest is used for testing. To run all test from the model directory run:

`pytest`

To run only model components tests:

`pytest test_components.py`

To run only model level tests:

`pytest test_model.py`