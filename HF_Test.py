from transformers import pipeline
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
resp = captioner("dog.jpg")
print(resp)
# import torch
# from torch import hub
# resnet18 = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)