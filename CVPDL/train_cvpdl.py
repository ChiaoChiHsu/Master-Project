from ultralytics import RTDETR

model = RTDETR('./ultralytics/cfg/models/rt-detr/rtdetr-x.yaml').load('rtdetr-x.pt')

result = model.train(data='coco_cvpdl.yaml', device="0,1", batch=8, epochs=400, patience=50, imgsz=960, optimizer='Adam', lr0=0.00015, weight_decay=0.00015, cls=0.6, dfl=1.6, project='runs/train/cvpdl/', name='cvpdl_1015', augment=True, resume=True, fliplr=1.0, copy_paste=1.0)



# Load the partially trained model
#model = RTDETR("/home/dinci_root/workspace/ultralytics/runs/train/cvpdl/cvpdl_1009/weights/last.pt")

# Resume training
#results = model.train(resume=True)
