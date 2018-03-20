from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from PIL import Image
import os

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)


# Our application logic will be added here

def cnn_model_fn(features, labels, mode):
    input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])

    conv1 = tf.layers.conv2d(inputs=input_layer, filters=32, kernel_size=[5, 5], padding='SAME', activation=tf.nn.relu)
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    conv2 = tf.layers.conv2d(inputs=pool1, filters=64, kernel_size=[5, 5], padding='SAME', activation=tf.nn.relu)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)

    dropout = tf.layers.dropout(inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout, units=10)

    # prediction
    predictions = {
        'classes': tf.argmax(input=logits, axis=1),
        'probabilities': tf.nn.softmax(logits, name='softmax_tensor')
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # onehot_labels = tf.one_hot(indices=tf.cast(labels, tf.int32), depth=10)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(loss=loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)
    if mode == tf.estimator.ModeKeys.EVAL:
        eval_metric_ops = {
            'accuracy': tf.metrics.accuracy(
                labels=labels, predictions=predictions['classes']
            )
        }
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def recognize(img_path):
    mnist_classifier = tf.estimator.Estimator(model_fn=cnn_model_fn, model_dir='tmp/mnist_convnet_model')
    img = Image.open(img_path).convert('L')
    im = img.convert('L').resize((28, 28), Image.ANTIALIAS)
    # 暂存像素值的一维数组
    arr = []
    for i in range(28):
        for j in range(28):
            # mnist 里的颜色是0代表白色（背景），1.0代表黑色
            pixel = 1.0 - float(im.getpixel((j, i))) / 255.0
            # pixel = 255.0 - float(img.getpixel((j, i))) # 如果是0-255的颜色值
            arr.append(pixel)

    arr1 = np.array(arr).reshape((1, 28, 28, 1))
    # pix_array = np.array(im).astype(np.float32)
    pix_array = arr1.astype(np.float32)
    pred_input_fn = tf.estimator.inputs.numpy_input_fn(x={'x': pix_array}, num_epochs=1, shuffle=False)
    pred_results = mnist_classifier.predict(input_fn=pred_input_fn)

    res = {}
    for result in pred_results:
        # print('result: {}'.format(result))
        print(result.get('classes'))
        res['class'] = str(result.get('classes'))
        print(type(result.get('classes')))
        print(max(result.get('probabilities')))
        res['probability'] = str(max(result.get('probabilities')))
        print(type(max(result.get('probabilities'))))

    return res
