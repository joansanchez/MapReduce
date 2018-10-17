OUTPUT_DIR=/user/${USER}/submissionFolder/tasks/task8
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task8 \
  -D mapred.reduce.tasks=9 \
  -input /data/small/imdb/title.basics.tsv \
  -output $OUTPUT_DIR \
  -mapper mapper1.py \
  -combiner combiner1.py \
  -reducer reducer1.py \
  -file mapper1.py \
  -file combiner1.py \
  -file reducer1.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
