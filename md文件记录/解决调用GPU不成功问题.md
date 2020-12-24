# 解决调用不成功问题
# 经常出现以下问题：
2020-05-27 09:46:18.549599: E C:\users\nwani\_bazel_nwani\mmtm6wb6\execroot\org_tensorflow\tensorflow\stream_executor\cuda\cuda_dnn.cc:455] could not create cudnn handle: CUDNN_STATUS_ALLOC_FAILED
2020-05-27 09:46:18.556087: F C:\users\nwani\_bazel_nwani\mmtm6wb6\execroot\org_tensorflow\tensorflow\core\kernels\conv_ops.cc:713] Check failed: stream->parent()->GetConvolveAlgorithms( conv_parameters.ShouldIncludeWinogradNonfusedAlgo<T>(), &algorithms)

# 解决方法：
```py
# 导入下列语句解决GPU调用不成功问题
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
```