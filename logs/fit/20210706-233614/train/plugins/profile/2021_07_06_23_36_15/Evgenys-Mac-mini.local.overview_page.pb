�	�p;4,�%@�p;4,�%@!�p;4,�%@	�a���?�a���?!�a���?"{
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails:�p;4,�%@��_cD�?A X9�i%@Y��Y5ѧ?rEagerKernelExecute 0*	�"��~�M@2U
Iterator::Model::ParallelMapV2�$"����?!a��*�<@)�$"����?1a��*�<@:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeatka�9͒?!��A���>@)P4`�_�?1ʉ���9@:Preprocessing2F
Iterator::Model\kF�?!D����D@)w���}?1O��'�?(@:Preprocessing2v
?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate����?!de��f�2@)}"O��y?11C���%@:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice%�c\qqt?!��â�� @)%�c\qqt?1��â�� @:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip�M�d��?!�="�}M@)i��Q�q?1U���@:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor:vP��h?!�?�9l@):vP��h?1�?�9l@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMapPqx�܉?!)����15@)����eV?1&�3��Z@:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.4% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9�a���?IS�^�X@Zno#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	��_cD�?��_cD�?!��_cD�?      ��!       "      ��!       *      ��!       2	 X9�i%@ X9�i%@! X9�i%@:      ��!       B      ��!       J	��Y5ѧ?��Y5ѧ?!��Y5ѧ?R      ��!       Z	��Y5ѧ?��Y5ѧ?!��Y5ѧ?b      ��!       JCPU_ONLYY�a���?b qS�^�X@Y      Y@q�5[6��?"�
device�Your program is NOT input-bound because only 0.4% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQ2"CPU: B 