# CS408-Team-2
2021 Fall KAIST CS408 Team Project

Requirements
----
- GPU that supports `CUDA==11.3`
- Python 3.9.7

How To Run
----
- Download pretrained model from `https://drive.google.com/file/d/1H1Z1_fdOV-5mRiSlb58MQ5zA8g-NBF-a/view?usp=sharing` and import into `{Project}/model/run/pytorch_model.bin`
- Download dataset from `https://drive.google.com/file/d/1_af78sAEm-w2MGSQns7xK6smzt9UzAfe/view?usp=sharing` and import into `{Project}/result.txt`
- Install requirements with `pip install -r requirements.txt`

### Dataset Acquisition
- Run `preprocessing.py`

### Data preprocessing
- Run `model/preprocess.ipynb`

### Model train
- Run `model/train_script.py`

### Model demo
- Run `model/test_script.py`

### Run Web Service
- `python web/manage.py runserver`
- Access with browser on `localhost:5000`