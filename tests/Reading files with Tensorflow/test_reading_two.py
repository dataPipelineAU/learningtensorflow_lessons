import tensorflow as tf
import os


def test_reading_two():
    def create_file_reader_ops(filename_queue):
        reader = tf.TextLineReader(skip_header_lines=1)
        _, csv_row = reader.read(filename_queue)
        record_defaults = [[""], [""], [0], [0], [0], [0]]
        country, code, gold, silver, bronze, total = tf.decode_csv(csv_row, record_defaults=record_defaults)
        features = tf.stack([gold, silver, bronze])
        return features, country

    dir_path = os.path.dirname(os.path.realpath(__file__))
    filenames = [dir_path + "/olympics2016.csv"]
    filename_queue = tf.train.string_input_producer(filenames, num_epochs=1, shuffle=False)
    example, country = create_file_reader_ops(filename_queue)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        while True:
            try:
                example_data, country_name = sess.run([example, country])
                print(example_data, country_name)
            except tf.errors.OutOfRangeError:
                break