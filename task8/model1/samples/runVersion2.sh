OUTPUT_DIR=/user/${USER}/submissionFolder/tasks/task8/final
OUTPUT_DIR_AUX=/user/${USER}/submissionFolder/tasks/task8/aux
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r $OUTPUT_DIR_AUX

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task8_fisrtMap \
  -D mapred.reduce.tasks=1 \
  -input /data/small/imdb/title.basics.tsv \
  -output $OUTPUT_DIR_AUX \
  -mapper mapper1.py \
  -reducer reducer1.py \
  -file mapper1.py \
  -file reducer1.py

hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task8_secondMap \
  -input /data/small/imdb/title.ratings.tsv \
  -input $OUTPUT_DIR_AUX \
  -output $OUTPUT_DIR \
  -mapper mapper2.py \
  -combiner combiner2.py \
  -reducer reducer2.py \
  -file mapper2.py \
  -file combiner2.py \
  -file reducer2.py

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
