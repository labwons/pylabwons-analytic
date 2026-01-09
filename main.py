import pandas as pd
import pylabwons as lw
import os


pd.set_option('display.expand_frame_repr', False)
if __name__ == "__main__":
    file = '2508150300_2512181300_3000x6x446.parquet'
    data = pd.read_parquet(
        os.path.join(os.path.dirname(__file__), f'archive/{file}'),
        engine='pyarrow'
    )

    test = lw.BackTester(data)
    test.calc_return(5)
    test.add_bollinger_band('close', window=20, std=2)
    test.add_macd('close', window_slow=26, window_fast=12, window_sign=9)
    test.add_average_true_range(window=10)
    test.add_volume_roc(window=7)
    test.add_obv_slope(window=12)
    test.add_rsi(window=9)
    test_stack = test.stack(level=0, future_stack=True)
    # print(test)
    # print(test_stack)

