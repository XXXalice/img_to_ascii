from handler import encoder
from handler import logger


print('-------------------')
enc = encoder.Encoder()
print('-------------------')
log = logger.Logger('.aalog')
trace = log._trace_test()
print(trace[1])