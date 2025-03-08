import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):
    if VaR is None:
        # If VaR is not provided, determine VaR based on the confidence percentile
        VaR = np.percentile(losses, 100 * confidence)

    # Calculate ES as the average of losses exceeding the VaR threshold
    es_value = np.mean(losses[losses > VaR])
    return es_value

# Unit test
u = np.random.uniform(0, 100, 100000)

# Test the ES function with an confidence of 0.8
es_confidence = ES(losses=u, confidence=0.8)
print('ES with confidence:', np.round(es_confidence, 0) == 90)

# Test the ES function with a VaR of 80
es_var = ES(losses=u, VaR=80)
print('ES with VaR:', np.round(es_var, 0) == 90)
