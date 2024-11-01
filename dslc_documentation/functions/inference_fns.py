import numpy as np
import matplotlib.pyplot as plt
from permute.core import two_sample
from scipy import stats

def do_two_sample_perm_test(x_p, x_q, plot=True, reps=10**5, alternative='greater'):
    if len(x_p) == 0 or len(x_q) == 0:
        raise ValueError("Input arrays must not be empty.")

    p, t, distr = two_sample(x_p, x_q, reps=reps, stat='mean', alternative=alternative, keep_dist=True)

    print('Difference of means:', np.round(t, 5))
    print('P-value:', np.round(p, 5))    

    if plot:
        n, bins, patches = plt.hist(distr, 25, histtype='bar', density=True)
        plt.title('Permutation Distribution')
        plt.axvline(x=t, color='red', label='$\overline{X_p} - \overline{X_q}$= ' + str(np.round(t, 3)))
        plt.text(t, max(n)*0.8, f' P-value = {np.round(p, 5)}', color='red', fontsize=12)
        plt.xlabel('Difference of means')
        plt.ylabel('Density')

        # Replace T-distribution with Gaussian distribution
        mean = np.mean(distr)
        std = np.std(distr)
        x = np.linspace(mean - 4*std, mean + 4*std, 100)
        plt.plot(x, stats.norm.pdf(x, mean, std), lw=3, alpha=0.6, label='Gaussian Distribution')
        plt.legend()
        plt.show()
    return p


def test_hypothesis_for_criterion(all_steps_results, fn, plot=True, reps=10**3, alternative='greater'):
    # Apply the lambda function to filter the test population
    test_population = all_steps_results.copy()
    test_population = test_population[fn(test_population)]
    
    # Extract steps before and after as numpy arrays
    before_as_np_array = test_population['steps_before'].values
    after_as_np_array = test_population['steps_after'].values
    
    
    # Perform the two-sample permutation test
    p_value = do_two_sample_perm_test(after_as_np_array, before_as_np_array, plot=plot, reps=reps, alternative=alternative)
    return p_value

def benjamini_hochberg(p_values, alpha=0.05, plot=True):
    """
    Perform the Benjamini-Hochberg procedure to control the false discovery rate.
    
    Args:
        p_values: A dictionary of p-values, where keys are hypothesis names and values are p-values.
        alpha: The desired family-wise error rate (FWER).
        plot: Boolean indicating whether to plot the p-values and BH threshold.
    
    Returns:
        A list of successful hypotheses (i.e., hypotheses rejected at the given alpha level).
    """
    sorted_p_values = sorted(p_values.items(), key=lambda item: item[1])
    m = len(p_values)
    successful_hypotheses = []

    for i, (hypothesis, p_value) in enumerate(sorted_p_values):
        if p_value <= (alpha * (i + 1) / m):
            successful_hypotheses.append((hypothesis, p_value))

    if plot:
        # Calculate the Benjamini-Hochberg threshold values
        bh_threshold = [(alpha * (i + 1) / m) for i in range(m)]
        # Plot the p-values and highlight the significant ones
        plt.figure(figsize=(10, 6))
        plt.scatter(range(m), [p[1] for p in sorted_p_values], label='P-values')
        #print the associated p-value above each point
        for i, (hypothesis, p_value) in enumerate(sorted_p_values):
            plt.text(i, p_value-0.008, f"{p_value:.4f}", ha='center', va='top')
        plt.plot(range(m), bh_threshold, color='r', linestyle='--', label='BH Threshold')
        plt.xlabel('Hypothesis Index')
        plt.ylabel('P-value')
        plt.title('P-values for Multiple Hypotheses with Benjamini-Hochberg Threshold')
        plt.legend()
        plt.show()
# Print the list of successful hypotheses
    if successful_hypotheses:
        print("Successful Hypotheses (Rejected at alpha 0.05):")
        for hypothesis, p_value in successful_hypotheses:
            print(f"- Notification sent when {hypothesis} (p-value: {p_value:.4f})")
    else:
        print("No hypotheses were rejected at the given alpha level.")
    return successful_hypotheses
