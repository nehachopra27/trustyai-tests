from enum import Enum, auto


class MetricType(Enum):
    FAIRNESS = auto()
    DRIFT = auto()


class Metric(Enum):
    # Fairness metrics
    SPD = ("spd", MetricType.FAIRNESS)
    DIR = ("dir", MetricType.FAIRNESS)

    # Drift metrics
    MEANSHIFT = ("meanshift", MetricType.DRIFT)
    FOURIERMMD = ("fouriermmd", MetricType.DRIFT)
    KSTEST = ("kstest", MetricType.DRIFT)
    APPROXKSTEST = ("approxkstest", MetricType.DRIFT)

    def __init__(self, value, metric_type):
        self._value_ = value
        self.metric_type = metric_type


def get_metric_endpoint(metric, schedule=False):
    base_endpoint = "/metrics/group/fairness" if metric.metric_type == MetricType.FAIRNESS else "/metrics/drift"
    endpoint = f"{base_endpoint}/{metric.value}"

    if schedule:
        endpoint += "/request"

    return endpoint