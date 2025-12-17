from ultralytics import RTDETR
# Load a model
model = RTDETR('./runs/train/cvpdl/cvpdl_10088/weights/best.pt')  # load an official model


# Validate the model
metrics = model.val(data='test_cvpdl.yaml',
                               imgsz=960,
                               conf=0.55,
                               device='0',
                               plots=True,
                               iou=0.5,
                               name='cvpdl_10088_valid_result'
                               )  # no arguments needed, dataset and settings remembered


print('map50-95')
print(metrics.box.map)

print('map50')
print(metrics.box.map50)

print('map75')
print(metrics.box.map75)

print('map_list')
print(metrics.box.maps)

# Accessing AP75 for each category
# Note: metrics.box.maps is already the list of mAP values for each category
ap75_each_category = metrics.box.maps
print('map_list_mAP75:')
print(ap75_each_category)

# If you want to print mAP values for specific IoU thresholds:
print('\nmAP values for different IoU thresholds:')
print(f'mAP@0.5: {metrics.box.map50}')
print(f'mAP@0.75: {metrics.box.map75}')
print(f'mAP@0.5:0.95: {metrics.box.map}')
