# import tensorflow as tf
#
# # 모델 파일 경로
# pb_file_path = "./deep_sort/model_weights/mars-small128.pb"
#
# # TensorFlow 그래프 생성
# tf.compat.v1.reset_default_graph()
# graph = tf.compat.v1.Graph()
#
# # 가중치 텐서 개수 초기화
# total_weights = 0
#
# with tf.compat.v1.Session(graph=graph) as sess:
#     # 모델 파일 읽기
#     with tf.io.gfile.GFile(pb_file_path, "rb") as f:
#         graph_def = tf.compat.v1.GraphDef()
#         graph_def.ParseFromString(f.read())
#         sess.graph.as_default()
#         tf.import_graph_def(graph_def, name="")
#
#     # 가중치 확인
#     for op in graph.get_operations():
#         for tensor in op.values():
#             print(tensor.name, tensor.shape)
#             # 가중치 텐서 식별
#             if tensor.dtype == tf.float32 or tensor.dtype == tf.float64:
#                 total_weights += 1
#
# # 총 가중치 개수 출력
# print("Total number of weights:", total_weights)

import tensorflow as tf

# 주어진 출력에서 가중치 텐서의 모양과 이름
weight_shapes_and_names = {
    "conv1_1/weights:0": (3, 3, 3, 32),
    "conv1_2/weights:0": (3, 3, 32, 32),
    "conv2_1/1/weights:0": (3, 3, 32, 32),
    "conv2_3/1/weights:0": (3, 3, 32, 32),
    "conv3_1/1/weights:0": (3, 3, 32, 64),
    "conv3_3/1/weights:0": (3, 3, 64, 64),
    "conv4_1/1/weights:0": (3, 3, 64, 128),
    "conv4_3/1/weights:0": (3, 3, 128, 128),
    "fc1/weights:0": (16384, 128)
}

# 총 파라미터 수 초기화
total_params = 0

# 각 가중치 텐서의 크기를 곱하고 모두 더함
for weight_name, shape in weight_shapes_and_names.items():
    weight_size = tf.reduce_prod(shape)
    total_params += weight_size

# 총 파라미터 수 출력
print("Total number of parameters:", total_params.numpy())
