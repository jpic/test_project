def test_generator(build_id, pull):
    ENV_VAR_1 = ['foo', 'bar']
    ENV_VAR_2 = ['x', 'y']

    for x in ENV_VAR_1:
        for y in ENV_VAR_2:
            # there i can skip or implement basic logic
            yield {'CMD': './test.sh', 'ENV_VAR_1': x, 'ENV_VAR_2': y,
                   'RETRIES': 3, 'RETRY_AFTER': 600}
