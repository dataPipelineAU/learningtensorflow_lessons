import tensorflow as tf

from tests.Clustering.test_functions import create_samples, choose_random_centroids, plot_clusters


def test_cluster_one():
    n_features = 2
    n_clusters = 3
    n_samples_per_cluster = 500
    seed = 700
    embiggen_factor = 70

    centroids, samples = create_samples(n_clusters, n_samples_per_cluster, n_features, embiggen_factor, seed)
    initial_centroids = choose_random_centroids(samples, n_clusters)

    model = tf.initialize_all_variables()
    with tf.Session() as session:
        sample_values = session.run(samples)
        updated_centroid_value = session.run(initial_centroids)

    plot_clusters(sample_values, updated_centroid_value, n_samples_per_cluster)