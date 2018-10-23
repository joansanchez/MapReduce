OUTPUT_DIR=/user/${USER}/submissionFolder/tasks/task10
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task10 \
  -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
  -D stream.map.output.field.separator=. \
  -D mapreduce.map.output.key.field.separator=. \
  -D stream.num.map.output.key.fields=2 \
  -D num.key.fields.for.partition=1 \
  -D mapreduce.partition.keypartitioner.options=-k1 \
  -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2nr" \
  -input /data/large/imdb/title.basics.tsv \
  -input /data/large/imdb/name.basics.tsv \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
