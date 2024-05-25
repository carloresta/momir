import pandas as pd

#=================================
#    LEVELLING BY CAPRARO DATA
#=================================
T_CAPRARO_DATA = pd.read_parquet('data/tower/parquet_data/capraro/tower_levelling')
T_CAPRARO_BENCHMARKS = pd.read_parquet('data/tower/parquet_data/capraro/tower_benchmark_positions')

#=====================================
#    STABILIZATION BENCHMARKS DATA
#=====================================
T_STABIL_COORDS = pd.read_parquet('data/tower/parquet_data/stabil_bench_coords')
T_STABIL_DISP = pd.read_parquet('data/tower/parquet_data/stabil_bench_disp')