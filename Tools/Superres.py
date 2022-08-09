import cv2

def init(model_path):
    modelName = model_path.split("models/")[-1].split("_")[0].lower()
    modelScale = model_path.split("_x")[-1]
    modelScale = int(modelScale[:modelScale.find(".")])
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(model_path)
    sr.setModel(modelName, modelScale)
    return sr

