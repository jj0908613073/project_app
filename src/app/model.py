import gzip
import pickle
import torch

def predict(text1,text2):
    model.eval()
    inputs = tokenizer(text1,text2, padding=True, return_tensors='pt')
    outputs = model(**inputs)
    logits = outputs[0]
    _,pred = torch.max(logits.data, 1)
    pred=pred.tolist()
    print(pred[0])
    if pred[0] == 2 :
        print("unrelated")
        return("unrelated")
    elif pred[0] == 1 :
        print("disagree")
        return("disagree")
    else :
        print("agree")
        return("agree")



from transformers import BertTokenizer
from transformers import BertForSequenceClassification
PRETRAINED_MODEL_NAME = "bert-base-chinese"  # 指定繁簡中文 BERT-BASE 預訓練模型

# 取得此預訓練模型所使用的 tokenizer
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
#創建BERT模型
model = BertForSequenceClassification.from_pretrained('bert-base-chinese',num_labels=3)
#載入模型參數
#model.Load state_dict(torch.Load('model.plk2'))

#將模型設置為評估模式

with gzip.open('D:/flask/app/model/bertChinese.pgz','r') as f :
    model = pickle.load(f)





    
    