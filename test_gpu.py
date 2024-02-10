import tensorflow as tf
ans =  tf. __version__
# print(ans)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
