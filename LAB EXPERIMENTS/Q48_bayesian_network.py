# P(A|B) using Bayes theorem
p_disease=0.01
p_positive_given_disease=0.95
p_positive_given_no_disease=0.05
p_positive=p_positive_given_disease*p_disease+p_positive_given_no_disease*(1-p_disease)
posterior=p_positive_given_disease*p_disease/p_positive
print("P(Disease):",p_disease)
print("P(Positive test):",round(p_positive,4))
print("P(Disease | Positive):",round(posterior,4))
