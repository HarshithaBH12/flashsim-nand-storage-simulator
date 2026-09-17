from flashsim import Metrics

def test_write_amplification():
    metrics = Metrics(writes=10, pages_moved=5)
    assert metrics.write_amplification() == 1.5
