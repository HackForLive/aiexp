from datetime import datetime


if __name__ == "__main__":
    from curve import Curve, InterpolationMethod

    c = Curve(nodes={datetime(2022, 1, 1): 1.00,
                     datetime(2022, 4, 1): 0.9975,
                     datetime(2022, 7, 1): 0.9945},
              interpolation=InterpolationMethod.LOG_LINEAR)
    print(c)
    print(c[datetime(2022, 3, 15)])
    print(c[datetime(2022, 4, 1)])