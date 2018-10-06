OUTPUT_DIR=/user/${USER}/submissionFolder/tasks/task1
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task1 \
  -input /data/small/gutenberg \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -reducer reducer2.py \
  -file mapper.py \
  -file reducer2.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
