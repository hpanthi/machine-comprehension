import tensorflow as tf
#question module
#tensor storing all the questions
query = tf.placeholder(tf.float32,[None,None,D], "query")

#tensor stores the length of all the questions
input_query_lengths = tf.placeholder(tf.int32,[None,2],"query_lengths")

question_module_outputs, _ = tf.nn.dynamic_rnn(gru_drop, query, dtype=tf.float32, scope=tf.VariableScope(True,"input_module"))

#stores the input module outputs as per their sentence endings
q=tf.gather_nd(question_module_outputs, input_query_lengths)

